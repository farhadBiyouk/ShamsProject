from django.shortcuts import render


def index(request, ):
    return render(request, 'index.html')


def preview(request, ):
    return render(request, 'preview.html')
