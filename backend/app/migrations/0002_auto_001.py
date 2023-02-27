# Generated by Django 4.1.2 on 2023-02-07 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            "ALTER TABLE CDC_CONN ADD COLUMN id SERIAL"
        ),
        migrations.RunSQL(
            "ALTER TABLE CDC_FIELDS ADD COLUMN id SERIAL"
        ),
        migrations.RunSQL(
            "ALTER TABLE CDC_STATUS ADD COLUMN id SERIAL"
        ),
        migrations.RunSQL(
            "ALTER TABLE CDC_TABLES ADD COLUMN id SERIAL"
        ),
    ]