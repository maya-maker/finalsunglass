from django.contrib import admin
from product.models import Product,Category



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['c_name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['p_name','price','Category']
    list_filter = ['Category','price']
    search_fields=['p_name']


admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
