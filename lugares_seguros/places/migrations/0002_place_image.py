# Generated by Django 4.1 on 2022-08-14 07:33

from django.db import migrations, models
import places.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=places.models.upload_load),
        ),
    ]
