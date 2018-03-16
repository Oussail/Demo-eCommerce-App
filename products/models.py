import time
from django.db import models
import random
import os


def get_filename_ext(filename):
	base_name = os.path.basename(filename)
	name, ext = os.path.splitext(base_name)
	return name, ext


def upload_image_path(instance, filename):
	print(instance)
	print(filename)
	new_filename = random.randint(1, 99999999)
	name, ext = get_filename_ext(filename)
	return "products/images/{date}/{new_filename}{ext}".format(
		date=time.strftime("%Y/%m/%d"),
		new_filename=new_filename,
		ext=ext
	)


class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	price = models.DecimalField(decimal_places=2, max_digits=20)
	image = models.ImageField(upload_to=upload_image_path, null=True)

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

