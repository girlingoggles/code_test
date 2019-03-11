from django.db import models

class FilledQuestionnaire(models.Model):
 
    MONTH_CHOICES = (
        ('1', 'January'),
        ('2', 'February'),
        ('3', 'March'),
        ('4', 'April'),
        ('5', 'May'),
        ('6', 'June'),
        ('7', 'July'),
        ('8', 'August'),
        ('9', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),
    )

    DAY_CHOICES = (
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
        ('7', 'Sunday'),
    )
    month = models.CharField( 
        choices=MONTH_CHOICES,
        max_length=2,
        verbose_name='favourite month',
    )
    day = models.CharField( 
        choices=DAY_CHOICES,
        max_length=1,
        verbose_name='favourite day',
    )

