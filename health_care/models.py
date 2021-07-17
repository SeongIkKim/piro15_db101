from django.db import models

class FitnessClub(models.Model):
    name = models.CharField(verbose_name="이름", max_length=50)
    address = models.CharField(verbose_name="주소", max_length=100, blank=True)
    fee = models.IntegerField(verbose_name="회비", blank=True)

    def __str__(self):
        return self.name

class Trainer(models.Model):
    club = models.ForeignKey(verbose_name="소속 헬스장", to='health_care.FitnessClub',
                             on_delete=models.SET_NULL, null=True)
    name = models.CharField(verbose_name="이름", max_length=50)
    phone_num = models.CharField(verbose_name="휴대폰번호", max_length=12)

    def __str__(self):
        return self.name

class Member(models.Model):
    club = models.ForeignKey(verbose_name="소속 헬스장", to='health_care.FitnessClub',
                             on_delete=models.CASCADE, related_name='member')
    trainer = models.ForeignKey(verbose_name="전담 트레이너", to='health_care.Trainer',
                                on_delete=models.SET_NULL, null=True, related_name='trainee')
    name = models.CharField(verbose_name="이름", max_length=50)
    phone_num = models.CharField(verbose_name="휴대폰번호", max_length=12)
    expiry_date = models.DateField(verbose_name="만료일")

    def __str__(self):
        return self.name

class PersonalTrain(models.Model):
    trainer = models.ForeignKey(verbose_name="트레이너", to='health_care.Trainer',
                                on_delete=models.CASCADE, related_name='PT')
    trainee = models.ForeignKey(verbose_name="PT회원", to='health_care.Member',
                                on_delete=models.CASCADE, unique=True, related_name='PT') # SAME WITH ONE-TO-ONE FIELD
    remain = models.IntegerField(verbose_name="남은 PT 횟수")

    def __str__(self):
        return f'{self.trainer} - {self.trainee} / {self.remain}'

class Locker(models.Model):
    number = models.IntegerField(verbose_name="라커룸 번호", primary_key=True)
    owner = models.OneToOneField(verbose_name="라커룸 주인", to='health_care.Member',
                                 on_delete=models.SET_NULL, null=True, related_name='locker')

    def __str__(self):
        return self.number

class Equipment(models.Model):
    name = models.CharField(verbose_name="기구 이름", max_length=50)
    user = models.ManyToManyField(verbose_name="사용자", to='health_care.Member',
                                  through='health_care.Use', related_name='used_equipment')
    # If 'through' argument is not taken, django will make default bridge table for Member - Equipment.

    def __str__(self):
        return self.name

class Use(models.Model):
    equipment = models.ForeignKey(verbose_name="사용 기구", to='health_care.Equipment', on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name="사용자", to='health_care.Member', on_delete=models.CASCADE)
    used_at = models.DateTimeField(verbose_name="사용 일시", auto_now_add=True)

    def __str__(self):
        return f'{self.equipment} - {self.user} : {self.used_at}'
