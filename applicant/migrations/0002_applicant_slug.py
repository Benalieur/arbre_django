# Generated by Django 3.2.5 on 2022-11-25 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='slug',
            field=models.SlugField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
