from audioop import reverse
import imp
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.text import slugify

CHOICES = (
	("1", "Available"),
	("2", "Not Available")
)

class Brand(models.Model):
	name = models.CharField(max_length=255)
	status = models.CharField(max_length=10, choices=CHOICES)

	def __str__(self):
		return self.name


class Category(models.Model):
	name = models.CharField(max_length=255)
	status = models.CharField(max_length=10, choices=CHOICES)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.name


class Product(models.Model):
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	name = models.CharField(max_length=255)
	code = models.CharField(max_length=10)
	image = models.ImageField(upload_to="product_images")
	quantity = models.IntegerField()
	rate = models.FloatField(max_length=100)
	status = models.CharField(max_length=10, choices=CHOICES)
	seller = models.ForeignKey(User, on_delete=models.CASCADE)
	slug = models.SlugField(blank=True, default='')


	def get_absolute_url(self):
		return reverse("product-detail", args={'slug': self.slug})


	def __str__(self):
		return self.name

	def save(self, *args, **kwargs): # < here
		self.slug = slugify(self.title)
		super(Product, self).save()



	def save(self):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)


	