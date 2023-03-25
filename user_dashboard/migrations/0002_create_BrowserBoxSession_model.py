# Generated by Django 4.1.7 on 2023-03-25 11:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0001_crate_browserbox_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrowserBoxSession',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ip', models.GenericIPAddressField()),
                ('user_agent', models.TextField()),
                ('last_active', models.DateTimeField()),
                ('browser_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='browser_box', to='user_dashboard.browserbox')),
            ],
            options={
                'verbose_name': 'browser_box_session',
                'verbose_name_plural': 'browser_box_sessions',
                'ordering': ['id'],
            },
        ),
    ]