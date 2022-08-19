# Generated by Django 4.0.4 on 2022-08-19 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0014_post_like_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'verbose_name_plural': 'DateTime',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='date_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='board.datecategory'),
        ),
    ]