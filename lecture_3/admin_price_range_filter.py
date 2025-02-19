

from django.contrib import admin
from main_app.models import Product
from django.utils.translation import gettext_lazy as _
from django.db.models import Q

# admin.site.register(Product)


class PriceRangeFilter(admin.SimpleListFilter):
    title = _('price range')  # Filter title
    parameter_name = 'price_range'  # Query parameter

    def lookups(self, request, model_admin):
        return [
            ('1-100', _('1-100')),
            ('101-200', _('101-200')),
            ('201-300', _('201-300')),
        ]

    def queryset(self, request, queryset):
        if self.value() == '1-100':
            return queryset.filter(price__gte=1, price__lte=100)
        elif self.value() == '101-200':
            return queryset.filter(price__gte=101, price__lte=200)
        elif self.value() == '201-300':
            return queryset.filter(price__gte=201, price__lte=300)
        return queryset


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_on')
    search_fields = ('name', 'category', 'supplier')
    list_filter = (PriceRangeFilter,)
    fieldsets = (
        ('General Information',
         {'fields': ('name', 'description', 'price', 'barcode')}),
        ('Categorization', {'fields': ('category', 'supplier')})
    )
    date_hierarchy = 'created_on'