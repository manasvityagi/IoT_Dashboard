# Generated by Django 3.0.6 on 2020-06-02 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200603_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valuestream',
            name='description',
            field=models.CharField(default='value stream description', max_length=120),
        ),
    ]
