# Generated by Django 2.2.4 on 2019-09-14 08:54

from django.db import migrations

import phonenumbers


def update_phonenumber_pure_from_phone_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all():
        phone_pure = phonenumbers.parse(flat.owners_phonenumber, region='RU')
        if not phonenumbers.is_valid_number(phone_pure):
            flat.owner_phone_pure = '+{}{}'.format(
                phone_pure.country_code, phone_pure.national_number
            )
            flat.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all():
        flat.owner_phone_pure = ''
        flat.save()


class Migration(migrations.Migration):
    dependencies = [('property', '0007_flat_owner_phone_pure')]

    operations = [
        migrations.RunPython(update_phonenumber_pure_from_phone_number, move_backward)
    ]
