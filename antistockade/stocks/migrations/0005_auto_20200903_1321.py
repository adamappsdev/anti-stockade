# Generated by Django 3.1 on 2020-09-03 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_auto_20200903_1309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='user',
        ),
    ]
