from django.shortcuts import render


def index(request, ):
    return render(request, 'index.html')


def preview(request, ):
    return render(request, 'preview.html')


def products(request):
    return render(request, 'product.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'about.html')
