from django.contrib.auth.models import User
from django.db import models


class Worker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    male = models.CharField(max_length=50)
    age = models.IntegerField()
    birthdate = models.DateField()
    jop_position = models.CharField(max_length=150)
    phone_number = models.IntegerField()


class CallBack(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()



class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    surname = models.CharField(max_length=100, verbose_name="Surname")
    age = models.IntegerField(verbose_name="Age")














class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    author = models.ManyToManyField(Author, verbose_name="Author")
    publish_date = models.DateField(verbose_name="Publish Date")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Price",
                                help_text='Number can be non whole')

    def __str__(self):
        return f"{self.title} by {self.author}"

















class Order(models.Model):
    class Status(models.TextChoices):
        NEW = 'n', 'New',
        PROGRESSING = 'p', 'In progressing',
        COMPLETED = 'c', 'Ended',
        CANCELED = 'x', 'Canceled',

    status = models.CharField(max_length=10,
                              choices=Status.choices,
                              default=Status.NEW,
                              verbose_name="Status order",)










class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Category Name")
    def __str__(self):
        return self.name







class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    description = models.TextField(max_length=200, verbose_name="Description")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Price")
    available = models.BooleanField(default=True, verbose_name="Available")
    release_date = models.DateField(verbose_name="Release Date", null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.PROTECT)


    def save(self, *args, **kwargs):
        if self.price <= 0:
            raise ValueError("Price must be greater than 0!")
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(verbose_name="Bio", blank=True, null=True)

    def __str__(self):
        return self.user.name











































