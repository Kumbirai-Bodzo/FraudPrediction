
from django.db import models

class Reports(models.Model):
    id = models.AutoField(primary_key=True)
    batch_no = models.PositiveIntegerField()
    transaction_id = models.CharField(max_length=255)
    probability_fradulent = models.DecimalField(max_digits=10,decimal_places=5)
    date_created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        auto_created=True,
    )

    class Meta:
        verbose_name_plural = 'Reports'
        verbose_name = 'Report'

    def __str__(self) -> str:
        return '{}-{}'.format(self.batch_no,self.transaction_id)