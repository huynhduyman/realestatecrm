# Generated by Django 2.2.4 on 2019-12-20 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunity', '0005_auto_20191219_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='status',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('Assigned', 'Assigned'), ('Pending', 'Pending'), ('Closed', 'Closed'), ('Rejected', 'Rejected'), ('Duplicate', 'Duplicate')], default='', max_length=64, null=True),
        ),
    ]
