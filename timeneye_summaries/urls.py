"""timeneye_summaries URL Configuration
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('timeneye/', include('summaries.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
