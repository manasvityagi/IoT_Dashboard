# Generated by Django 3.0.6 on 2020-05-28 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20200527_1326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='things',
            old_name='image_path',
            new_name='image',
        ),
    ]
