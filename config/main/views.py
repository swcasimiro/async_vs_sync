from django.shortcuts import render
from .models import Product, Category
import os
import django

# async settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()


# async request
async def async_main(request):
    product = Product.objects.all()

    data = {
        'product': product
    }

    return render(request, 'async_main.html', data)


# sync request
def sync_main(request):
    product = Product.objects.all()

    data = {
        'product': product
    }

    return render(request, 'sync_main.html', data)
