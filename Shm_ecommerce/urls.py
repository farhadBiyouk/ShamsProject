from django.urls import path
from .views import index, preview, products, about

urlpatterns = [
    path('', index, name="homePage"),
    path('preview/', preview, name="previewPage"),
    path('products/', products, name="productsPage"),
    path('about/', about, name="aboutPage")
]
