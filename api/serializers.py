from rest_framework import serializers

from main.models import Category, Wallpaper


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class WallpaperSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field="name",
    )

    class Meta:
        model = Wallpaper
        fields = [
            "id",
            "name",
            "image",
            "created",
            "updated",
            "category",
        ]
        depth = 1
