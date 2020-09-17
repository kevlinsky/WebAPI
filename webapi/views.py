from django.shortcuts import render, redirect

from .forms import *
from django.views.generic import ListView, CreateView
from rest_framework import generics
from .serializers import TicketSerializer
import requests


class TicketAPIView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
    lookup_field = 'pk'


class CreateTicketView(CreateView):
    model = Ticket
    template_name = 'create_ticket.html'
    success_url = 'tickets:list'
    form_class = TicketForm

    def post(self, request, *args, **kwargs):
        form = TicketForm(request.POST)
        if form.is_valid():
            post_data = {
                "number": request.POST.get('number'),
                "date": "%s-%s-%s" % (request.POST.get('date_year'), request.POST.get('date_month'), request.POST.get('date_day')),
                "time": request.POST.get('time')
            }
            requests.post('http://127.0.0.1:8000/tickets/api/create/', data=post_data)
            return redirect('tickets:list')
        else:
            return render(request, 'create_ticket.html', context={'form': TicketForm, 'errors': form.errors})


class ListTicketView(ListView):
    model = Ticket
    template_name = 'list_tickets.html'
