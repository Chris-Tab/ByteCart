from django.db import models
from decimal import Decimal
from billing.models import BillingProfile
from django.db.models.signals import pre_save, post_save
from bytecart.utils import unique_order_id_generator
from carts.models import Cart
from addresses.models import Address

ORDER_STATUS_CHOICES =(
    ("created", "Created"),
    ("paid", "Paid"),
    ("shipped", "Shipped"),
    ("refunded", "Refunded"),
    ("canceled", "Canceled"),
)

class OrderManager(models.Manager):
    def new_or_get(self, billing_profile, cart_obj):
        created = False
        qs = self.filter(billing_profile=billing_profile, cart=cart_obj, active=True)
        if qs.count() == 1:            
            order_obj = qs.first()
        else:
            order_obj = self.create(billing_profile=billing_profile, cart=cart_obj)
            created = True
        return order_obj, created


class Order(models.Model):

    billing_profile     = models.ForeignKey(BillingProfile, on_delete=models.CASCADE, null=True, blank=True)
    order_id            = models.CharField(max_length=120, blank=True)    
    shipping_address    = models.ForeignKey(Address, null=True, blank=True, on_delete=models.SET_NULL, related_name='shipping_address')
    billing_address     = models.ForeignKey(Address, null=True, blank=True, on_delete=models.SET_NULL, related_name='billing_address')
    cart                = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='orders')
    status              = models.CharField(max_length=120, default="created", choices=ORDER_STATUS_CHOICES)
    shipping_total      = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
    order_total         = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    active              = models.BooleanField(default=True)


    def __str__(self):
        return self.order_id
    
    objects = OrderManager()
    
    def update_total(self):
        cart_total = self.cart.total or Decimal('0.00')

        shipping_total = self.shipping_total
        if isinstance(shipping_total, float):
            shipping_total = Decimal(str(shipping_total))
        elif shipping_total is None:
            shipping_total = Decimal('0.00')

        new_total = cart_total + shipping_total
        self.order_total = new_total
        return new_total
    
def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)
    qs = Order.objects.filter(cart=instance.cart).exclude(billing_profile=instance.billing_profile)
    if qs.exists():
        qs.update(active=False)


    if instance.cart:
        instance.cart.save()  # make sure cart.total is up-to-date

        cart_total = instance.cart.total or Decimal('0.00')

       
        shipping_total = instance.shipping_total
        if isinstance(shipping_total, float):
            shipping_total = Decimal(str(shipping_total))  # safest way
        elif shipping_total is None:
            shipping_total = Decimal('0.00')

        instance.order_total = cart_total + shipping_total


pre_save.connect(pre_save_create_order_id, sender=Order)  


def post_save_cart_total(sender, instance, created,*args, **kwargs):
    if not created:
        cart_obj = instance
        cart_total = cart_obj.total
        cart_id = cart_obj.id
        qs = Order.objects.filter(cart__id=cart_id)
        if qs.count() == 1:
            order_obj = qs.first()
            order_obj.update_total()
    
post_save.connect(post_save_cart_total, sender=Cart)

def post_save_order (sender, instance, created, *args, **kwargs):
    print("running")
    if created:
        print("Updating first")
        instance.update_total()

post_save.connect(post_save_order, sender=Order)