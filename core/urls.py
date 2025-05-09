
from django.contrib import admin
from django.urls import path



from book_shop.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('hello/', hello_view),
    path('authors/', authors_view),
    path('books/', books_view),
    path('customers/', customers_view),
    path('book/', book_details),
    path('customer/', customer_details),
    path('price/', book_max_price),
    path('stock/', book_max_stock),
    path('like/', book_of_author),

]
