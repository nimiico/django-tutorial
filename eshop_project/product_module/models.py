from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, verbose_name='عنوان در url')

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=300)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
    price = models.IntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0 )
    short_description = models.CharField(max_length=360, null=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True)  # samsung galaxy s20 -> samsung-galaxy-s20

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)  # samsung galaxy s20 -> samsung-galaxy-s20
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"