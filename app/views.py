from django.shortcuts import render

# Create your views here.
# myapp/views.py
from rest_framework import generics
from .models import Place
from .serializers import PlaceSerializer
# views.py
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
import cloudinary.uploader
from .models import Video,Teacher,Spiritual,Adventure,Cultural,WildLife,PopularDestination,Nature,MostVisit,About,AllMonth
from .serializers import UserSerializer,VideoSerializer,TeacherSerializer,SpiritualSerializer,AdventureSerializer,CulturalSerializer,WildLifeSerializer,PopularDestinationSerializer,NatureSerializer,MostVisitSerializer,AboutSerializer,AllMonthSerializer

# from rest_framework.authtoken.models import Token
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.http import HttpResponse
import logging
def simple_response(request):
    message = "Hello, YaTrip user its a Backend Side PLease use a valid url"  # Your message here
    return HttpResponse(message)

class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)  


class SignInView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            return Response({'message': 'Authentication successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]  # Allow unauthenticated requests

    def post(self, request, *args, **kwargs):
        if 'sessionid' not in request.COOKIES:
            return Response({'error': 'No session cookie found'}, status=status.HTTP_400_BAD_REQUEST)
        
        if request.user.is_authenticated:
            logout(request)
            return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_400_BAD_REQUEST)




class VideoUploadAPIView(APIView):
    def post(self, request, format=None):
        try:
            video_file = request.FILES.get('video')
            if not video_file:
                return Response({'error': 'No video file provided'}, status=status.HTTP_400_BAD_REQUEST)
            
            upload_result = cloudinary.uploader.upload(video_file, resource_type="video")
            video_url = upload_result['secure_url']
            
            serializer = VideoSerializer(data={'title': request.data.get('title', ''), 'video_url': video_url})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, format=None):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def put(self, request, pk, format=None):
        try:
            instance = self.get_object(pk)
            serializer = VideoSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TeacherApiView(APIView):
    
    def post(self, request, format=None):
        try:
            image_file = request.FILES.get('image_file')
            if not image_file:
                return Response({'error': 'No image file provided'}, status=status.HTTP_400_BAD_REQUEST)
            
            upload_result = cloudinary.uploader.upload(image_file, resource_type="image")
            image_url = upload_result['secure_url']

            serializer = SpiritualSerializer(data={
                'name': request.data.get('name'),
                'role': request.data.get('role'),
                'image_url': image_url
            })

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk, format=None):
        try:
            instance = self.get_object(pk)
            serializer = TeacherSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, format=None):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class SpiritualApiView(APIView):
#     def post(self, request, format= None):
#         try:
#             image_file = request.FILES.get('image_file')
#             if not image_file:
#                 return Response({'error':'No image file are Provided'}, status= status.HTTP_400_BAD_REQUEST)
#             upload_result = cloudinary.uploader.upload(image_file, resource_type="image")
#             image_url = upload_result['secure_url']
#             print(image_url)
#             serializer = SpiritualSerializer(
#                 data={'name': request.data.get('name'),
#                       'city_name':request.data.get('city_name'),
#                       'state_name':request.data.get('state_name'),
#                     #   'img':request.data.get('image_file'), 
#                       'image_url': image_url
#                       })
#             # print(serializer.image_url)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SpiritualApiView(APIView):
    def post(self, request, format=None):
        try:
            image_file = request.FILES.get('image_file')
            if not image_file:
                return Response({'error': 'No image file provided'}, status=status.HTTP_400_BAD_REQUEST)
            
            upload_result = cloudinary.uploader.upload(image_file, resource_type="image")
            image_url = upload_result['secure_url']

            serializer = SpiritualSerializer(data={
                'name': request.data.get('name'),
                'city_name': request.data.get('city_name'),
                'state_name': request.data.get('state_name'),
                'image_url': image_url
            })

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, format=None):
        spiritual = Spiritual.objects.all()
        serializer = SpiritualSerializer(spiritual, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        try:
            instance = self.get_object(pk)
            serializer = SpiritualSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AdventureApiView(APIView):
    def post(self, request, format=None):
        try:
            image_file = request.FILES.get('image_file')
            if not image_file:
                return Response({'error': 'No image file provided'}, status=status.HTTP_400_BAD_REQUEST)
            
            upload_result = cloudinary.uploader.upload(image_file, resource_type="image")
            image_url = upload_result['secure_url']

            serializer = AdventureSerializer(data={
                'name': request.data.get('name'),
                'city_name': request.data.get('city_name'),
                'state_name': request.data.get('state_name'),
                'image_url': image_url
            })

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, format=None):
        adventure = Adventure.objects.all()
        serializer = AdventureSerializer(adventure, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, pk, format=None):
        try:
            instance = self.get_object(pk)
            serializer = AdventureSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CulturalApiView(APIView):
    def post(self, request, format=None):
        try:
            image_file = request.FILES.get('image_file')
            if not image_file:
                return Response({'error': 'No image file provided'}, status=status.HTTP_400_BAD_REQUEST)
            
            upload_result = cloudinary.uploader.upload(image_file, resource_type="image")
            image_url = upload_result['secure_url']

            serializer = CulturalSerializer(data={
                'name': request.data.get('name'),
                'city_name': request.data.get('city_name'),
                'state_name': request.data.get('state_name'),
                'image_url': image_url
            })

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, format=None):
        cultural = Cultural.objects.all()
        serializer = CulturalSerializer(cultural, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



    def put(self, request, pk, format=None):
        try:
            instance = self.get_object(pk)
            serializer = CulturalSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class WildLifeApiView(APIView):
    def post(self, request, format=None):
        try:
            image_file = request.FILES.get('image_file')
            if not image_file:
                return Response({'error': 'No image file provided'}, status=status.HTTP_400_BAD_REQUEST)
            
            upload_result = cloudinary.uploader.upload(image_file, resource_type="image")
            image_url = upload_result['secure_url']

            serializer = WildLifeSerializer(data={
                'name': request.data.get('name'),
                'city_name': request.data.get('city_name'),
                'state_name': request.data.get('state_name'),
                'image_url': image_url
            })

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, format=None):
        wildlife = WildLife.objects.all()
        serializer = WildLifeSerializer(wildlife, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



    def put(self, request, pk, format=None):
        try:
            instance = self.get_object(pk)
            serializer = WildLifeSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PopularDestinationApiView(APIView):
    def post(self, request, format=None):
        try:
            image_file = request.FILES.get('image_file')
            if not image_file:
                return Response({'error': 'No image file provided'}, status=status.HTTP_400_BAD_REQUEST)
            
            upload_result = cloudinary.uploader.upload(image_file, resource_type="image")
            image_url = upload_result['secure_url']

            serializer = PopularDestinationSerializer(data={
                'name': request.data.get('name'),
                'city_name': request.data.get('city_name'),
                'state_name': request.data.get('state_name'),
                'image_url': image_url
            })

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, format=None):
        adventure = PopularDestination.objects.all()
        serializer = PopularDestinationSerializer(adventure, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        try:
            instance = self.get_object(pk)
            serializer = PopularDestinationSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class NatureApiView(APIView):
    def post(self, request, format=None):
        try:
            image_file = request.FILES.get('image_file')
            if not image_file:
                return Response({'error': 'No image file provided'}, status=status.HTTP_400_BAD_REQUEST)
            
            upload_result = cloudinary.uploader.upload(image_file, resource_type="image")
            image_url = upload_result['secure_url']

            serializer = NatureSerializer(data={
                'name': request.data.get('name'),
                'city_name': request.data.get('city_name'),
                'state_name': request.data.get('state_name'),
                'image_url': image_url
            })

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self,rerquest,format=None):
        nature = Nature.objects.all()
        serializer = NatureSerializer(nature, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        try:
            instance = self.get_object(pk)
            serializer = NatureSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MostVisitApiView(APIView):
    def post(self, request, format=None):
        try:
            image_file = request.FILES.get('image_file')
            if not image_file:
                return Response({'error': 'No image file provided'}, status=status.HTTP_400_BAD_REQUEST)
            
            upload_result = cloudinary.uploader.upload(image_file, resource_type="image")
            image_url = upload_result['secure_url']

            serializer = MostVisitSerializer(data={
                'name': request.data.get('name'),
                'city_name': request.data.get('city_name'),
                'state_name': request.data.get('state_name'),
                'image_url': image_url
            })

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self,rerquest,format=None):
        nature = MostVisit.objects.all()
        serializer = MostVisitSerializer(nature, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        try:
            instance = self.get_object(pk)
            serializer = MostVisitSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AboutCreateView(generics.ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class AboutRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class AllMonthApiView(APIView):
    def post(self, request, format=None):
        try:
            image_file = request.FILES.get('image_file')
            if not image_file:
                return Response({'error': 'No image file provided'}, status=status.HTTP_400_BAD_REQUEST)
            
            upload_result = cloudinary.uploader.upload(image_file, resource_type="image")
            image_url = upload_result['secure_url']

            serializer = AllMonthSerializer(data={
                'name': request.data.get('name'),
                'image_url': image_url
            })

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self,rerquest,format=None):
        nature = AllMonth.objects.all()
        serializer = AllMonthSerializer(nature, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        try:
            instance = self.get_object(pk)
            serializer = AllMonthSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PlaceListCreateView(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PlaceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

