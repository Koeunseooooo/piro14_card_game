# Generated by Django 2.2.17 on 2021-01-18 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_auto_20210118_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardbattle',
            name='from_user_card_num',
            field=models.IntegerField(blank=True, choices=[(5, 5), (6, 6), (4, 4), (2, 2), (3, 3)], null=True),
        ),
        migrations.AlterField(
            model_name='cardbattle',
            name='to_user_card_num',
            field=models.IntegerField(blank=True, choices=[(5, 5), (6, 6), (4, 4), (2, 2), (3, 3)], null=True),
        ),
    ]