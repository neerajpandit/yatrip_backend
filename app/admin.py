from django.contrib import admin

# Register your models here.
# myapp/admin.py
from django.contrib import admin
from app.models import Place,Teacher,Video,Spiritual,Cultural,Adventure,WildLife,Nature,PopularDestination,MostVisit,About,AllMonth

@admin.register(PopularDestination)
class PopularDestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city_name', 'state_name', 'image_url')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display=('title','description')

@admin.register(AllMonth)
class AllMonthAdmin(admin.ModelAdmin):
    list_display=('id','name','image_url')

@admin.register(Nature)
class NatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'city_name', 'state_name', 'image_url')

@admin.register(MostVisit)
class MostVisitAdmin(admin.ModelAdmin):
    list_display = ('name', 'city_name', 'state_name', 'image_url')


@admin.register(WildLife)
class WildLifeAdmin(admin.ModelAdmin):
    list_display = ('name', 'city_name', 'state_name', 'image_url')

@admin.register(Adventure)
class AdventureAdmin(admin.ModelAdmin):
    list_display = ('name', 'city_name', 'state_name', 'image_url')

@admin.register(Cultural)
class CulturalAdmin(admin.ModelAdmin):
    list_display = ('name', 'city_name', 'state_name', 'image_url')

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'img', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','role', 'image_url')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'video_url')
    search_fields = ('title', )
    list_filter = ('title',)

@admin.register(Spiritual)
class SpiritualAdmin(admin.ModelAdmin):
    list_display = ('name', 'city_name', 'state_name', 'image_url')
    # readonly_fields = ('image_url_display',)

    # def image_url_display(self, obj):
    #     return '<img src="{}" style="max-width:200px; max-height:200px;" />'.format(obj.image_url)
    
    # image_url_display.allow_tags = True
    # image_url_display.short_description = 'Image'

    # fieldsets = (
    #     (None, {
    #         'fields': ('name', 'city_name', 'state_name', 'image_url_display')
    #     }),
    #     ('Image', {
    #         'fields': ('image_file',),
    #     }),
    # )