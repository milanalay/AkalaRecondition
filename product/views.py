from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, Http404
from django.views.generic import DetailView
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import login
from product.forms import IncomingForm, IncomingUpdateForm, OutgoingForm, ExpenditureForm

from product.models.datamodel import Incoming, Outgoing
from product.models.expendituremodel import Expenditure

# Create your views here.
from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils.decorators import method_decorator
from django.db.models import Sum, Avg


def home(request):
    products = Incoming.objects.filter(stock='Available')
    return render(request, 'home.html', {'products': products})


def login(request):
    return render(request, 'login.html')


@user_passes_test(lambda u: u.is_superuser)
def view_dashboard(request):
    
    product_in = Incoming.objects.filter(stock='Available')
    available_product = Incoming.objects.filter(stock='Available').count()
    sold_product = Incoming.objects.filter(stock='Sold').count()
    product_out = Outgoing.objects.all()

    sale_amount = Outgoing.objects.aggregate(Sum('price')).get('price__sum', 0.00)
    buy_amount = Incoming.objects.filter(stock='Sold').aggregate(Sum('price')).get('price__sum', 0.00)
    if sale_amount and buy_amount:
        profit = int(sale_amount - buy_amount)
        profit_percent = int(profit * 100 / buy_amount)
    else:
        profit = 0
        profit_percent = 0

    expenditure = Expenditure.objects.all()
    expenditure_amount = Expenditure.objects.aggregate(Sum('amount')).get('amount__sum', 0.00)
    if expenditure_amount:
        total_expenditure = expenditure_amount
    else:
        total_expenditure = 0
    
    expenditure_average = Expenditure.objects.aggregate(Avg('amount')).get('amount__avg', 0.00)
    if expenditure_average:
        expenditure_avg = int(expenditure_average)
    else:
        expenditure_avg = 0

    context = {
        'object': product_in,
        'available_product': available_product,
        'sold_product': sold_product,
        'data': product_out,
        'profit': profit,
        'profit_percent': profit_percent,
        'total_expenditure': total_expenditure,
        'expenditure_avg': expenditure_avg,
        'expenditure': expenditure,

    }
    return render(request, 'dashboard.html', context)

@user_passes_test(lambda u: u.is_superuser)
def view_product(request):
    products = Incoming.objects.all()

    return render(request, 'product.html', {'products': products})


@user_passes_test(lambda u: u.is_superuser)
def add_incoming(request, *args, **kwargs):
    if request.method == 'POST':
        form = IncomingForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data = Incoming(
                name = form.cleaned_data['name'],
                image = form.cleaned_data['image'],
                model = form.cleaned_data['model'],
                bike_number = form.cleaned_data['bike_number'],
                price = form.cleaned_data['price'],
                sale_price = form.cleaned_data['sale_price'],
                owner = form.cleaned_data['owner'],
                contact = form.cleaned_data['contact'],
                date = form.cleaned_data['date']
            )
            data.save()
            return redirect('product')
    else:
        form = IncomingForm()
    return render(request, 'add_new_form.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def sale_outgoing(request, *args, **kwargs):
    if request.method == 'POST':
        form = OutgoingForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('dashboard')
    else:
        form = OutgoingForm()
    return render(request, 'sale_form.html', {'form': form})


from product.utils import LoginRequiredMixin
class ProductDetailView(LoginRequiredMixin, DetailView):
    queryset = Incoming.objects.all()
    template_name = 'product_detail.html'
    model = Incoming

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        return context

    
    def get_object(self, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            product = Incoming.objects.get(slug=slug) 
        except Incoming.DoesNotExist:
            raise Http404("Not found..")
        except Incoming.MultipleObjectsReturned:
            qs = Incoming.objects.filter(slug=slug)
            product = qs.first()
        except:
            raise Http404("Error..")
        return product


@user_passes_test(lambda u: u.is_superuser)
def update_view(request, slug):
    context = {}
    obj = get_object_or_404(Incoming, slug=slug)
    form = IncomingUpdateForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/product/'+slug)
    
    context['form'] = form
    return render(request, 'update_view.html', context)


@user_passes_test(lambda u: u.is_superuser)
def add_expenditure(request, *args, **kwargs):
    if request.method == 'POST':
        form = ExpenditureForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('dashboard')
    else:
        form = ExpenditureForm()
    return render(request, 'add_expenditure.html', {'form': form})



def search_product(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = Incoming.objects.filter(
                Q(name__icontains=srch) | Q(model__icontains=srch) | Q(bike_number__icontains=srch) | Q(price__icontains=srch) | Q(owner__icontains=srch))

            if match:
                return render(request, 'search_view.html', {'sr': match})
            else:
                messages.error(request, 'No result found')
        else:
            return HttpResponseRedirect('#')
    
    return render(request, 'search_view.html')


def search_home(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = Incoming.objects.filter(stock='Available').filter(
                Q(name__icontains=srch) | Q(model__icontains=srch) | Q(bike_number__icontains=srch) | Q(price__icontains=srch) | Q(owner__icontains=srch))

            if match:
                return render(request, 'search_view_home.html', {'sr': match})
            else:
                messages.error(request, 'No result found')
        else:
            return HttpResponseRedirect('/')
    
    return render(request, 'search_view_home.html')