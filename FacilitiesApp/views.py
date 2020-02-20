from django.shortcuts import render
import datetime
from .models import Apartment

def home(request):
    x = datetime.datetime.now()
    date_tmp = (x.strftime('%d-%m-%Y, %H:%M:%S'))
    
 
#    current_user = request.user
#    disp_temp = date_tmp + " User: " + str(current_user)
    return render(request, "FacilitiesApp/index.html", {"date_str": date_tmp})


def apartment(request):
    textx = {
        'posts': Apartment.objects.all()#.values('title')
       # 'posts': SavedData.objects.filter(author_id = request.user.id)
    }
    return render(request, "FacilitiesApp/apartment.html", textx)