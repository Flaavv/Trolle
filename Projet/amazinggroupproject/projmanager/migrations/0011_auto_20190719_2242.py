# Generated by Django 2.2.3 on 2019-07-19 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projmanager', '0010_merge_20190717_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=250),
        ),
    ]
