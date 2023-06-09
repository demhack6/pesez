# Generated by Django 4.1.7 on 2023-03-25 15:22

import browserbox.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('browserbox', '0002_create_BrowserBoxSession_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='browserbox',
            name='owner',
        ),
        migrations.AddField(
            model_name='browserbox',
            name='create_dt',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='browserbox',
            name='terminate_dt',
            field=models.DateTimeField(default=browserbox.models._add_30_minutes),
        ),
        migrations.AlterField(
            model_name='browserboxsession',
            name='browser_box',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='browserbox.browserbox'),
        ),
    ]
