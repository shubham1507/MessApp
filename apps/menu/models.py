from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

# Create your models here.
# class Weeklymenubyvendor(models.Model):
#     #Menuitem - (idli,poha,upma),(dal-rice, chapati-bhaji),(dahi-paratha)
#     #Menutype - Brakfast, lunch, dinner

#     menuitem_id = models.ForeignKey(
#         'Menuitem',
#         on_delete=models.CASCADE,
#     )
#     menutype_id = models.ForeignKey(
#         'Menutype',
#         on_delete=models.CASCADE,
#     )

#     date = models.DateField(default=datetime.now, blank=True)

#     class Meta:

#         unique_together = ('menuitem_id', 'menutype_id', 'date')

# class Menuitem(models.Model):

#     name = models.CharField(_('Food item name'), max_length=30, blank=True)


class Menuoftheday(models.Model):

    menuitem_id = models.ForeignKey('Menuitem',
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True)

    mealtype_id = models.ForeignKey('Mealtype',
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True)

    DAYS_OF_WEEK = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )

    days = models.CharField(max_length=1,
                            choices=DAYS_OF_WEEK,
                            blank=True,
                            null=True)


class Menuitem(models.Model):  #menuitem

    name = models.CharField(_('Food item name'), max_length=30, blank=True)

    def __str__(self):

        return 'MyModel: {}'.format(self.name)


class Mealtype(models.Model):

    MEAL_CHOICE = (
        ('B', 'breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner'),
        ('B+L', 'Breakfast&Lunch'),
        ('B+L+D', 'Breakfast&Lunch&Dinner'),
    )

    PRICE_PLAN = (
        ('M', 'MONTHLY'),
        ('W', 'WEEKLY'),
        ('D', 'ONE TIME'),
    )

    meal_type = models.CharField(_('MEAL_CHOICE'),
                                 choices=MEAL_CHOICE,
                                 max_length=20,
                                 blank=True,
                                 null=True)

    price_plan = models.CharField(_('PRICE_PLAN'),
                                  choices=PRICE_PLAN,
                                  max_length=20,
                                  blank=True,
                                  null=True)
    price = models.IntegerField()
