# Generated by Django 3.1.5 on 2021-01-28 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_auto_20210127_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='ranking',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]