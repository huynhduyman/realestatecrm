# Generated by Django 2.2.4 on 2019-12-13 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20191213_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='mota',
        ),
        migrations.AddField(
            model_name='listing',
            name='moTa',
            field=models.TextField(null=True),
        ),
    ]
