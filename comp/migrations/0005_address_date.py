# Generated by Django 3.2 on 2021-07-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0004_remove_address_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='date',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
