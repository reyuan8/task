from django.db import models
from datetime import datetime, date


class CreditProgramm(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    min_amount = models.PositiveIntegerField('Минимальная сумма')
    max_amount = models.PositiveIntegerField('Максимальная сумма')
    min_age = models.PositiveIntegerField('Минимальный возраст')
    max_age = models.PositiveIntegerField('Максимальный возраст')

    class Meta:
        verbose_name = 'Кредитная программа'
        verbose_name_plural = 'Кредитные программы'

    def __str__(self):
        return f"Программа: {self.name}"


class Borrower(models.Model):
    iin = models.CharField(max_length=12)
    birth_date = models.DateField()

    @property
    def age(self):
        try:
            return int((datetime.now().date() - self.birth_date).days / 365.25)
        except:
            return

    class Meta:
        verbose_name = 'Заёмщик'
        verbose_name_plural = 'Заёмщики'


class Request(models.Model):
    programm = models.ForeignKey(
        to='CreditProgramm',
        related_name='requests',
        on_delete=models.CASCADE
    )
    borrower = models.ForeignKey(
        to='Borrower',
        related_name='requests',
        on_delete=models.CASCADE
    )
    amount = models.PositiveIntegerField('Сумма')

    ACCEPTED, DECLINED = 1, 2
    STATUS_TYPES = (
        (ACCEPTED, 'Accepted'),
        (DECLINED, 'Declined')
    )
    status = models.PositiveSmallIntegerField(choices=STATUS_TYPES)

    rejection_reason = models.TextField(
        max_length=100,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class BlockedTarget(models.Model):
    iin = models.CharField(max_length=12)

    class Meta:
        verbose_name = 'Заблокированный'
        verbose_name_plural = 'Заблокированные'
