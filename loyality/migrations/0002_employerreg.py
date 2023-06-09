# Generated by Django 4.1.5 on 2023-03-29 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyality', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployerReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('firstName', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('stage', models.CharField(max_length=20)),
                ('chatID', models.IntegerField()),
                ('findUserByID', models.IntegerField()),
                ('role', models.IntegerField()),
                ('report', models.IntegerField()),
            ],
        ),
    ]
