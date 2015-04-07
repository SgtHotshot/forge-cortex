from django.db import models

# Create your models here.

MOD_TYPE_CHOICES = (
	('0', 'Forge'),
	('1', 'Bukkit'),
)

VISIBILITY_CHOICES = (
	('0', 'Visible'),
	('1', 'Hidden'),
	('2', 'Private'),
)


	



class String(models.Model):
	value = models.CharField(max_length=255)

class person(models.Model):
	firstName = models.CharField(max_length=20)
	lastName = models.CharField(max_length=20)
	isVerified = models.BooleanField(default=False)
	
class mod(models.Model):
	def generate_imagefilename(self, filename):
		url = "mods/%s/images/" % (self.mod.name)
		return url

	name = models.CharField(max_length=40)
	modType = models.CharField(max_length=1, choices=MOD_TYPE_CHOICES, blank=True)
	visibility = models.CharField(max_length=1, choices=VISIBILITY_CHOICES)
	logo = models.ImageField(upload_to=generate_imagefilename, blank=True)
	authors = models.ForeignKey(person, blank=True)
	recommended = models.OneToOneField('modVersion', related_name="recommended_mod")
	latest = models.OneToOneField('modVersion', related_name="latest_mod")
	website = models.URLField()
	description = models.TextField()
	license = models.TextField()
	tags = models.ManyToManyField(String, blank=True)
	
class modVersion(models.Model):
	def generate_filename(self, filename):
		url = "mods/%s/files/" % (self.mod.name)
		return url

	tags = models.ManyToManyField(String)
	version = models.CharField(max_length=40, blank=True)
	filename = models.CharField(max_length=120, blank=True)
	mod = models.ForeignKey(mod)
	file = models.FileField(upload_to=generate_filename)
