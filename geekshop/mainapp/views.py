from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')


def contact(request):
    return render(request, 'mainapp/contact.html')


def date_and_title(request):
    return render(request, 'mainapp/date_and_title.html')


