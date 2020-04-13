from django.shortcuts import render
import datetime
from .models import Apartment, Ticket
from .forms import TicketForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
#    ListView,
#    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def home(request):
    x = datetime.datetime.now()
    date_tmp = (x.strftime('%d.%m.%Y, %H:%M:%S'))

    members_of_tmp = ''
    textx = {}
    if request.user.is_authenticated:
        members_of_tmp = request.user.profile.members_of
        textx = {
        'posts': Ticket.objects.filter(company_name = request.user.profile.members_of).order_by('-date_posted'),
        'date_str': date_tmp,
        'members_of': members_of_tmp
       # 'posts': Apartment.objects.filter(company_name = request.user.profile.members_of).order_by('address')
        }


#    date_tmp = request.user.profile.members_of
 
#    current_user = request.user
#    disp_temp = date_tmp + " User: " + str(current_user)
    return render(request, "FacilitiesApp/index.html", textx)


def apartment(request):
    textx = {
       # 'posts': Apartment.objects.all()#.values('title')
        'posts': Apartment.objects.filter(company_name = request.user.profile.members_of).order_by('address')
    }
    return render(request, "FacilitiesApp/apartment.html", textx)

#class ApartmentDetailView(DetailView):
#    model = Apartment


class ApartmentCreateView(LoginRequiredMixin, CreateView):
    model = Apartment
    success_url = '/apartment'
    template_name = 'FacilitiesApp/apartment_form_new.html'
    fields = ['first_name', 'last_name', 'address', 'phone_no', 'email', 'house_company', 'notes']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.company_name = self.request.user.profile.members_of
        form.instance.username_first = self.request.user
        return super().form_valid(form)


class ApartmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Apartment
    success_url = '/apartment'
    fields = ['first_name', 'last_name', 'address', 'phone_no', 'email', 'house_company', 'notes']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Apartment = self.get_object()
        if self.request.user.profile.members_of == Apartment.company_name:
            return True
        return False


class ApartmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Apartment
    success_url = '/apartment'

    def test_func(self):
        Apartment = self.get_object()
        if self.request.user == Apartment.author:
            return True
        return False 

class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketForm
    success_url = '/'
    template_name = 'FacilitiesApp/ticket_form_new.html'
#    fields = ['first_name', 'last_name', 'address','repair_state','repair','date_repair', 'phone_no', 'email', 'house_company', 'notes']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.company_name = self.request.user.profile.members_of
        form.instance.username_first = self.request.user
        return super().form_valid(form)


class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ticket
    form_class = TicketForm
    success_url = '/'
#    fields = ['first_name', 'last_name', 'address', 'phone_no', 'email', 'house_company', 'notes']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Ticket = self.get_object()
        if self.request.user.profile.members_of == Ticket.company_name:
            return True
        return False



class TicketPreCreateView(LoginRequiredMixin, CreateView):


    def get_initial(self):
        super(TicketPreCreateView, self).get_initial()
        db_dic = Apartment.objects.all().values().get(pk=self.kwargs.get('pk'))
        first_name = ''
        last_name = ''
        address = ''
        phone_no = ''
        email = ''
        house_company = ''
  
        if db_dic['company_name'] == self.request.user.profile.members_of:
            first_name = db_dic['first_name']
            last_name = db_dic['last_name']
            address = db_dic['address']
            phone_no = db_dic['phone_no']
            email = db_dic['email']
            house_company = db_dic['house_company']
 
        
        user = self.request.user
        self.initial = {
            'first_name': first_name,
            'last_name':last_name, 
            'address':address,
            'phone_no':phone_no,
            'email':email,
            'house_company':house_company
            }
        return self.initial    
        

    model = Ticket
    form_class = TicketForm
    success_url = '/'
    template_name = 'FacilitiesApp/ticket_form_new.html'
#    fields = ['first_name', 'last_name', 'address','repair_state','repair','date_repair', 'phone_no', 'email', 'house_company', 'notes']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.company_name = self.request.user.profile.members_of
        form.instance.username_first = self.request.user
        return super().form_valid(form)