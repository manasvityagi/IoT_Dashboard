# Generated by Django 3.0.6 on 2020-06-04 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_channel_rule'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Channel',
        ),
        migrations.DeleteModel(
            name='Rule',
        ),
    ]