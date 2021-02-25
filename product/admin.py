from django.contrib import admin
from product.models.expendituremodel import Expenditure
from product.models.datamodel import Incoming, Outgoing
from product.models.contactmodel import Contact, Newsletter

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
    list_display = ['name', 'slug', 'image', 'model', 'price', 'owner', 'contact', 'date', 'stock']




@admin.register(Outgoing)
class OutgoingAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price', 'customer', 'contact', 'date',]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message',]


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['__str__',]