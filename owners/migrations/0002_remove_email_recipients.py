# Generated by Django 2.2.4 on 2020-01-10 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='recipients',
        ),
    ]
