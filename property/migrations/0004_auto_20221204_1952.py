# Generated by Django 2.2.24 on 2022-12-04 16:35

from django.db import migrations


def fill_new_builder(apps, schema_editor):
    flats = apps.get_model('property', 'Flat')
    for flat in flats.objects.all():
        if flat.construction_year >= 2015:
            flat.new_building = True
        else:
            flat.new_building = False

        flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0003_auto_20221204_1658'),
    ]

    operations = [
        migrations.RunPython(fill_new_builder),
    ]
