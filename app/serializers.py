# myapp/serializers.py
from rest_framework import serializers
from app.models import Place,Video,Teacher,Spiritual,PopularDestination,Nature,WildLife,Cultural,Adventure,MostVisit,About,AllMonth
import cloudinary.uploader
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title','video_file', 'video_url']
    def update(self, instance, validated_data):
        video_file = validated_data.pop('video_file', None)
        if video_file:
            upload_result = cloudinary.uploader.upload(video_file, resource_type="video")
            instance.video_url = upload_result['secure_url']
        return super().update(instance, validated_data) 

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'role','image_file', 'image_url']

    def update(self, instance, validated_data):
        image_file = validated_data.pop('image_file', None)
        if image_file:
            upload_result = cloudinary.uploader.upload(image_file, resource_type="image")
            instance.image_url = upload_result['secure_url']
        return super().update(instance, validated_data) 

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'img', 'description')

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'title','description']



class AdventureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adventure
        fields = ['id', 'name', 'city_name', 'state_name', 'image_url', 'image_file']

    def update(self, instance, validated_data):
        image_file = validated_data.pop('image_file', None)
        if image_file:
            upload_result = cloudinary.uploader.upload(image_file, resource_type="image")
            instance.image_url = upload_result['secure_url']
        return super().update(instance, validated_data)  



class CulturalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultural
        fields = ['id', 'name', 'city_name', 'state_name', 'image_url', 'image_file']

    def update(self, instance, validated_data):
        image_file = validated_data.pop('image_file', None)
        if image_file:
            upload_result = cloudinary.uploader.upload(image_file, resource_type="image")
            instance.image_url = upload_result['secure_url']
        return super().update(instance, validated_data)  



class WildLifeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WildLife
        fields = ['id', 'name', 'city_name', 'state_name', 'image_url', 'image_file']

    def update(self, instance, validated_data):
        image_file = validated_data.pop('image_file', None)
        if image_file:
            upload_result = cloudinary.uploader.upload(image_file, resource_type="image")
            instance.image_url = upload_result['secure_url']
        return super().update(instance, validated_data)  


class AllMonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllMonth
        fields = ['id', 'name','image_url', 'image_file']

    def update(self, instance, validated_data):
        image_file = validated_data.pop('image_file', None)
        if image_file:
            upload_result = cloudinary.uploader.upload(image_file, resource_type="image")
            instance.image_url = upload_result['secure_url']
        return super().update(instance, validated_data)  



class NatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nature
        fields = ['id', 'name', 'city_name', 'state_name', 'image_url', 'image_file']

    def update(self, instance, validated_data):
        image_file = validated_data.pop('image_file', None)
        if image_file:
            upload_result = cloudinary.uploader.upload(image_file, resource_type="image")
            instance.image_url = upload_result['secure_url']
        return super().update(instance, validated_data)  


class MostVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MostVisit
        fields = ['id', 'name', 'city_name', 'state_name', 'image_url', 'image_file']

    def update(self, instance, validated_data):
        image_file = validated_data.pop('image_file', None)
        if image_file:
            upload_result = cloudinary.uploader.upload(image_file, resource_type="image")
            instance.image_url = upload_result['secure_url']
        return super().update(instance, validated_data)  




class PopularDestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularDestination
        fields = ['id', 'name', 'city_name', 'state_name', 'image_url', 'image_file']

    def update(self, instance, validated_data):
        image_file = validated_data.pop('image_file', None)
        if image_file:
            upload_result = cloudinary.uploader.upload(image_file, resource_type="image")
            instance.image_url = upload_result['secure_url']
        return super().update(instance, validated_data)  



class SpiritualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spiritual
        fields = ['id', 'name', 'city_name', 'state_name', 'image_url', 'image_file']

    def update(self, instance, validated_data):
        image_file = validated_data.pop('image_file', None)
        if image_file:
            upload_result = cloudinary.uploader.upload(image_file, resource_type="image")
            instance.image_url = upload_result['secure_url']
        return super().update(instance, validated_data)        