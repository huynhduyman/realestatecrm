# Generated by Django 2.2.4 on 2019-12-13 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20191213_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='feature',
            field=models.TextField(null=True),
        ),
    ]