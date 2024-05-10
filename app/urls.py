# myapp/urls.py
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from app.views import SignInView,LogoutView,SignUpView,AboutCreateView,MostVisitApiView,PlaceListCreateView, PlaceRetrieveUpdateDestroyView,VideoUploadAPIView,TeacherApiView,SpiritualApiView,NatureApiView,CulturalApiView,AdventureApiView,WildLifeApiView,PopularDestinationApiView,AllMonthApiView
from . import views
# from .views import register, login_view, logout_view

admin.site.site_title = "Yatrip"
admin.site.site_header = "Yatrip Admin DashBoard"
admin.site.index_title = "Yatrip"


urlpatterns = [

    path('', views.simple_response, name='simple_response'),
    path('as', views.simple_response, name='simple_response'),

    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(), name='logout'),


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

    path('mostvisit/', MostVisitApiView.as_view(), name='mostvisit'),

    path('about/',AboutCreateView.as_view(),name='about'),

    path('populardestination/', PopularDestinationApiView.as_view(), name='populardestination'),

    path('allmonth/', AllMonthApiView.as_view(), name='allmonth' ),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
