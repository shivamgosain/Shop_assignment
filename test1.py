from math import cos, asin, sqrt, pi

lat2=18.596189
lat1=18.5979600
lon2=73.712791
lon1=73.7007900

def distance(lat1, lon1, lat2, lon2):
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a))
print(distance(lat1, lon1, lat2, lon2))

'''
def search_shop(request):
    list1=[]
    if request.method == 'POST':
        data=request.POST
        user_latitude=float(data.get('user_latitude'))
        user_longitude=float(data.get('user_longitude'))
        user_distance=float(data.get('user_distance'))
        query_set=Shop.objects.all()        
        p=pi/180
        for shop in query_set:
            lat1=float(shop.latitude)
            lon1=float(shop.longitude)
            a=0.5 - cos((user_latitude-lat1)*p)/2 + cos(lat1*p) * cos(user_latitude*p) * (1-cos((user_longitude-lon1)*p))/2
            b=12742 * asin(sqrt(a))
            if (user_distance) >= b:
                context={'shops':Shop.objects.all}        
            return render(request,'search_shop.html',context)
        return redirect('/search_shops')
        '''