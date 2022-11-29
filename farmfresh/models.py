from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=250)
    author_name = models.CharField(max_length=250)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'mobile_images')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to = 'mobile_images', null=True, blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=350)
    price = models.FloatField(default=0)
    product_date = models.DateTimeField()
    update_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'mobile_images')

    class Meta:
        ordering = ['-product_date']

    def __str__(self):
        return self.title


class Country(models.Model):
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.country


class City(models.Model):
    city = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.city


class Farmer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    adress = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'mobile_images', null=None)
    twitter_url = models.CharField(max_length=200, null=True, blank=True)
    facebook_url = models.CharField(max_length=200, null=True, blank=True)
    linkedin_url = models.CharField(max_length=200, null=True, blank=True)
    instagram_url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.first_name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    adress = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)
    image = models.ImageField(upload_to = 'mobile_images', null=True, blank=True)

    def __str__(self):
        return self.first_name


class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.FloatField(default=0)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer, self.farmer, self.product


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to = 'mobile_images', null=True, blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=255)

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    adress = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    twitter_url = models.CharField(max_length=200, null=True, blank=True)
    facebook_url = models.CharField(max_length=200, null=True, blank=True)
    linkedin_url = models.CharField(max_length=200, null=True, blank=True)
    instagram_url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.adress


class Fact(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    image = models.ImageField(upload_to = 'mobile_images', null=True, blank=True)


    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)