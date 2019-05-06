from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('video_converter.urls', 'video_converter'),
                     namespace='video_converter'))
]
