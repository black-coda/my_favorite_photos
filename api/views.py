from rest_framework import viewsets
from api.serializers import CategorySerializer, WallpaperSerializer
from rest_framework import generics
from main.models import Category, Wallpaper
from rest_framework.permissions import AllowAny, IsAdminUser
from drf_yasg.utils import swagger_auto_schema



class WallpaperListView(generics.ListAPIView):
    queryset = Wallpaper.objects.all()
    serializer_class = WallpaperSerializer
    permission_classes = [AllowAny]


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class WallpaperRetrieveView(generics.RetrieveAPIView):
    queryset = Wallpaper.objects.all()
    serializer_class = WallpaperSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'


class WallpaperCreateView(generics.CreateAPIView):
    queryset = Wallpaper.objects.all()
    serializer_class = WallpaperSerializer
    permission_classes = [IsAdminUser]


    def perform_create(self, serializer):
        category = serializer.validated_data.get("category")
        print(f"this is {category}")
        return super().perform_create(serializer)


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


    def perform_create(self, serializer):
        # serializer.save(user=self.)
        return super().perform_create(serializer)





class WallpaperUpdateView(generics.UpdateAPIView):
    queryset = Wallpaper.objects.all()
    serializer_class = WallpaperSerializer
    permission_classes = [IsAdminUser]


class WallpaperDestroyView(generics.DestroyAPIView):
    queryset = Wallpaper.objects.all()
    serializer_class = WallpaperSerializer
    permission_classes = [IsAdminUser]
