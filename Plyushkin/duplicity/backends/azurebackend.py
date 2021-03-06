# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright 2013 Matthieu Huin <mhu@enovance.com>
# Copyright 2015 Scott McKenzie <noizyland@gmail.com>
#
# This file is part of duplicity.
#
# Duplicity is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# Duplicity is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with duplicity; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

import os

import duplicity.backend
from duplicity import log
from duplicity.errors import BackendException


class AzureBackend(duplicity.backend.Backend):
    """
    Backend for Azure Blob Storage Service
    """
    def __init__(self, parsed_url):
        duplicity.backend.Backend.__init__(self, parsed_url)

        # Import Microsoft Azure SDK for Python library.
        try:
            import azure
            from azure.storage import BlobService
        except ImportError:
            raise BackendException('Azure backend requires Microsoft Azure SDK for Python '
                                   '(https://github.com/Azure/azure-sdk-for-python).')

        if 'AZURE_ACCOUNT_NAME' not in os.environ:
            raise BackendException('AZURE_ACCOUNT_NAME environment variable not set.')

        if 'AZURE_ACCOUNT_KEY' not in os.environ:
            raise BackendException('AZURE_ACCOUNT_KEY environment variable not set.')

        account_name = os.environ['AZURE_ACCOUNT_NAME']
        account_key = os.environ['AZURE_ACCOUNT_KEY']
        self.WindowsAzureMissingResourceError = azure.WindowsAzureMissingResourceError
        self.blob_service = BlobService(account_name=account_name, account_key=account_key)
        # TODO: validate container name
        self.container = parsed_url.path.lstrip('/')
        try:
            self.blob_service.create_container(self.container, fail_on_exist=True)
        except azure.WindowsAzureConflictError:
            # Indicates that the resource could not be created because it already exists.
            pass
        except Exception as e:
            log.FatalError("Could not create Azure container: %s"
                           % unicode(e.message).split('\n', 1)[0],
                           log.ErrorCode.connection_failed)

    def _put(self, source_path, remote_filename):
        # http://azure.microsoft.com/en-us/documentation/articles/storage-python-how-to-use-blob-storage/#upload-blob
        self.blob_service.put_block_blob_from_path(self.container, remote_filename, source_path.name)

    def _get(self, remote_filename, local_path):
        # http://azure.microsoft.com/en-us/documentation/articles/storage-python-how-to-use-blob-storage/#download-blobs
        self.blob_service.get_blob_to_path(self.container, remote_filename, local_path.name)

    def _list(self):
        # http://azure.microsoft.com/en-us/documentation/articles/storage-python-how-to-use-blob-storage/#list-blob
        blobs = self.blob_service.list_blobs(self.container)
        return [blob.name for blob in blobs]

    def _delete(self, filename):
        # http://azure.microsoft.com/en-us/documentation/articles/storage-python-how-to-use-blob-storage/#delete-blobs
        self.blob_service.delete_blob(self.container, filename)

    def _query(self, filename):
        prop = self.blob_service.get_blob_properties(self.container, filename)
        return {'size': int(prop['content-length'])}

    def _error_code(self, operation, e):
        if isinstance(e, self.WindowsAzureMissingResourceError):
            return log.ErrorCode.backend_not_found

duplicity.backend.register_backend('azure', AzureBackend)
