# Generated by Django 3.0.6 on 2020-05-27 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_remove_things_field27'),
    ]

    operations = [
        migrations.AlterField(
            model_name='things',
            name='image_path',
            field=models.ImageField(upload_to=''),
        ),
    ]
