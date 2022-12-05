# Generated by Django 2.2.24 on 2022-12-05 01:05

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20221205_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='owners_phonenumber',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RU', verbose_name='Номер телефона'),
        ),
    ]