import django_filters
from .models import Product, Review

class ProductFilter(django_filters.FilterSet):
    # Narx bo'yicha oraliq filter (min va max)
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    
    # Kategoriya slug'i bo'yicha filter (masalan: ?category=telefonlar)
    category = django_filters.CharFilter(field_name="category__slug", lookup_expr="exact")

    class Meta:
        model = Product
        fields = ["category", "min_price", "max_price"]

# Bonus vazifa (Review) uchun filter
class ReviewFilter(django_filters.FilterSet):
    product_id = django_filters.NumberFilter(field_name="product__id")

    class Meta:
        model = Review
        fields = ['product_id']

