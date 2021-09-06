from django.shortcuts import render

# Create your views here.

links_menu = {
    'links' : [
    {'href': 'main', 'name': 'домой'},
    {'href': 'product', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
    ]
}


def main(request):
    return render(request, 'mainapp/index.html', links_menu)


def products(request):
    return render(request, 'mainapp/products.html', links_menu)


def contact(request):
    return render(request, 'mainapp/contact.html', links_menu)


def date_and_title(request):
    return render(request, 'mainapp/date_and_title.html')


