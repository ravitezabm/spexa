from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class ProductCategory(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subcategories', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='categories/')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = RichTextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"Image for {self.product.title}"

class Banner(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True)
    image = models.ImageField(upload_to='banners/')
    show_on_homepage = models.BooleanField(default=True)

    def __str__(self):
        return self.title



class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.title):
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exclude(id=self.id).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True)
    quote = models.TextField()
    photo = models.ImageField(upload_to='testimonials/', blank=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)  # Allow blank so it can be auto-filled
    description = models.TextField(default="Coming soon")
    image = models.ImageField(upload_to='services/', default='services/default.jpg')
    thumb = models.ImageField(upload_to='services/', default='services/default.jpg')
    short_description = models.CharField(max_length=300)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            while Service.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='certificates/')

    def __str__(self):
        return self.name

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='company_profiles/')

    def __str__(self):
        return self.name

class Career(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    posted_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class AboutSection(models.Model):
    banner = models.ImageField(upload_to='about/')
    image1 = models.ImageField(upload_to='about/')
    image2 = models.ImageField(upload_to='about/')
    image3 = models.ImageField(upload_to='about/')


