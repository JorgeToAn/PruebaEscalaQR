# Generated by Django 4.2 on 2023-04-18 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(default='default_pfp.jpg', null=True, upload_to=''),
        ),
    ]
