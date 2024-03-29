# Generated by Django 5.0.1 on 2024-03-16 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllMonth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image_url', models.URLField(blank=True)),
                ('image_file', models.ImageField(blank=True, null=True, upload_to='nature_images/')),
            ],
        ),
    ]
