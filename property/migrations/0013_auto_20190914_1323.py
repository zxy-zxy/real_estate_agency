# Generated by Django 2.2.4 on 2019-09-14 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('property', '0012_auto_20190914_1310')]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owners_phonenumber',
            new_name='owner_phonenumber',
        ),
        migrations.RemoveField(model_name='flat', name='owner'),
        migrations.RemoveField(model_name='flat', name='owner_phone_pure'),
        migrations.RemoveField(model_name='flat', name='owners_phonenumber'),
        migrations.AlterField(
            model_name='owner',
            name='owner_flats',
            field=models.ManyToManyField(
                to='property.Flat', verbose_name='Квартиры в собственности'
            ),
        ),
    ]
