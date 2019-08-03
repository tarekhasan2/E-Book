
from django.contrib import admin
from django.urls import path

from . import views
app_name = "novels"

urlpatterns = [
    
	path('', views.novels, name = 'list'),
	path('<int:id>/details', views.novel_details, name = 'details'),
	path('create', views.novel_create, name = 'create'),
	path('<int:id>/update', views.novel_update, name = 'update'),
	path('<int:id>/delete', views.novel_delete, name = 'delete'),
	path('<int:id>/unpublish', views.novel_unpublish, name = 'unpublish'),
	path('<int:id>/update_content', views.novel_update_and_content, name = 'update_content'),


]