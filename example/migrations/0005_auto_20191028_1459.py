# Generated by Django 2.2.6 on 2019-10-28 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0004_auto_20191028_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='Episodes',
            field=models.PositiveSmallIntegerField(),
        ),
    ]