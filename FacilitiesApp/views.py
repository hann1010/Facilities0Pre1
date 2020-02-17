from django.shortcuts import render
import datetime

def home(request):
    x = datetime.datetime.now()
    date_tmp = (x.strftime('%d-%m-%Y, %H:%M:%S'))
    
 
#    current_user = request.user
#    disp_temp = date_tmp + " User: " + str(current_user)
    return render(request, "FacilitiesApp/index.html", {"date_str": date_tmp})
