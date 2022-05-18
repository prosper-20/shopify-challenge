import imp
from django.urls import reverse, reverse_lazy
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.text import slugify
from django.utils import timezone

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
	seller = models.CharField(max_length=30)
	slug = models.SlugField()
	specifications = models.TextField(blank=True, null=True)


	def get_absolute_url(self):
		return reverse("product-detail", kwargs={'slug': self.slug})


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



class Comment(models.Model):
	product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	body = models.TextField('Enter your commment...')
	date_added = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return f"{self.name}"

	def get_absolute_url(self):
		return reverse("product-detail", kwargs={
			'slug': self.slug
		})

	def get_success_url(self):
		return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})


LOCATION_CHOICES = (
	("1", "AFRICA"),
	("2", "EUROPE"),
	("3", "AUSTRALIA"),
	("4", "SOUTH AMERICA"),
	("5", "OTHER")
)


class Warehouse(models.Model):
	name = models.CharField(max_length=100)
	location = models.CharField(choices=LOCATION_CHOICES, max_length=20)
	item = models.ManyToManyField(Product, related_name="warehouse_item")
	date_stored = models.DateTimeField(default=timezone.now)

	def __str__(self):
    		return self.name





	