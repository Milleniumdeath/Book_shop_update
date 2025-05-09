from django.shortcuts import render
from django.http import HttpResponse

from .models import *
def hello_view(request):
    return HttpResponse(
        """
        <h1>Hello View</h1>
        <hr>
        <p>Bu  sahifa Httpresponse orqali chiqarildi! </p>
        """
    )

def home_view(request):
    return render(request, 'index.html')

def authors_view(request):
    authors = Author.objects.all()
    context = {
        'authors' : authors,
    }
    return render(request, 'authors.html', context=context)

def books_view(request):
    books = Book.objects.all()
    kitob = {
        'books' : books,
    }
    return render(request, 'books.html', context=kitob )

def customers_view(request):
    customers = Customer.objects.all()
    customers = {
        'customers' : customers,
    }
    return render(request, 'customers.html', context=customers)

def book_details(request):
    book = Book.objects.get(id=1)
    context = {
        'book': book,
    }
    return render(request, 'book_details.html', context)

def customer_details(request):
    customer = Customer.objects.get(id=1)
    context = {
        'customer': customer,
    }
    return render(request, 'customer_details.html', context)

def book_max_price(request):
    price = Book.objects.order_by('price').last()
    context = {
        'price': price,
    }
    return render(request, 'book_max_price.html', context)

def book_max_stock(request):

    stock = Book.objects.order_by('stock').last()
    context = {
        'stock': stock,
    }
    return render(request, 'book_max_stock.html', context)

def book_of_author(request):
    like = Author.objects.filter(name__contains="bek")
    books=[]
    for i in like:
        books.append(Book.objects.filter(author=i))

    context = {
        'like': like,
        'books':books[0]
    }
    return render(request, 'book_of_author.html', context)