# Generated by Django 3.0.6 on 2020-05-30 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerprofile',
            name='image',
            field=models.ImageField(default='owner_pics/default.jpg', upload_to='owner_pics'),
        ),
    ]