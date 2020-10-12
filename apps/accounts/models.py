from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from address.models import AddressField
from phone_field import PhoneField
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=10)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    address_line_1 = models.TextField(blank=True, null=True)
    address_line_2 = models.TextField(blank=True, null=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    is_seller = models.BooleanField(_('is seller'), default=False)
    image = ProcessedImageField(upload_to='BackgroundImages/',
                                processors=[ResizeToFill(550, 550)],
                                format='JPEG',
                                options={'quality': 60},
                                blank=True,
                                null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
    ]

    def __str__(self):
        return "{}".format(self.email)


class Vendor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='vendor')
    mess_center_name = models.CharField(_('Mess Name'),
                                        max_length=300,
                                        blank=True)
    FOOD_CHOICES = (('V', 'veg'), ('N', 'non-veg'), ('M', 'mix'))
    deliverylt = models.CharField(_('Region of delivery'),
                                  max_length=20,
                                  blank=True,
                                  null=True)
    foodserved = models.CharField(_('Food served'),
                                  choices=FOOD_CHOICES,
                                  max_length=20,
                                  blank=True,
                                  null=True)


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='customer')
    birth_date = models.DateField(_("Date"), blank=True, null=True)
    preference = models.CharField(max_length=30, blank=True,
                                  null=True)  #veg, non-veg, mix
