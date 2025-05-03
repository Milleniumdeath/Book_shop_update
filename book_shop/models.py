from django.db import models
#----------------------------------------------------------------------------------
class Author(models.Model):
    name = models.CharField(max_length=255)
    birth_year = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
#----------------------------------------------------------------------------------
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True )
    price = models.FloatField()
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.title
#----------------------------------------------------------------------------------
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name
#----------------------------------------------------------------------------------
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True )
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True )
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.customer)
#----------------------------------------------------------------------------------