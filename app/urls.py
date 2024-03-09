# myapp/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import PlaceListCreateView, PlaceRetrieveUpdateDestroyView,VideoUploadAPIView,TeacherApiView,SpiritualApiView,NatureApiView,CulturalApiView,AdventureApiView,WildLifeApiView,PopularDestinationApiView

urlpatterns = [
    path('upload-video/', VideoUploadAPIView.as_view(), name='upload_video'),

    path('upload-video/<int:pk>/', VideoUploadAPIView.as_view(), name='video-update'),

    path('teacher/', TeacherApiView.as_view(), name= 'teacher'),

    path('place/', PlaceListCreateView.as_view(), name='place-list-create'),

    path('place/<int:pk>/', PlaceRetrieveUpdateDestroyView.as_view(), name='place-retrieve-update-destroy'),

    path('spiritual/', SpiritualApiView.as_view(), name= 'spiritual'),

    path('nature/', NatureApiView.as_view(), name='nature'),

    path('adventure/', AdventureApiView.as_view(), name='adventure'),

    path('wildlife/', WildLifeApiView.as_view(), name='wildlife'),

    path('cultural/', CulturalApiView.as_view(), name='cultural'),

    path('populardestination/', PopularDestinationApiView.as_view(), name='populardestination')

    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
