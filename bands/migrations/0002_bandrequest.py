# Generated by Django 5.0.4 on 2024-04-24 11:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bands", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BandRequest",
            fields=[
                ("request_id", models.AutoField
                 (primary_key=True, serialize=False)),
                ("motivation", models.CharField(max_length=255)),
                ("request_date", models.DateTimeField(auto_now_add=True)),
                ("slug", models.SlugField
                 (blank=True, max_length=255, unique=True)),
                (
                    "band",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bands.band"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["request_date"],
            },
        ),
    ]
