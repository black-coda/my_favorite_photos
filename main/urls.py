from django.urls import path
from api import views


urlpatterns = [
    path('category-list/', views.CategoryListView.as_view()),
    # path('category-retrieve/<int:pk>/', views.WallpaperRetrieveView.as_view()),
    path('category-create/', views.CategoryCreateView.as_view()),

    #wallpaper
    path('wallpaper-list/', views.WallpaperListView.as_view()),
    path('wallpaper-retrieve/<int:pk>/', views.WallpaperRetrieveView.as_view()),
    path('wallpaper-create/', views.WallpaperCreateView.as_view()),
]
