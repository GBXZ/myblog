
from django.contrib import admin
from django.urls import path,include
from blog import views
urlpatterns = [
	path('index/',views.Index.as_view())
]
