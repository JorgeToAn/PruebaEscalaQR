# Generated by Django 4.2 on 2023-04-07 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.IntegerField(choices=[(0, 'Male'), (1, 'Female')], default=0),
        ),
    ]
