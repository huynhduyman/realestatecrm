# Generated by Django 2.2.4 on 2020-01-10 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0009_auto_20191223_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='currency',
            field=models.CharField(blank=True, choices=[('VND', 'VND, Dong'), ('USD', '$, Dollar')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='invoicehistory',
            name='currency',
            field=models.CharField(blank=True, choices=[('VND', 'VND, Dong'), ('USD', '$, Dollar')], max_length=3, null=True),
        ),
    ]
