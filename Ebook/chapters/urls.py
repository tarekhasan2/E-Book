
from django.contrib import admin
from django.urls import path

from . import views
app_name = "chapters"

urlpatterns = [

	path('<int:id>/chapter', views.chapter_details, name = 'details'),
	path('<int:id>/chapter_create', views.chapter_create, name = 'create'),
	path('<int:id>/chapter_update', views.chapter_update, name = 'update'),
	path('<int:id>/chapter_delete', views.chapter_delete, name = 'delete'),

]
