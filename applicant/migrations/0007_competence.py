# Generated by Django 3.2.5 on 2022-11-30 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0006_delete_compform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C1', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3)], max_length=1)),
                ('C2', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3)], max_length=1)),
                ('C3', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3)], max_length=1)),
                ('C4', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3)], max_length=1)),
                ('C5', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3)], max_length=1)),
                ('C6', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3)], max_length=1)),
                ('C7', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3)], max_length=1)),
                ('C8', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3)], max_length=1)),
                ('C9', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3)], max_length=1)),
                ('C10', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3)], max_length=1)),
                ('C11', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3)], max_length=1)),
                ('C12', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3)], max_length=1)),
                ('C13', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3)], max_length=1)),
                ('C14', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3)], max_length=1)),
                ('C15', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3)], max_length=1)),
                ('C16', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3)], max_length=1)),
                ('C17', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3)], max_length=1)),
                ('C18', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3)], max_length=1)),
            ],
        ),
    ]
