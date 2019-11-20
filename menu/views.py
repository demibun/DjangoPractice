from django.shortcuts import render, redirect, get_list_or_404
from .models import *
from django.views.generic import View
from .forms import *
from datetime import datetime


class AddMenu(View):
    def post(self, request):
        form = AddMenuForm(request.POST)
        if form.is_valid():
            menu_name = form.cleaned_data['menu_name']
            store_name = form.cleaned_data['store_name']
            price = form.cleaned_data['price']

            new_menu = Menu(menu_name=menu_name, store_name=store_name, price=price)
            new_menu.save()
            return redirect('/menu/showMenus/')

    def get(self, request):
        form = AddMenuForm()
        return render(request, 'menu/menu/add_menu.html', {'form': form})


class ShowMenus(View):
    def get(self, request):
        menus = Menu.objects.all()
        return render(request, 'menu/menu/show_menus.html', {'menus': menus})


class AddStore(View):
    def post(self, request):
        form = AddStoreForm(request.POST)
        if form.is_valid():
            store_name = form.cleaned_data['store_name']
            menu_name = form.cleaned_data['menu_name']
            price = form.cleaned_data['price']
            location = form.cleaned_data['location']
            tel = form.cleaned_data['tel']

            new_menu = Menu(menu_name=menu_name, price=price, store_name=store_name)
            new_menu.save()

            new_store = Store(store_name=store_name, menu=new_menu, location=location, tel=tel)
            new_store.save()

            return redirect('/menu/showStores/')

    def get(self, request):
        form = AddStoreForm()
        return render(request, 'menu/menu/add_store.html', {'form': form})


class ShowStore(View):
    def get(self, request):
        stores = Store.objects.all()
        return render(request, 'menu/menu/show_stores.html', {'stores': stores})


class StoreDetail(View):
    def get(self, request, store_name):
        menus = get_list_or_404(Menu, store_name=store_name)
        return render(request, 'menu/menu/stores_detail.html', {'menus': menus})


class Order(View):
    def get(self, request, store_name, menu_name):
        menus = get_list_or_404(Menu, menu_name=menu_name)
        for menu in menus:
            if menu.store_name == store_name:
                price = menu.price

        return render(request, 'menu/order/order.html',
                      {'store_name': store_name, 'menu_name': menu_name, 'price': price})


class OrderDetail(View):
    def post(self, request, store_name, menu_name):
        location = request.POST['location']
        new_order = Order(name="홍길동", menu_name=menu_name, store_name=store_name, tel="010-1234-5678",
                          location=location, time=datetime.now())
        return render(request, 'menu/order/order_detail.html',
                      {'location': location, 'store_name': store_name, 'menu_name': menu_name})
