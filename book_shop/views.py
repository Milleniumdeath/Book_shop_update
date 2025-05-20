from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import *
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
    if request.method=="POST":
        form_data = AuthorForm(request.POST)
        if form_data.is_valid():
            data = form_data.cleaned_data
            Author.objects.create(
                name=data['name'],
                birth_year=data['birth_year']
            )

        # Author.objects.create(
        #     name=request.POST.get("name"),
        #     birth_year = int(request.POST.get("birth_year"))
        # )
        return redirect('yozuvchi')
    authors = Author.objects.all()
    context = {
        'authors' : authors,
        'form': AuthorForm,
    }
    return render(request, 'authors.html', context=context)

def books_view(request):
    if request.method == "POST":
        form_data = BookForm(request.POST)
        if form_data.is_valid():
            form_data.save()

        return redirect('books')

    books = Book.objects.all()

    yozuvchilar = Author.objects.order_by('name')
    search = request.GET.get('search')
    if search is not None:
        books = books.filter(title__contains=search)

    kitob = {
        'books' : books,
        'search': search,
        'yozuvchilar': yozuvchilar,
        'form': BookForm,
    }

    return render(request, 'books.html', context=kitob )

def customers_view(request):
    customers = Customer.objects.all()

    gender = request.GET.get('gender')
    if gender is not None:
        customers = Customer.objects.filter(jins=gender)

    customers = {
        'customers' : customers,
        'genders': Customer.Jinsi,
        'select_gender': gender
    }
    return render(request, 'customers.html', context=customers)

def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        'book': book,
    }
    return render(request, 'book_details.html', context)

def book_update_details(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        data = BookUpdateForm(request.POST, instance=book)
        if data.is_valid():
            data.save()
        return redirect('books')
    # yozuvchilar = Author.objects.order_by('name')
    context = {
        'book': book,
        # 'yozuvchilar': yozuvchilar,
        'form': BookUpdateForm(instance=book)
    }
    return render(request, 'book-update.html', context)

def book_delete_details(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('/books/')

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

def customer_tasdiq_delete(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    context = {
        'customer': customer,
    }
    return render(request, 'tasdiq-delete.html', context)

def customers_tasdiq_delete(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    customer.delete()
    return redirect('/customers/')