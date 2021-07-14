from django.db import models

class FitnessClub(models.Model):
    name = models.CharField(verbose_name="이름", max_length=50)
    address = models.CharField(verbose_name="주소", max_length=100, blank=True)
    fee = models.IntegerField(verbose_name="회비", blank=True)

    def __str__(self):
        return self.name
