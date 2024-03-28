# Generated by Django 5.0.1 on 2024-02-14 10:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_lazyuserprofile_availability"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lazyuserprofile",
            name="availability",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 2, 14, 10, 21, 16, 521243, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Earliest Start Date",
            ),
        ),
    ]
