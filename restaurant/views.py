from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItem, Chef, Contact,Order
from django.contrib import messages
from django.urls import reverse
from .forms import MenuItemForm,OrderForm
# Create your views here.

# View for the homepage (with menu and chef sections)
def  index(request):
     # Fetch menu items by category
    breakfast_items = MenuItem.objects.filter(category='breakfast')
    lunch_items = MenuItem.objects.filter(category='lunch')
    dinner_items = MenuItem.objects.filter(category='dinner')
    
        # Fetch all chefs
    chefs = Chef.objects.all()

    context = {
        'breakfast_items': breakfast_items,
        'lunch_items': lunch_items,
        'dinner_items': dinner_items,
        'chefs': chefs,
    }
    return render(request, 'index.html',context)

# View to handle contact form submissions
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save the contact form data
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        # Show a success message and redirect back to the contact section
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')  # Replace with the correct URL name or view

    return render(request, 'contact.html')


# View for individual menu item
def detail_item(request, item_id):
    # Fetch the menu item by id
    item = MenuItem.objects.get(id=item_id)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.menu_item = item  # Link the order to the selected menu item
            order.save()
            return redirect('order', order_id=order.id)  # Redirect to a success page after ordering
    else:
        form = OrderForm()

    
    return render(request, 'details_item.html',{'item': item, 'form': form})
    
def edit_item(request, item_id):
    item = MenuItem.objects.get(id=item_id)
    
    # If the request is POST, process the form data
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()  # Save the updated item
            return redirect('detail', item_id=item.id)  # Redirect to the item detail page
    else:
        # If the request is GET, display the form with the current item data
        form = MenuItemForm(instance=item)

    return render(request, 'edit_item.html', {'form': form, 'item': item})

def delete_item(request, item_id):
    item = MenuItem.objects.get(id=item_id)
    if request.method == 'POST':
        item.delete()         # If confirmed, delete the item
        return redirect('index')
    return render(request, 'delete_item.html', {'item': item})

def add_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)  # Handle file uploads (e.g., images)
        if form.is_valid():
            form.save()  # Save the new item to the database
            return redirect('index')  # Redirect to the menu or home page after saving
    else:
        form = MenuItemForm()  # Display an empty form
    
    return render(request, 'add_item.html', {'form': form})


def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order.html', {'order': order})

def blog(request):
    return render(request, "blog.html")
 