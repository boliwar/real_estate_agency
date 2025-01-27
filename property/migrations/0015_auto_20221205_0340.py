# Generated by Django 2.2.24 on 2022-12-05 01:40

from django.db import migrations

def fill_owner(apps, schema_editor):
    flats = apps.get_model('property', 'Flat')
    owners = apps.get_model('property', 'Owner')
    flats_set = flats.objects.all()
    if flats_set.exists():
        for flat in flats_set.iterator():
            owners.objects.get_or_create(owner=flat.owner, defaults={
                'phonenumber': flat.owners_phonenumber,
                'pure_phone': flat.owner_pure_phone,
            })


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20221205_0339'),
    ]

    operations = [
        migrations.RunPython(fill_owner),
    ]
