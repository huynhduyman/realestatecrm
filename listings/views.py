from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from common.access_decorators_mixins import sales_access_required
from .models import Listing


@login_required
@sales_access_required
def listings_list(request):
    if request.user.role == 'ADMIN' or request.user.is_superuser:
        listings = Listing.objects.all().distinct()
    else:
        listings = Listing.objects.filter(
            Q(created_by=request.user) | Q(assigned_to=request.user)).distinct()
    today = datetime.today().date()
    return render(request, 'listings_listings_list.html', {'listings': listings, 'today': today})


@login_required
@sales_access_required
def listing_create(request):
    return ''
