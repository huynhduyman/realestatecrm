# Generated by Django 2.2.4 on 2019-12-19 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_auto_20191213_1026'),
        ('leads', '0010_lead_teams'),
        ('opportunity', '0004_opportunity_teams'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='leads',
            field=models.ManyToManyField(related_name='oppurtunity_leads', to='leads.Lead'),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='listings',
            field=models.ManyToManyField(related_name='oppurtunity_listings', to='listings.Listing'),
        ),
    ]
