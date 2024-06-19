from django.shortcuts import render, redirect
import logging
import requests

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from .forms import LoginUser, RegisterUser, StockForm
logger = logging.getLogger(__name__)
# - Home Page
def home(request):
    return render(request, 'dash_app/index.html')

# - Login User
def login(request):
    form = LoginUser()
    
    if request.method=="POST":
        
        form = LoginUser(request, data=request.POST)
        
        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username = username, password = password)

            if user is not None:
                auth.login(request,user)
                return redirect('stock-list')
                
    context = {'form2':form}
    return render(request, 'dash_app/login.html', context=context)
# ***************************************************
# - Register User

def register(request):
    
    form = RegisterUser()
    
    if request.method == "POST":
        
        form = RegisterUser(request.POST)
        
        if form.is_valid():
            
            form.save()
            return redirect('login')
    
    context = {'form':form}
    
    return render(request, 'dash_app/register.html', context=context)
# ***************************************************
# - Logout User

def logout(request):
    auth.logout(request)
    return redirect("login")
# ***************************************************
# - to view all stocks together
@login_required(login_url='login')
def stock_list(request):
    response = requests.get('http://127.0.0.1:9000/api/stocks')
    stocks = response.json()
    
    return render(request, 'dash_app/dashboard.html', {'stocks':stocks})
# ***************************************************
# - to view each stock individually
@login_required(login_url='login')
def stock_detail(request, stock_id):
    response = requests.get(f'http://127.0.0.1:9000/api/stocks/{stock_id}')
    
    stock = response.json()
    
    return render(request, 'dash_app/view-stock.html', {'stock':stock} )

# ***************************************************
# - CREATE

@login_required(login_url='login')
def stock_create(request):
    form = StockForm()
    
    if request.method=='POST':
        form = StockForm(request.POST)
        
        if form.is_valid():
            
            data = {
                'shortname': form.cleaned_data['shortname'],
                'stockname': form.cleaned_data['stockname'],
                'option': form.cleaned_data['option'],
                'quantity': form.cleaned_data['quantity'],
                'price': form.cleaned_data['price']}
            try:
                response = requests.post('http://127.0.0.1:9000/api/stocks/',data = data)
                response.raise_for_status()
                return redirect('stock-list')
            except requests.exceptions.RequestException as e:
                logger.error(f"Error: {e}")
                logger.error(f"JSON data: {data}")
            
        else:
            form = StockForm()
    context = {'form':form}
    return render(request, 'dash_app/create-stock.html', context = context)

# - update a stock record

@login_required(login_url='login')
def stock_update(request, stock_id):
    # logs
    response = requests.get(f'http://127.0.0.1:9000/api/stocks/{stock_id}')
    print(stock_id)
    
    stock = response.json()
    form2 = StockForm(initial=stock)
    
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            data = {
                'shortname': form.cleaned_data['shortname'],
                'stockname': form.cleaned_data['stockname'],
                'option': form.cleaned_data['option'],
                'quantity': form.cleaned_data['quantity'],
                'price': form.cleaned_data['price']
            }
            response = requests.put(f'http://127.0.0.1:9000/api/stocks/{stock_id}/', data = data)
            if response.status_code == 200:
                return redirect('stock-list')
        else:
            # Form is invalid, render the form with errors
            return render(request, 'dash_app/update-stock.html', {'form2': form2, 'stock_id': stock_id})
    
    return render(request, 'dash_app/update-stock.html', {'form2': form2, 'stock_id': stock_id})
# - delete a stock record
def stock_delete(request, stock_id):
    response = requests.delete(f'http://127.0.0.1:9000/api/stocks/{stock_id}/')
    response.raise_for_status()
    return redirect('stock-list')