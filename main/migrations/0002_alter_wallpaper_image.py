# Generated by Django 4.1.4 on 2022-12-30 08:19

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wallpaper",
            name="image",
            field=models.ImageField(
                max_length=70, null=True, upload_to=main.models.category_dir_file
            ),
        ),
    ]