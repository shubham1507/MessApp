from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

# Create your models here.
# class MenuOfTheDay(models.Model):

#     menu_name = models.CharField(_('Food item name'),
#                                  max_length=30,
#                                  blank=True)

#     DAYS_OF_WEEK = (
#         (1, 'Monday'),
#         (2, 'Tuesday'),
#         (3, 'Wednesday'),
#         (4, 'Thursday'),
#         (5, 'Friday'),
#         (6, 'Saturday'),
#         (7, 'Sunday'),
#     )

#     meal_type = models.ForeignKey('MealType',
#                                   on_delete=models.CASCADE,
#                                   blank=True,
#                                   null=True)

#     days = models.PositiveIntegerField(choices=DAYS_OF_WEEK,
#                                        blank=True,
#                                        null=True)

#     class Meta:

#         constraints = [
#             models.UniqueConstraint(fields=['meal_type', 'days'],
#                                     name='name of constraint')
#         ]

#     def __str__(self):

#         return ' {}'.format(self.get_days_display())


class MenuOfTheDay(models.Model):

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
                                       primary_key=True,
                                       default=7)
    # days_in_week = models.CharField(max_length=100,
    #                                 default='Monday',
    #                                 choices=DAYS_OF_WEEK)

    breakfast_item = models.CharField(max_length=20, blank=True, null=True)
    lunch_item = models.CharField(max_length=20, blank=True, null=True)
    dinner_item = models.CharField(max_length=20, blank=True, null=True)

    class Meta:

        constraints = [
            models.UniqueConstraint(
                fields=['breakfast_item', 'lunch_item', 'dinner_item', 'days'],
                name='name of con')
        ]

    def __str__(self):

        return ' {}'.format(self.get_days_display())


# class ServiceAndSubscription(models.Model):

#     SUB_PLAN = (
#         ('M', 'MONTHLY'),
#         ('W', 'WEEKLY'),
#         ('D', 'ONE TIME'),
#     )
#     MEAL_CHOICE = (
#         ('B', 'breakfast'),
#         ('L', 'Lunch'),
#         ('D', 'Dinner'),
#     )

#     service = models.CharField(
#         choices=MEAL_CHOICE,
#         blank=True,
#         null=True,
#         max_length=20,
#     )
#     subscription_type = models.CharField('SUB_PLAN',
#                                          choices=SUB_PLAN,
#                                          max_length=20,
#                                          blank=True,
#                                          null=True)

#     meal_schedule = models.TimeField(blank=True, default=now)
#     price = models.IntegerField(default=1)


class ServiceAndSubscription(models.Model):

    SUB_PLAN = (
        ('M', 'MONTHLY'),
        ('W', 'WEEKLY'),
        ('D', 'ONE TIME'),
    )
    subscription_type = models.CharField('SUB_PLAN',
                                         choices=SUB_PLAN,
                                         max_length=20,
                                         default='MONTHLY')
    breakfast_price = models.IntegerField(default=1)
    lunch_price = models.IntegerField(default=1)
    dinner_price = models.IntegerField(default=1)

    def __str__(self):
        return ' {}'.format(self.get_subscription_type_display())


class Mealschedule(models.Model):

    MEAL_CHOICE = (
        ('B', 'breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner'),
    )
    meal_type = models.CharField(
        choices=MEAL_CHOICE,
        blank=True,
        null=True,
        max_length=20,
    )
    meal_schedule = models.TimeField(blank=True, default=now)


# class MealType(models.Model):

#     MEAL_CHOICE = (
#         ('B', 'breakfast'),
#         ('L', 'Lunch'),
#         ('D', 'Dinner'),
#     )

#     meal_type = models.CharField(_('MEAL_CHOICE'),
#                                  choices=MEAL_CHOICE,
#                                  max_length=20,
#                                  blank=True,
#                                  null=True)

#     def __str__(self):

#         return 'Mealtype: {}'.format(self.meal_type)

# class ServiceAndSubscription(models.Model): id, day,lunch, dinner ,break, menu_name
#     SUB_PLAN = (
#         ('M', 'MONTHLY'),
#         ('W', 'WEEKLY'),
#         ('D', 'ONE TIME'),
#     )
#id, day,lunch, dinner ,break, menu_name
#1  , mon ,idli,
#     _type = models.CharField(_('SUB_PLAN'),
#                              choices=SUB_PLAN,
#                              max_length=20,
#                              blank=True,
#                              null=True)

#     service = models.ForeignKey('MenuOfTheDay',
#                                 on_delete=models.CASCADE,
#                                 blank=True,
#                                 null=True)

#     subscription_type = models.CharField('_type',
#                                          choices=SUB_PLAN,
#                                          max_length=20,
#                                          blank=True,
#                                          null=True)

#     price = models.IntegerField(null=True)

#     meal_schedule = models.TimeField(blank=True, default=now)
