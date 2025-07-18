from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from accounts.models import GuestEmail

User = settings.AUTH_USER_MODEL

class BillingProfileManager(models.Manager):
    def new_or_get(self, request):
        user = request.user
        guest_email_id = request.session.get('guest_email_id')
        created = False
        obj = None

        if user.is_authenticated:
            try:
                obj = self.model.objects.get(user=user)
                created = False
            except self.model.DoesNotExist:
                obj = self.model.objects.create(user=user, email=user.email)
                created = True

        elif guest_email_id is not None:
            try:
                guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
                obj, created = self.model.objects.get_or_create(email=guest_email_obj.email)
            except GuestEmail.DoesNotExist:
                obj = None
                created = False

        return obj, created

class BillingProfile(models.Model):
    user        = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    email       = models.EmailField(null=True, blank=True)
    active      = models.BooleanField(default=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)


    objects = BillingProfileManager()


    def __str__(self):
        return self.email
    

# def billing_profile_created_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         print("Actual API REQUEST Send to stripe/braintree")
#         instance.customer_id = newID
        instance.save()
        

def user_created_receiver(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)

post_save.connect(user_created_receiver, sender=User)