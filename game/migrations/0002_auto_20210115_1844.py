# Generated by Django 2.2.17 on 2021-01-15 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardBattle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_user_card_num', models.CharField(blank=True, choices=[('가위', '가위'), ('바위', '바위'), ('보', '보')], max_length=255, null=True)),
                ('from_user_card_num', models.CharField(blank=True, choices=[('가위', '가위'), ('바위', '바위'), ('보', '보')], max_length=255, null=True)),
                ('result', models.CharField(blank=True, max_length=255, null=True)),
                ('to_user_result', models.CharField(blank=True, max_length=255, null=True)),
                ('from_user_result', models.CharField(blank=True, max_length=255, null=True)),
                ('to_user_point', models.PositiveIntegerField(default=0)),
                ('from_user_point', models.PositiveIntegerField(default=0)),
                ('to_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Game',
        ),
    ]
