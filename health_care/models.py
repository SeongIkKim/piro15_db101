from django.db import models

class FitnessClub(models.Model):
    name = models.CharField(verbose_name="이름", max_length=50)
    address = models.CharField(verbose_name="주소", max_length=100, blank=True)
    fee = models.IntegerField(verbose_name="회비", blank=True)

    def __str__(self):
        return self.name

class Trainer(models.Model):
    club = models.OneToOneField(verbose_name="소속 헬스장", to='health_care.FitnessClub',
                             on_delete=models.SET_NULL, null=True)
    name = models.CharField(verbose_name="이름", max_length=50)
    phone_num = models.CharField(verbose_name="휴대폰번호", max_length=12)

class Member(models.Model):
    club = models.OneToOneField(verbose_name="소속 헬스장", to='health_care.FitnessClub',
                             on_delete=models.CASCADE, related_name='member')
    trainer = models.ForeignKey(verbose_name="전담 트레이너", to='health_care.Trainer',
                                on_delete=models.SET_NULL, null=True, related_name='trainee')
    name = models.CharField(verbose_name="이름", max_length=50)
    phone_num = models.CharField(verbose_name="휴대폰번호", max_length=12)
    expiry_date = models.DateField(verbose_name="만료일")

class PersonalTrain(models.Model):
    trainer = models.ForeignKey(verbose_name="트레이너", to='health_care.Trainer',
                                on_delete=models.CASCADE, related_name='PT')
    trainee = models.ForeignKey(verbose_name="PT회원", to='health_care.Member',
                                on_delete=models.CASCADE, unique=True, related_name='PT') # SAME WITH ONE-TO-ONE FIELD
    remain = models.DateField(verbose_name="남은 PT 횟수")
