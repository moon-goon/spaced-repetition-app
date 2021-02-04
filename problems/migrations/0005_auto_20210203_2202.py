# Generated by Django 3.1.5 on 2021-02-04 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0004_auto_20210127_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='begin_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='problem',
            name='hint',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='problem',
            name='problem_statement',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='problem',
            name='repetition_1',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='problem',
            name='repetition_2',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='problem',
            name='repetition_3',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='problem',
            name='source',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]