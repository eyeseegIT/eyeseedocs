# Generated by Django 3.2.7 on 2021-11-23 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20211123_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='antseg',
            name='segment',
        ),
        migrations.RemoveField(
            model_name='postseg',
            name='segment',
        ),
    ]
