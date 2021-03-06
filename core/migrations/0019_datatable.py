# Generated by Django 3.0.5 on 2020-07-08 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0018_table_hidden"),
    ]

    operations = [
        migrations.CreateModel(
            name="DataTable",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("db_table_name", models.TextField()),
                ("active", models.BooleanField(default=False)),
                (
                    "table",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="data_tables",
                        to="core.Table",
                    ),
                ),
            ],
        ),
    ]
