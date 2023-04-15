# Generated by Django 4.1.7 on 2023-04-15 12:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0003_menuitem_delete_menu"),
    ]

    operations = [
        migrations.CreateModel(
            name="Menu",
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
                ("name", models.CharField(max_length=200)),
                ("price", models.IntegerField()),
                (
                    "menu_item_description",
                    models.TextField(default="", max_length=1000),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="booking",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="menuitem",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
