from django.contrib import admin
from product.models.expendituremodel import Expenditure
from product.models.datamodel import Incoming, Outgoing

# Register your models here.


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['__str__', 'status',]

#     # def product_name(self, obj):
#     #     data = Product.objects.get(incoming_product=obj.pk)
#     #     return Incoming.objects.get(product=data).name


@admin.register(Expenditure)
class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount', 'date',]
    

@admin.register(Incoming)
class IncomingAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'model', 'price', 'owner', 'contact', 'date', 'stock']




@admin.register(Outgoing)
class OutgoingAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price', 'customer', 'contact', 'date',]