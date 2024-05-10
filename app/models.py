from django.db import models
from django.contrib.auth.models import AbstractUser


import cloudinary.uploader

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.URLField()
    video_file = models.FileField(upload_to='video/', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the instance already exists (updating)
            original = Video.objects.get(pk=self.pk)
            if self.video_file and self.video_file != original.video_file:
                #video file has been changed, upload to Cloudinary and update video_url
                upload_result = cloudinary.uploader.upload(self.video_file, resource_type="video")
                self.video_url = upload_result['secure_url']
        else:  # If creating a new instance
            if self.video_file:
                upload_result = cloudinary.uploader.upload(self.video_file, resource_type="video")
                self.video_url = upload_result['secure_url']
        super().save(*args, **kwargs)


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image_url = models.URLField()
    image_file = models.ImageField(upload_to='teacher_images/', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the instance already exists (updating)
            original = Teacher.objects.get(pk=self.pk)
            if self.image_file and self.image_file != original.image_file:
                # Image file has been changed, upload to Cloudinary and update image_url
                upload_result = cloudinary.uploader.upload(self.image_file, resource_type="image")
                self.image_url = upload_result['secure_url']
        else:  # If creating a new instance
            if self.image_file:
                upload_result = cloudinary.uploader.upload(self.image_file, resource_type="image")
                self.image_url = upload_result['secure_url']
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.name
    
    

class Spiritual(models.Model):
    name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    state_name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True)
    image_file = models.ImageField(upload_to='spiritual_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:  # If the instance already exists (updating)
            original = Spiritual.objects.get(pk=self.pk)
            if self.image_file and self.image_file != original.image_file:
                # Image file has been changed, upload to Cloudinary and update image_url
                upload_result = cloudinary.uploader.upload(self.image_file, resource_type="image")
                self.image_url = upload_result['secure_url']
        else:  # If creating a new instance
            if self.image_file:
                upload_result = cloudinary.uploader.upload(self.image_file, resource_type="image")
                self.image_url = upload_result['secure_url']
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class PopularDestination(models.Model):
    name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    state_name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True)
    image_file = models.ImageField(upload_to='spiritual_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:  # If the instance already exists (updating)
            original = PopularDestination.objects.get(pk=self.pk)
            if self.image_file and self.image_file != original.image_file:
                # Image file has been changed, upload to Cloudinary and update image_url
                upload_result = cloudinary.uploader.upload(self.image_file, resource_type="image")
                self.image_url = upload_result['secure_url']
        else:  # If creating a new instance
            if self.image_file:
                upload_result = cloudinary.uploader.upload(self.image_file, resource_type="image")
                self.image_url = upload_result['secure_url']
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class AllMonth(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True)
    image_file = models.ImageField(upload_to='nature_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:  # If the instance already exists (updating)
            original = Nature.objects.get(pk=self.pk)
            if self.image_file and self.image_file != original.image_file:
                # Image file has been changed, upload to Cloudinary and update image_url
                upload_result = cloudinary.uploader.upload(self.image_file, resource_type="image")
                self.image_url = upload_result['secure_url']
        else:  # If creating a new instance
            if self.image_file:
                upload_result = cloudinary.uploader.upload(self.image_file, resource_type="image")
                self.image_url = upload_result['secure_url']
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Nature(models.Model):
    name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    state_name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True)
    image_file = models.ImageField(upload_to='nature_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:  # If the instance already exists (updating)
            original = Nature.objects.get(pk=self.pk)
            if self.image_file and self.image_file != original.image_file:
                # Image file has been changed, upload to Cloudinary and update image_url
                upload_result = cloudinary.uploader.upload(self.image_file, resource_type="image")
                self.image_url = upload_result['secure_url']
        else:  # If creating a new instance
            if self.image_file:
                upload_result = cloudinary.uploader.upload(self.image_file, resource_type="image")
                self.image_url = upload_result['secure_url']
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class MostVisit(models.Model):
    name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    state_name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True)
    image_file = models.ImageField(upload_to='nature_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:  # If the instance already exists (updating)
            original = MostVisit.objects.get(pk=self.pk)
            if self.image_file and self.image_file != original.image_file:
                # Image file has been changed, upload to Cloudinary and update image_url
                upload_result = cloudinary.uploader.upload(self.image_file, resource_type="image")
                self.image_url = upload_result['secure_url']
        else:  # If creating a new instance
            if self.image_file:
                upload_result = cloudinary.uploader.upload(self.image_file, resource_type="image")
                self.image_url = upload_result['secure_url']
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title




class WildLife(models.Model):
    name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    state_name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True)
    image_file = models.ImageField(upload_to='wildlife_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:  # If the instance already exists (updating)
            original = WildLife.objects.get(pk=self.pk)
            if self.image_file and self.image_file != original.image_file:
                # Image file has been changed, upload to Cloudinary and update image_url
                upload_result = cloudinary.uploader.upload(self.image_file, resource_type="image")
                self.image_url = upload_result['secure_url']
        else:  # If creating a new instance
            if self.image_file:
                upload_result = cloudinary.uploader.upload(self.image_file, resource_type="image")
                self.image_url = upload_result['secure_url']
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



class Cultural(models.Model):
    name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    state_name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True)
    image_file = models.ImageField(upload_to='cultural_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:  # If the instance already exists (updating)
            original = Cultural.objects.get(pk=self.pk)
            if self.image_file and self.image_file != original.image_file:
                # Image file has been changed, upload to Cloudinary and update image_url
                upload_result = cloudinary.uploader.upload(self.image_file, resource_type="image")
                self.image_url = upload_result['secure_url']
        else:  # If creating a new instance
            if self.image_file:
                upload_result = cloudinary.uploader.upload(self.image_file, resource_type="image")
                self.image_url = upload_result['secure_url']
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



class Adventure(models.Model):
    name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    state_name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True)
    image_file = models.ImageField(upload_to='adventure_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:  # If the instance already exists (updating)
            original = Adventure.objects.get(pk=self.pk)
            if self.image_file and self.image_file != original.image_file:
                # Image file has been changed, upload to Cloudinary and update image_url
                upload_result = cloudinary.uploader.upload(self.image_file, resource_type="image")
                self.image_url = upload_result['secure_url']
        else:  # If creating a new instance
            if self.image_file:
                upload_result = cloudinary.uploader.upload(self.image_file, resource_type="image")
                self.image_url = upload_result['secure_url']
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name