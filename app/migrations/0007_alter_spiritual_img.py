# Generated by Django 5.0.1 on 2024-03-09 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_spiritual_image_url_alter_spiritual_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spiritual',
            name='img',
            field=models.ImageField(default='', upload_to='images/spiritual/'),
        ),
    ]