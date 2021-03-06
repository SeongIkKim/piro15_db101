# Generated by Django 3.1.5 on 2021-07-17 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health_care', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
                ('phone_num', models.CharField(max_length=12, verbose_name='휴대폰번호')),
                ('expiry_date', models.DateField(verbose_name='만료일')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member', to='health_care.fitnessclub', verbose_name='소속 헬스장')),
                ('trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trainee', to='health_care.trainer', verbose_name='전담 트레이너')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalTrain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remain', models.IntegerField(verbose_name='남은 PT 횟수')),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PT', to='health_care.member', unique=True, verbose_name='PT회원')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PT', to='health_care.trainer', verbose_name='트레이너')),
            ],
        ),
    ]
