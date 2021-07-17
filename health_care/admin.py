from django.contrib import admin

# Register your models here.
from health_care.models import FitnessClub, Trainer, Member, PersonalTrain, Locker, Equipment, Use

for model in [FitnessClub, Trainer, Member, PersonalTrain, Locker, Equipment, Use]:
    admin.site.register(model)
