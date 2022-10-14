from ast import keyword
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import price_choices, bedroom_choices, state_choices

from .models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.Get.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
        
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html')

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords

    if 'keywords' in request.Get:
       keywords = request.Get['keywords']
       if keywords:
        queryset_list =  queryset_list.filter(description__icontains=keywords)

    # City 

    if 'city' in request.Get:
        city = request.Get['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)


    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list 
    }
    return render(request, 'listings/search.html', context)
