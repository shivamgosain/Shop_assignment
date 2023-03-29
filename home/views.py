from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
# Create your views here.

def home(request):
    if request.method == 'POST':
        data=request.POST
        shop_name=data.get('shop_name')
        shop_type=data.get('shop_type')
        latitude=data.get('latitude')
        longitude=data.get('longitude')
        Shop.objects.create(shop_name=shop_name,shop_type=shop_type,latitude=latitude,longitude=longitude)
        return redirect('/')
    query_set=Shop.objects.all()
    context={'shops':query_set}
    print(context)
    return render(request, 'home.html',context)

def delete_shop(request,id):
    query_set=Shop.objects.get(id=id)
    query_set.delete()
    return redirect('/')

def update_shop(request,id):
    query_set=Shop.objects.get(id=id)
    if request.method == 'POST':
        data=request.POST
        shop_name=data.get('shop_name')
        shop_type=data.get('shop_type')
        latitude=data.get('latitude')
        longitude=data.get('longitude')
        query_set.shop_name=shop_name
        query_set.shop_type=shop_type
        query_set.latitude=latitude
        query_set.longitude=longitude
        query_set.save()
        return redirect('/')
    context={'shop':query_set}
    return render(request, 'update_shop.html',context)

def search_shop(request):
    if request.method == 'POST':
        user_latitude = float(request.POST['user_latitude'])
        user_longitude = float(request.POST['user_longitude'])
        user_distance = float(request.POST['user_distance'])

        locations = Shop.objects.all()

        # Filter locations within max_distance km from user
        filtered_locations = [
            location for location in locations
            if location.distance_to(user_latitude, user_longitude) <= user_distance
        ]
        print(filtered_locations)
        return render(request, 'search_shop.html', {'shops': filtered_locations})
    else:
        return render(request, 'search_shop.html')
        
'''
        def distance(lat1, lon1, lat2, lon2):
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a))
'''