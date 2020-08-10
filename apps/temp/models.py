from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now


# Create your models here.
class Menuoftheday(models.Model):

    # menuitem = models.ForeignKey('Menuitem',
    #                              on_delete=models.CASCADE,
    #                              blank=True,
    #                              null=True)
    name = models.CharField(_('Food item name'), max_length=30, blank=True)

    mealtype = models.ForeignKey('Mealtype',
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)

    DAYS_OF_WEEK = (
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday'),
    )

    days = models.PositiveIntegerField(choices=DAYS_OF_WEEK,
                                       blank=True,
                                       null=True)

    def __str__(self):

        return ' {}'.format(self.get_days_display())

    class Meta:
        unique_together = ('mealtype0,', 'days')
        # name    mealtype    days
        # idli        B           1


# class Menuitem(models.Model):
# def __str__(self):

#     return 'Menuitems: {}'.format(self.name)


class Mealtype(models.Model):

    MEAL_CHOICE = (
        ('B', 'breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner'),
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

    mealschedule = models.TimeField(blank=True, default=now)

    def __str__(self):

        return 'Mealtype: {}'.format(self.meal_type)
