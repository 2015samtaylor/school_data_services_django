# Generated by Django 4.2.11 on 2024-04-05 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emailscraper_app", "0002_basiccsvingestion_delete_mymodel_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailFileUpload",
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
                ("email", models.CharField(max_length=150)),
                ("HighSchools", models.CharField(max_length=150)),
                ("file", models.FileField(upload_to="EmailFiles/files/")),
            ],
        ),
        migrations.DeleteModel(name="BasicCSVIngestion",),
    ]
