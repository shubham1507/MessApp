from django.db import models

# Create your models here.

SERVICE = (('BREAKFAST', 'breakfast'), ('LUNCH', 'lunch'),
           ('DINNER', 'dinner'), ('FULL_MEAL', 'full_meal'))


class ServiceAndSubscription(models.Model):

    offered_services = models.CharField(max_length=60,
                                        choices=SERVICE,
                                        default='BREAKFAST')

    one_time_subscription = models.IntegerField()

    weekly_subscription = models.IntegerField()

    monthly_subscription = models.IntegerField()

    class Meta:

        constraints = [
            models.UniqueConstraint(fields=['offered_services'],
                                    name='name of con')
        ]

    def __str__(self):
        return ' {}'.format(self.get_offered_services_display())
