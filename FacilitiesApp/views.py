from django.shortcuts import render
import datetime
from .models import Apartment, Ticket
from .forms import TicketForm
from .forms import FilterForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
#    ListView,
#    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def home(request):

    date_tmp = datetime.datetime.now().strftime('%d.%m.%Y, %H:%M:%S')

    
    dic_x = {}
    if request.user.is_authenticated:
        db_data = ''
        members_of_tmp = request.user.profile.members_of
        repair_state_filter = request.POST.get('filter_repair_state')
        repair_year_filter = request.POST.get('repair_year')
        filter_tmp = FilterForm(request.POST or None)
        if str(repair_state_filter) == str(None):
            repair_state_filter = 'New'
        if str(repair_year_filter) == str(None):
            db_data = Ticket.objects.filter(company_name = members_of_tmp)\
                .filter(repair_state = repair_state_filter).order_by('-date_posted')
        else:
            db_data = Ticket.objects.filter(company_name = members_of_tmp)\
                .filter(repair_state = repair_state_filter)\
                .filter(date_repair__year = repair_year_filter).order_by('-date_posted')
        paginator = Paginator(db_data, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        dic_x = {
        'posts': page_obj,
        'date_str': date_tmp,
        'members_of': members_of_tmp,
        'filter': filter_tmp
        }

    return render(request, "FacilitiesApp/index.html", dic_x)


def apartment(request):
    dic_x = {}
    if request.user.is_authenticated:
        db_data = Apartment.objects.filter(company_name = request.user.profile.members_of).order_by('address')
        paginator = Paginator(db_data, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        dic_x = {
            'posts': page_obj
        }
    return render(request, "FacilitiesApp/apartment.html", dic_x)



class ApartmentCreateView(LoginRequiredMixin, CreateView):
    model = Apartment
    success_url = '/apartment'


    def get_template_names(self):
        if  self.request.user.profile.user_level > 2:
            template_name = 'FacilitiesApp/apartment_form_new.html'
        else:
            template_name = 'FacilitiesApp/forbidden.html'
        return template_name

    fields = ['first_name', 'last_name', 'address', 'phone_no', 'email', 'house_company', 'notes']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.company_name = self.request.user.profile.members_of
        form.instance.username_first = self.request.user
        messages.add_message(self.request, messages.INFO, 'Apartment has been saved!')
        return super().form_valid(form)


class ApartmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Apartment
    success_url = '/apartment'
    fields = ['first_name', 'last_name', 'address', 'phone_no', 'email', 'house_company', 'notes']

    def get_template_names(self):
        if  self.request.user.profile.user_level > 2:
            template_name = 'FacilitiesApp/apartment_form.html'
        else:
            template_name = 'FacilitiesApp/apartment_list.html'
        return template_name

    def form_valid(self, form):
        form.instance.author = self.request.user
        db_data = Apartment.objects.all().values().get(pk=self.kwargs.get('pk'))
        info = 'Apartment '+ db_data['address']+ ' has been updated!'
        messages.add_message(self.request, messages.INFO, info)
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
        if self.request.user == Apartment.author and self.request.user.profile.user_level > 3:
            return True
        return False 

class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketForm
    success_url = '/'

    def get_template_names(self):
        if  self.request.user.profile.user_level > 1:
            template_name = 'FacilitiesApp/ticket_form_new.html'
        else:
            template_name = 'FacilitiesApp/forbidden.html'
        return template_name

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.company_name = self.request.user.profile.members_of
        form.instance.username_first = self.request.user
        messages.add_message(self.request, messages.INFO, 'Ticket has been saved!')
        return super().form_valid(form)


class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ticket
    form_class = TicketForm
    success_url = '/'
#    fields = ['first_name', 'last_name', 'address', 'phone_no', 'email', 'house_company', 'notes']

    def get_template_names(self):
        if  self.request.user.profile.user_level > 1:
            template_name = 'FacilitiesApp/ticket_form.html'
        else:
            template_name = 'FacilitiesApp/ticket_list.html'
        return template_name

    def form_valid(self, form):
        form.instance.author = self.request.user
        db_data = Ticket.objects.all().values().get(pk=self.kwargs.get('pk'))
        info = 'Ticket for '+ db_data['address']+ ' has been updated!'
        messages.add_message(self.request, messages.INFO, info)
        return super().form_valid(form)

    def test_func(self):
        Ticket = self.get_object()
        if self.request.user.profile.members_of == Ticket.company_name:
            return True
        return False



class TicketPreCreateView(LoginRequiredMixin, CreateView):


    def get_initial(self):
        super(TicketPreCreateView, self).get_initial()
        db_data = Apartment.objects.all().values().get(pk=self.kwargs.get('pk'))
        first_name = ''
        last_name = ''
        address = ''
        phone_no = ''
        email = ''
        house_company = ''
  
        if db_data['company_name'] == self.request.user.profile.members_of:
            first_name = db_data['first_name']
            last_name = db_data['last_name']
            address = db_data['address']
            phone_no = db_data['phone_no']
            email = db_data['email']
            house_company = db_data['house_company']
 
        
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

    def get_template_names(self):
        if  self.request.user.profile.user_level > 1:
            template_name = 'FacilitiesApp/ticket_form_new.html'
        else:
            template_name = 'FacilitiesApp/forbidden.html'
        return template_name

#    fields = ['first_name', 'last_name', 'address','repair_state','repair','date_repair', 'phone_no', 'email', 'house_company', 'notes']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.company_name = self.request.user.profile.members_of
        form.instance.username_first = self.request.user
        messages.add_message(self.request, messages.INFO, 'Ticket has been saved!')
        return super().form_valid(form)