# Generated by Django 4.2.11 on 2024-08-24 01:34

from django.db import migrations, models
import django.utils.timezone
import emailscraper_app.models


class Migration(migrations.Migration):

    dependencies = [
        ("emailscraper_app", "0008_emailfileupload_body_rtf_3"),
    ]

    operations = [
        migrations.CreateModel(
            name="RecordingEmailSends",
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
                ("name", models.CharField(max_length=255)),
                ("campaign", models.CharField(max_length=255)),
                ("subject", models.CharField(max_length=255)),
                ("sender_email", models.EmailField(max_length=254)),
                ("message_body", models.TextField()),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(name="EmailOption",),
        migrations.AlterField(
            model_name="emailfileupload",
            name="file",
            field=models.FileField(upload_to=emailscraper_app.models.upload_to),
        ),
    ]
