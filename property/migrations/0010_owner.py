# Generated by Django 2.2.4 on 2019-09-14 09:48

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [('property', '0009_auto_20190914_1237')]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'owner_initials',
                    models.CharField(max_length=200, verbose_name='ФИО владельца'),
                ),
                (
                    'owners_phonenumber',
                    models.CharField(max_length=20, verbose_name='Номер владельца'),
                ),
                (
                    'owner_phone_pure',
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True,
                        max_length=128,
                        region=None,
                        verbose_name='Нормализованный номер владельца',
                    ),
                ),
                (
                    'owner_flats',
                    models.ManyToManyField(
                        related_name='owners_to_flats',
                        to='property.Flat',
                        verbose_name='Квартиры в собственности',
                    ),
                ),
            ],
        )
    ]
