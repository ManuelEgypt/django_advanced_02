# Generated by Django 2.1.5 on 2019-09-01 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_auto_20190901_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]