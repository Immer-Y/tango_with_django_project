# Generated by Django 2.1.5 on 2022-02-23 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_pageadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
