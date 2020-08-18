from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from product.utils import unique_slug_generator
from product.models.datamodel import Incoming, Outgoing



@receiver(pre_save, sender=Incoming)
def product_pre_save_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        


@receiver(post_save, sender=Outgoing)
def update_incoming(sender, instance, **kwargs):
    product_instance = Incoming.objects.get(pk=instance.product.id)
    print(product_instance.name)
    product_instance.stock = 'Sold'
    
    product_instance.save()
    