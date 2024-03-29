import arrow
from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _

from accounts.models import Account, Tags
from contacts.models import Contact
from common.models import User
from common.utils import STAGES, SOURCES, CURRENCY_CODES, STATUS_CHOICE

from teams.models import Teams
from leads.models import Lead
from listings.models import Listing


class Opportunity(models.Model):
    name = models.CharField(pgettext_lazy(
        "Name of Opportunity", "Name"), max_length=64)
    account = models.ForeignKey(
        Account, related_name='opportunities',
        on_delete=models.CASCADE, blank=True, null=True)
    stage = models.CharField(
        pgettext_lazy("Stage of Opportunity",
                      "Stage"), max_length=64, choices=STAGES)
    currency = models.CharField(
        max_length=3, choices=CURRENCY_CODES, blank=True, null=True)
    amount = models.DecimalField(
        _("Opportunity Amount"),
        decimal_places=0, max_digits=12, blank=True, null=True)
    lead_source = models.CharField(
        _("Source of Lead"), max_length=255,
        choices=SOURCES, blank=True, null=True)
    probability = models.IntegerField(default=0, blank=True, null=True)
    contacts = models.ManyToManyField(Contact)
    #leads = models.ManyToManyField(Lead)
    closed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # closed_on = models.DateTimeField(blank=True, null=True)
    closed_on = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICE, max_length=64, blank=True, null=True, default='')
    assigned_to = models.ManyToManyField(
        User, related_name='opportunity_assigned_to')
    created_by = models.ForeignKey(
        User, related_name='opportunity_created_by',
        on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    is_active = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tags, blank=True)
    teams = models.ManyToManyField(Teams, related_name='oppurtunity_teams')
    leads = models.ManyToManyField(Lead, related_name='oppurtunity_leads')
    listings = models.ManyToManyField(Listing, related_name='oppurtunity_listings')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

    @property
    def created_on_arrow(self):
        return arrow.get(self.created_on).humanize()
