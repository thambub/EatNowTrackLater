# Generated by Django 3.0.8 on 2020-11-10 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20201110_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_age',
            field=models.IntegerField(default=0),
        ),
    ]
