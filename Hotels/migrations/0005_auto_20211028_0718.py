# Generated by Django 3.2.8 on 2021-10-28 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotels', '0004_alter_hotel_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='room_cat',
            new_name='room_type',
        ),
        migrations.AddField(
            model_name='room',
            name='room_no',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
