# Generated by Django 2.2.3 on 2019-07-16 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='id_task',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projmanager.Task'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='status',
            name='level',
            field=models.CharField(max_length=20),
        ),
    ]
