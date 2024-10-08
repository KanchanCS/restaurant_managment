# Generated by Django 4.2.4 on 2024-09-17 09:36

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Chef",
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
                ("name", models.CharField(max_length=100)),
                ("biography", models.TextField(blank=True)),
                ("image", models.ImageField(upload_to="chef_images/")),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=200)),
                ("message", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="MenuItem",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("breakfast", "Breakfast"),
                            ("lunch", "Lunch"),
                            ("dinner", "Dinner"),
                        ],
                        max_length=20,
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
                ("image", models.ImageField(upload_to="menu_images/")),
            ],
        ),
    ]
