# Generated by Django 3.1 on 2020-09-03 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_auto_20200903_1253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='owner',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='user',
            new_name='username',
        ),
    ]
