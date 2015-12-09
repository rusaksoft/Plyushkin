from django.db import models

class Source(models.Model):
    url = models.TextField()
    login = models.TextField()
    password = models.TextField()

class Resource(models.Model):
    source = models.ForeignKey(Source, blank=True)
    path = models.TextField(blank = True)
    include = models.TextField(blank = True)
    exclude = models.TextField(blank = True)

class Storage(models.Model):
	name = models.CharField(max_length=255, blank=True)
	access_type = models.TextField()
	login = models.TextField()
	password = models.TextField()
	url = models.TextField()

	last_check = models.DateTimeField(null = True, blank = True)

	#restrictions, in MB
	max_space = models.IntegerField(blank=True, null = True)
	
	#restrictions on some backup spaces
	max_file_count = models.IntegerField(blank=True, null = True) 

	def free_space_status(self):
		return "No info"

	def __str__(self):
		return self.name or self.url

class Action(models.Model):
	name = models.TextField()
	notes = models.TextField(blank = True, null = True)
	
	resource = models.ForeignKey(Resource, blank = True, null = True)

	#for duplicity, simple_last_file_date, week1_2_last_date
	check_method = models.CharField(max_length=255, blank = True)

	#destination
	storage = models.ForeignKey(Storage)
	dest_path = models.TextField()

	#cron like: 0 5 * * * 
	schedule = models.TextField(blank = True)

	last_check = models.DateTimeField(null = True, blank = True)
	status = models.TextField(blank = True)

	def __str__(self):
		return self.name