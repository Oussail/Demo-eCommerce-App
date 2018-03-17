from django.views.generic import ListView, DetailView

from .models import Product


class ProductListView(ListView):
	queryset = Product.objects.all()


class ProductDetailView(DetailView):
	queryset = Product.objects.all()



