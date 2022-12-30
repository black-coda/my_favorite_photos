from django.db import models


def category_dir_file(instance, image_file, *args, **kwargs):
    return "category_{0}/{1}".format(instance.category, image_file)


class Category(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name


class Wallpaper(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to=category_dir_file, max_length=70,)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
