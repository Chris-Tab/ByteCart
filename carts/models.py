from django.conf import settings
from decimal import Decimal
from django.db import models
from django.db.models.signals import pre_save, m2m_changed

from products.models import Product



User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = self.new_cart(user=request.user)
            new_obj = True
            request.session["cart_id"] = cart_obj.id
        return cart_obj, new_obj

    def new_cart(self, user=None):
        if user is not None and user.is_authenticated:
            return self.model.objects.create(user=user)
        return self.model.objects.create()


class Cart(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products    = models.ManyToManyField(Product, blank=True)
    subtotal    = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total       = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)


# Update subtotal when products change
def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if action in ["post_add", "post_remove", "post_clear"]:
        products = instance.products.all()
        total = sum([p.price for p in products])
        instance.subtotal = total
        instance.save()

m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)


# Update total (with tax) just before saving
def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        instance.total = instance.subtotal * Decimal('1.08')  #  8% tax
    else:
        instance.total = Decimal('0.00')

pre_save.connect(pre_save_cart_receiver, sender=Cart)


def update_totals(self):
    self.subtotal = sum([p.price for p in self.products.all()])
    self.total = self.subtotal * Decimal('1.08') if self.subtotal > 0 else Decimal('0.00')
    self.save()