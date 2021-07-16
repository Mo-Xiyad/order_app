from django.shortcuts import render
from flower.forms import FlowerOrderForm, MultipleOrderForm
from django.forms import formset_factory

# from .helper import get_product
from .models import Order, Product
from django.utils import timezone
import datetime


def landing_page(request):
    return render(request, 'flower/home.html')

# Use "request.FILES" inside the form when accepting user information


def sign_up(request, ):
    return render(request, 'flower/Sign_up.html')


def slected_item(request, product_pk):
    selected_product = Product.objects.get(pk=product_pk)
    form = FlowerOrderForm()
    if request.method == 'POST':
        OrderForm = FlowerOrderForm(request.POST)

        if OrderForm.is_valid():
            OrderForm.save()
            form = OrderForm
            message = 'Order has been updated!'
            return render(request, 'flower/product_page.html', {'message': message,
                                                                'OrderForm': form,
                                                                'selected_product': selected_product
                                                                })

    return render(request, 'flower/slected_item.html', {'OrderForm': form,
                                                        'selected_product': selected_product})


def product_page(request, *args, **kwargs):
    qs = Product.objects.all()
    product = None
    if qs.exists():
        product = qs.all()

    # if request.method == 'GET':
    #     filled_form = FlowerOrderForm(product_pk)
    #     message = 'Please confirm your oder!'
    #     return render(request, 'flower/order.html', {'form': filled_form,
    #                                                  'message': message,
    #                                                  'selected_product': selected_product})

    return render(request, 'flower/product_page.html', {'object': product})


def order(request):
    multiple_form = MultipleOrderForm()

    if request.method == 'POST':
        filled_form = FlowerOrderForm(request.POST)
        if filled_form.is_valid():
            created_order = filled_form.save()
            created_order.start_datetime = datetime.datetime.now()
            created_order.date = datetime.datetime.now()
            created_order.updated_at = timezone.now()
            created_order_pk = created_order.id
            message = 'Thanks for ordering! Your %s flower bouquet is on its way!' %(filled_form.cleaned_data['name'])
            filled_form = FlowerOrderForm()
        else:
            created_order_pk = None
            message = 'Your order has failed. Please try again or if you are having any issues please contact us.'
        return render(request, 'flower/order.html', {'form': filled_form,
                                                     'message': message,
                                                     'multiple_form': multiple_form,
                                                     'created_order_pk': created_order_pk})
    else:
        form = FlowerOrderForm()
        return render(request, 'flower/order.html', {'form': form,
                                                     'multiple_form': multiple_form})


def multiple_order(request):
    number_of_orders = 3
    filled_multiple_order_form = MultipleOrderForm(request.GET)
    if filled_multiple_order_form.is_valid():
        number_of_orders = filled_multiple_order_form.cleaned_data['number']
    MultipleOrderFormSet = formset_factory(FlowerOrderForm, extra=number_of_orders)
    formset = MultipleOrderFormSet()
    if request.method == 'POST':
        filled_formset = MultipleOrderFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['type'])
            message = 'Your Bouquet has been ordered!'
        else:
            message = 'Order was not created, please tr again!'
        return render(request, 'flower/multiple_order.html', {'message': message,'formset': formset,})
    else:
        return render(request, 'flower/multiple_order.html', {'formset': formset, })


def edit_order(request, pk):
    ordered_bouquet = Order.objects.get(pk=pk)
    form = FlowerOrderForm(instance=ordered_bouquet)
    if request.method == 'POST':
        filled_form = FlowerOrderForm(request.POST, instance=ordered_bouquet)

        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            message = 'Order has been updated!'
            return render(request, 'flower/edit_order.html',
                          {'message': message, 'FlowerOrderForm': form, 'ordered_bouquet': ordered_bouquet})
    return render(request, 'flower/edit_order.html', {'FlowerOrderForm': form, 'ordered_bouquet': ordered_bouquet})

