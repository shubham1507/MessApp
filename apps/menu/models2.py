from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime


# Create your models here.
class Weeklymenubyvendor(models.Model):
    #Menuitem - (idli,poha,upma),(dal-rice, chapati-bhaji),(dahi-paratha)
    #Menutype - Brakfast, lunch, dinner
    menuitem_id = models.ForeignKey(
        'Menuitem',
        on_delete=models.CASCADE,
    )
    menutype_id = models.ForeignKey(
        'Menutype',
        on_delete=models.CASCADE,
    )

    # day  #day_id ubiquetogether

    # day = models.ForeignKey(Day)

    date = models.DateField(default=datetime.now, blank=True)

    class Meta:

        unique_together = ('menuitem_id', 'menutype_id', 'date')



class Menuitem(models.Model):  #menuitem

    name = models.CharField(_('Food item name'), max_length=30, blank=True)


class Menutype(models.Model):

    MENU_CHOICE = (
        ('B', 'breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner'),
    )

    menu_type = models.CharField(_('Meal type'),
                                 choices=MENU_CHOICE,
                                 max_length=20,
                                 blank=True,
                                 null=True)

    price = models.IntegerField()

    # def _str_(self):

    #     return self.menu_type


# class weeklyfoodmenuhistory(models.Model):

#     Weeklymenubyvendor = models.ManyToManyField('Weeklymenubyvendor')
#     from_date = models.DateField(_("start Date"), default=datetime.date.today)

#     # to_date = models.DateField(_("end Date"), default=datetime.date.today)

#     Meta:
#             {
#         "date": {
#         "B":"",
#         "L":"",
#         "D":""
#                 }
#             }
# # postgress JSON
