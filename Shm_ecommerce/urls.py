from django.urls import path
from .views import index, preview, products, about, contact

urlpatterns = [
    path('', index, name="homePage"),
    path('preview/', preview, name="previewPage"),
    path('products/', products, name="productsPage"),
    path('about/', about, name="aboutPage"),
    path('contact-us, contact, name="contactPage")
]
