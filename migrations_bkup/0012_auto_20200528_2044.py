# Generated by Django 3.0.6 on 2020-05-28 08:44

import dashboard.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20200528_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(default='38 Windsor', max_length=150),
        ),
        migrations.AlterField(
            model_name='home',
            name='address',
            field=models.ForeignKey(default=dashboard.models.Address(), on_delete=django.db.models.deletion.CASCADE, to='dashboard.Address'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.Address'),
        ),
        migrations.AlterField(
            model_name='things',
            name='mfg',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.Manufacturer'),
        ),
    ]
