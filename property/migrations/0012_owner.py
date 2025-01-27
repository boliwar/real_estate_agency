# Generated by Django 2.2.24 on 2022-12-05 01:36

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20221205_0318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('phonenumber', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='CA', verbose_name='Нормализованный номер телефона')),
                ('flats', models.ManyToManyField(blank=True, related_name='flat_owners', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]
