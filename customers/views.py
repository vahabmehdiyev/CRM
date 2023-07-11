from django.shortcuts import render, redirect
from django.views import View
from .models import Customer

class CustomerListView(View):
    template_name = 'customers.html'
    def get(self,request):
        customers = Customer.objects.all()
        return render(request, self.template_name, {'customers':customers})

    def post(Self,request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        customer = Customer(name=name, email=email, phone=phone, address=address)
        customer.save()
        return redirect('customers')


class CustomerDetailView(View):
    template_name = 'customer_detail.html'

    def get(self, request, pk):
        customer = Customer.objects.get(pk=pk)
        return render(request, self.template_name, {'customer': customer})
        