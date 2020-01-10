# Generated by Django 2.1.7 on 2019-06-04 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_date_of_meeting'),
        ('common', '0014_auto_20190524_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachments',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events_attachment', to='events.Event'),
        ),
        migrations.AddField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events_comments', to='events.Event'),
        ),
    ]
