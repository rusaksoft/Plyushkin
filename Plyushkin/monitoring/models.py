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

	free_space = models.IntegerField(blank=True, null=True)

	def free_space_status(self):
		unit = "MB"
		free_space = self.free_space
		max_space = self.max_space
		if free_space > 1000 or max_space > 1000:
			unit = "GB"
			free_space = free_space / 1000
			max_space = max_space / 1000

		status = str(free_space)+" "+unit

		warning = False

		if max_space:
			quota = round(float(free_space)/max_space*100,2)
			status += " of "+str(max_space)+" "+unit
			status += " ("+str(quota)+"%)"

			#warning if quota less than 5%
			warning = quota < 5

		print warning

		return (status, warning)



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