from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now


# Create your models here.
class MenuOfTheDay(models.Model):

    menu_name = models.CharField(_('Food item name'),
                                 max_length=30,
                                 blank=True)
    meal_type = models.ForeignKey('MealType',
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

    class Meta:

        constraints = [
            models.UniqueConstraint(fields=['meal_type', 'days'],
                                    name='name of constraint')
        ]

    def __str__(self):

        return ' {}'.format(self.get_days_display())


class MealType(models.Model):

    MEAL_CHOICE = (
        ('B', 'breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner'),
    )

    meal_type = models.CharField(_('MEAL_CHOICE'),
                                 choices=MEAL_CHOICE,
                                 max_length=20,
                                 blank=True,
                                 null=True)

    meal_schedule = models.TimeField(blank=True, default=now)

    def __str__(self):

        return 'Mealtype: {}'.format(self.meal_type)


class PricePlan(models.Model):

    SUB_PLAN = (
        ('M', 'MONTHLY'),
        ('W', 'WEEKLY'),
        ('D', 'ONE TIME'),
    )

    subscription = models.CharField(_('subscription'),
                                    choices=SUB_PLAN,
                                    max_length=20,
                                    blank=True,
                                    null=True)

    price = models.IntegerField()
