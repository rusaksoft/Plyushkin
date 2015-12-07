from django.contrib import admin
from monitoring.models import *

# Register your models here.
admin.site.register(Storage)
admin.site.register(Source)
admin.site.register(Resource)
admin.site.register(Action)
