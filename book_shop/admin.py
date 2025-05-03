from django.contrib import admin
from .models import *
admin.site.register(
    [Author, Book, Customer, Order]
)
# Register your models here.
