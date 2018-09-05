
from django.contrib import admin
from django.urls import path,include,re_path
from blog import views
urlpatterns = [
	re_path('index/(?P<nid>\d*)',views.Index.as_view()),
]
