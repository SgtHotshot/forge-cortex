from django.db import models
import os

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


MODS = "mods"
IMAGES = "images"
FILES = "files"



class Tag(models.Model):
	value = models.CharField(max_length=255)

class Person(models.Model):
	firstName = models.CharField(max_length=20)
	lastName = models.CharField(max_length=20)
	isVerified = models.BooleanField(default=False)

class Mod(models.Model):
	def generate_imagefilename(self, filename):
		return os.path.join(MODS, self.name, IMAGES, filename)

	name = models.CharField(max_length=40)
	modType = models.CharField(max_length=1, choices=MOD_TYPE_CHOICES, blank=True)
	visibility = models.CharField(max_length=1, choices=VISIBILITY_CHOICES)
	logo = models.ImageField(upload_to=generate_imagefilename, blank=True)
	authors = models.ForeignKey(Person, blank=True)
	recommended = models.OneToOneField('ModVersion', related_name="recommended_mod")
	latest = models.OneToOneField('ModVersion', related_name="latest_mod")
	website = models.URLField()
	description = models.TextField()
	license = models.TextField()
	tags = models.ManyToManyField(Tag, blank=True)

class ModVersion(models.Model):
	def generate_filename(self, filename):
		return os.path.join(MODS, self.mod.name, FILES, filename)

	tags = models.ManyToManyField(Tag)
	version = models.CharField(max_length=40, blank=True)
	filename = models.CharField(max_length=120, blank=True)
	mod = models.ForeignKey(Mod)
	file = models.FileField(upload_to=generate_filename)
