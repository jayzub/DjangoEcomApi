from django.contrib import admin
from ecomapp import models


admin.site.register(models.Product)
admin.site.register(models.Cart)
admin.site.register(models.CartProduct)
