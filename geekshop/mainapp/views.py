from django.shortcuts import render

# Create your views here.
from .models import Product

title = 'Главная'
products = Product.objects.all()
new_content = {'title': title, 'products': products}

content = {
    'new_content' : {'title': title, 'products': products},
    'links' : [
    {'href': 'main', 'name': 'домой'},
    {'href': 'product', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
    ]
}


def main(request):

    return render(request, 'mainapp/index.html', content)


def products(request):
    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html', content)


def date_and_title(request):
    return render(request, 'mainapp/date_and_title.html')


