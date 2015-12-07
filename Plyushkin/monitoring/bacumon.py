from duplicity import backend
from duplicity import log
from duplicity import globals

import re
from models import *
from datetime import datetime

log.setup()
backend.import_backends()
log.setverbosity(log.DEBUG)

def check_all():
	actions = Action.objects.all()

	for action in actions:
		check(action)

def build_url(action):
	storage = action.storage
	url = storage.access_type+"://"+storage.login + ":" + storage.password + "@" + storage.url + action.dest_path
	print url

	return url


def check(action):
	globals.ssl_no_check_certificate = True

	if action.check_method == "duplicity":
		check_duplicity(action)
	elif action.check_method == "simple_last_file_date":
		check_simple_last_file_date(action)
	elif action.check_method == "week1_2_last_file_date":
		check_week1_2_last_file_date(action)

def check_duplicity(action):
	dest = backend.get_backend(build_url(action))

	lst = dest.list()

	lst = [f for f in lst if f.startswith("duplicity-inc.") and f.endswith(".manifest.gpg")]
	#TODO is it safe check? can we sure these file creates after all backup uploaded?

	print lst

	lst = [re.search(".*to\.(.*)\.manifest.gpg",f).group(1) for f in lst]

	if not lst:
		action.status = "No files"
		action.last_check = datetime.now()
		action.save()
		return action.status 

	last_backup = datetime.strptime(max(lst),"%Y%m%dT%H%M%SZ")

	action.last_check = datetime.now()
	action.status = last_backup
	action.save()

	return action.status

def check_simple_last_file_date(action):
	action.status = _check_simple_last_file_date(action, backend.get_backend(build_url(action)))
	action.last_check = datetime.now()
	action.save()

def _check_simple_last_file_date(action, dest):
	lst = dest.list_with_attr()
	#TODO handle if year available in output

	year = datetime.now().year

	lst = [datetime.strptime(str(year)+" "+x[-4]+". "+x[-3]+", "+x[-2], "%Y %b. %d, %H:%M") for x in lst]

	return max(lst)


def check_week1_2_last_file_date(action):
	url = build_url(action)
	status1 = _check_simple_last_file_date(action, backend.get_backend(url + "/week1"))
	status2 = _check_simple_last_file_date(action, backend.get_backend(url + "/week2"))
	action.status = max([status1, status2])
	action.last_check = datetime.now()
	action.save()