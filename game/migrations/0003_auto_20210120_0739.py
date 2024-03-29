# Generated by Django 2.2.17 on 2021-01-19 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20210118_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardbattle',
            name='from_user_card_num',
            field=models.IntegerField(blank=True, choices=[(2, 2), (4, 4), (3, 3), (1, 1), (8, 8)], null=True, verbose_name='도전장을 내밀 상대는?'),
        ),
        migrations.AlterField(
            model_name='cardbattle',
            name='to_user_card_num',
            field=models.IntegerField(blank=True, choices=[(2, 2), (4, 4), (3, 3), (1, 1), (8, 8)], null=True, verbose_name='내가 고른 카드'),
        ),
    ]
