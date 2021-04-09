# Generated by Django 3.1.7 on 2021-04-09 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210409_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(choices=[('1', '1:00 AM'), ('2', '2:00 AM'), ('3', '3:00 AM'), ('4', '4:00 AM'), ('5', '5:00 AM'), ('6', '6:00 AM'), ('7', '7:00 AM'), ('8', '8:00 AM'), ('9', '9:00 AM'), ('10', '10:00 AM'), ('11', '11:00 AM'), ('12', '12:00 AM'), ('1', '1:00 PM'), ('2', '2:00 PM'), ('3', '3:00 PM'), ('4', '4:00 PM'), ('5', '5:00 PM'), ('6', '6:00 PM'), ('7', '7:00 PM'), ('8', '8:00 PM'), ('9', '9:00 PM'), ('10', '10:00 PM'), ('11', '11:00 PM'), ('12', '12:00 PM')], default='1', verbose_name='Event Time'),
        ),
    ]