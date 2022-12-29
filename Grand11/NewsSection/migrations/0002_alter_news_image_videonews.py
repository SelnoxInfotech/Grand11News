# Generated by Django 4.1.4 on 2022-12-29 06:00

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("NewsSection", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="Image",
            field=models.ImageField(default=None, upload_to="media/News"),
        ),
        migrations.CreateModel(
            name="VideoNews",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Title", models.CharField(default=None, max_length=100)),
                ("Description", ckeditor.fields.RichTextField()),
                ("Video", models.FileField(default=None, upload_to="media/News")),
                ("VideoUrl", models.URLField(blank=True, default=None)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "Category",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="NewsSection.category",
                    ),
                ),
                (
                    "SubCategory",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="NewsSection.subcategory",
                    ),
                ),
            ],
        ),
    ]