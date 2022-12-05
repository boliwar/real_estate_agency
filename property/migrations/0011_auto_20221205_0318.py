# Generated by Django 2.2.24 on 2022-12-05 01:18

from django.db import migrations
import phonenumbers

def fill_owner_pure_phone(apps, schema_editor):
    flats = apps.get_model('property', 'Flat')
    for flat in flats.objects.all():
        phone = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number:
            flat.owner_pure_phone = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.E164)

        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20221205_0313'),
    ]

    operations = [
        migrations.RunPython(fill_owner_pure_phone),
    ]
