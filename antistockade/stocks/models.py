from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=280, blank=True)
    cash = models.DecimalField(max_digits=10, decimal_places=2, default=10000) # cash either available or debt
    location = models.CharField(max_length=280, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} with ${self.cash} in hand"

@receiver(post_save, sender=User) # used for hooking up user creation w/ the default Django user table
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User) # used for hooking up user salvation w/ the default Django user table
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Transaction(models.Model): # used for keeping track of purchases and sales of stock
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    stockcode = models.CharField(max_length=6) # ticker symbol
    price = models.DecimalField(max_digits=10, decimal_places=2) # the price of the stock at the time;
                                  # negative numbers indicate a sale and positive numbers indicate a purchase
    amount = models.IntegerField() # no. of stocks sold or purchased;
                                   # negative numbers indicate a sale and positive numbers indicate a purchase
    time = models.DateTimeField(auto_now_add=True) # the date and time of this particular transaction

    def __str__(self):
        return f"{self.username} - {self.amount} of {self.stockcode} for ${self.price} each at {self.time}"

class Stock(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE) # which user owns this particular stock
    stockcode = models.CharField(max_length=6) # ticker symbol
    amount = models.IntegerField() # no. of stock owned

    def __str__(self):
        return f"{self.amount} stocks of {self.stockcode} owned by {self.username}"