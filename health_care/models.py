from django.db import models

class FitnessClub(models.Model):
    name = models.CharField(verbose_name="이름", max_length=50)
    address = models.CharField(verbose_name="주소", max_length=100, blank=True)
    fee = models.IntegerField(verbose_name="회비", blank=True)

    def __str__(self):
        return self.name

class Trainer(models.Model):
    club = models.ForeignKey(verbose_name="소속 헬스장", to='health_care.FitnessClub', on_delete=models.SET_NULL, null=True)
    name = models.CharField(verbose_name="이름", max_length=50)
    phone_num = models.CharField(verbose_name="휴대폰번호", max_length=12)



