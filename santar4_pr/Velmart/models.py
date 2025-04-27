from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey
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


class Producer(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Name")
    last_name = models.CharField(max_length=100, verbose_name="Surname")
    birthdate = models.DateField()
    length_of_work = models.PositiveSmallIntegerField(verbose_name="Length of Work (years)")
    country = models.CharField(max_length=100, verbose_name="Country")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=100)
    producer = models.ForeignKey(Producer, related_name='movies', on_delete=models.CASCADE)
    creation_date = models.DateField(verbose_name="Creation Date")
    year = models.PositiveSmallIntegerField(verbose_name="Year")
    genre = models.CharField(max_length=100)
    country = models.CharField(max_length=100, verbose_name="Country")
    rate = models.FloatField()

    def __str__(self):
        return self.title


class User(models.Model):
    nickname = models.CharField(max_length=100, verbose_name="Nickname")
    email = models.EmailField()
    password = models.CharField(max_length=100, verbose_name="Password")
    favourite_movies = models.ManyToManyField(Movie, verbose_name="Favorite Movies")

    def __str__(self):
        return self.nickname

class Comment(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE)
    movie = ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500, help_text="Text your comment")
    date = models.DateField()

    def __str__(self):
        return self.comment

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    author = models.ManyToManyField(Author, verbose_name="Author")
    publish_date = models.DateField(verbose_name="Publish Date")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Price",
                                help_text='Number can be non whole')

    def __str__(self):
        return f"{self.title} by {self.author}"


class Rubrick(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")

    def __str__(self):
        return f"{self.title}"

class Goiteens(models.Model):
    title = models.CharField(max_length=100, help_text="Type caption for your announcement ")
    content = models.TextField(help_text="Your announcement")
    price = models.DecimalField(max_digits=8, decimal_places=2, help_text="Your price")
    rubrick = models.ForeignKey(Rubrick, on_delete=models.CASCADE, help_text="Type title of your rubrick")

class Spare(models.Model):
    name = models.CharField(max_length=100, help_text="Type name of spare")

    def __str__(self):
        return self.name

class Machine(models.Model):
    name = models.CharField(max_length=100, help_text="Type name of machine")
    spares = models.ManyToManyField(Spare,
                                    blank=True,
                                    related_name='machines',
                                    help_text="Type name of spare")
    def __str__(self):
        return self.name

class Product2(models.Model):
    name = models.CharField(max_length=100, verbose_name="Product Name")
    description = models.TextField(max_length=150, verbose_name="Product Description", blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Product Price")
    created_at = models.DateField(auto_now_add=True, verbose_name="Product Creation Date")

    def __str__(self):
        return self.name

class Order2(models.Model):
    STATUS_CHOICES = [
        ('pendding', 'Waiting'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    product = models.ForeignKey(
        Product2,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name="Product",
    )

    quantity = models.DecimalField(max_digits=10,
                                   decimal_places=2,
                                   verbose_name="Quantity",
                                   blank=True)

    order_date = models.DateField(auto_now_add=True, verbose_name="Order Date")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Status")

    def save(self, *args, **kwargs):
        self.total_price = self.product.price + self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} {self.quantity} {self.order_date}"



















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











































