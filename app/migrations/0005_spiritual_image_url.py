# Generated by Django 5.0.1 on 2024-03-09 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_spiritual'),
    ]

    operations = [
        migrations.AddField(
            model_name='spiritual',
            name='image_url',
            field=models.URLField(default=0),
        ),
    ]