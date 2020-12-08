from django.shortcuts import render

from listings.models import Listing
from realtors.models import Realtor
from owners.models import Owner
from listings.options import bedroom_options, price_options, province_options

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'bedroom_options': bedroom_options,
        'price_options': price_options,
        'province_options': province_options,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')

    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    owners = Owner.objects.all()

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
        'owners': owners
    }
    return render(request, 'pages/about.html', context)