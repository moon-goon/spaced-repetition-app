# Generated by Django 3.1.5 on 2021-02-04 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0006_auto_20210203_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='begin_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='repetition_1',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='repetition_2',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='repetition_3',
            field=models.DateField(blank=True, null=True),
        ),
    ]
