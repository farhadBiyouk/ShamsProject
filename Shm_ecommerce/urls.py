from django.urls import path
from .views import index, preview

urlpatterns = [
    path('', index, name="homePage"),
    path('preview/', preview, name="previewPage")
]