# Generated by Django 4.0.4 on 2022-08-13 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]