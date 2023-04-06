from django.contrib import admin
from .models import Base, Size, Option, Product, Material, Property

admin.site.register(Base)
admin.site.register(Size)
admin.site.register(Option)
admin.site.register(Product)
admin.site.register(Property)
admin.site.register(Material)
