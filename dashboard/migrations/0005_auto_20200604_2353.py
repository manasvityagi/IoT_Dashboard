# Generated by Django 3.0.6 on 2020-06-04 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200604_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(default='38 Windsor Street', max_length=72),
        ),
    ]
