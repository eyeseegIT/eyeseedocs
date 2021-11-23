# Generated by Django 3.2.7 on 2021-11-23 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20211123_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='AntsegPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250)),
                ('antseg', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.antseg')),
            ],
        ),
        migrations.CreateModel(
            name='PostsegPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250)),
                ('postseg', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.postseg')),
            ],
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]