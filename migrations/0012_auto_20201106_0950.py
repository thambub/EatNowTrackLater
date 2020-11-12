# Generated by Django 3.0.8 on 2020-11-06 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20201105_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='servings_dairy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='servings_fruit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='servings_grains',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='servings_meat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='servings_vegetables',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post_connected',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='preference',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
