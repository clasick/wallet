# Generated by Django 2.0.4 on 2018-04-10 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0011_auto_20180409_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ssn',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
