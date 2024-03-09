# Generated by Django 5.0.1 on 2024-03-09 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spiritual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('img', models.ImageField(upload_to='images/spiritual/')),
                ('city_name', models.CharField(max_length=225)),
                ('state_name', models.CharField(max_length=225)),
            ],
        ),
    ]
