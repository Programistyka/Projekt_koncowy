from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.db.models import Sum, DecimalField
from .models import Wydatek,Dochod,Przypomnienie
from .forms import DochodForm, WydatekForm, PrzypomnienieForm, ZakresDatForm





def home(request):
    return render(request, 'home.html')
def lista_wydatkow(request):
    queryset = Wydatek.objects.all()

    form = ZakresDatForm(request.GET)
    if form.is_valid():
        data_rozpoczecia = form.cleaned_data['data_rozpoczecia']
        data_zakonczenia = form.cleaned_data['data_zakonczenia']
        if data_rozpoczecia and data_zakonczenia:
            queryset = queryset.filter(
                data__gte=data_rozpoczecia,
                data__lte=data_zakonczenia
            )

    suma_wydatkow = queryset.aggregate(Sum('kwota'))['kwota__sum'] or 0
    suma_wydatkow = round(suma_wydatkow, 2)

    return render(request, 'Wydatki.html', {'wydatki': queryset, 'form': form, 'suma_wydatkow': suma_wydatkow})
def dodaj_wydatek(request):
    if request.method == 'POST':
        form = WydatekForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_wydatkow')
    else:
        form = WydatekForm()
    return render(request, 'dodaj_wydatek.html', {'form': form})

def usun_wydatek(request, pk):
    wydatek = get_object_or_404(Wydatek, pk=pk)
    wydatek.delete()
    messages.success(request, 'Wydatek został usunięty!')
    return redirect('lista_wydatkow')
def lista_dochodow(request):
    queryset = Dochod.objects.all()

    form = ZakresDatForm(request.GET)
    if form.is_valid():
        data_rozpoczecia = form.cleaned_data['data_rozpoczecia']
        data_zakonczenia = form.cleaned_data['data_zakonczenia']
        if data_rozpoczecia and data_zakonczenia:
            queryset = queryset.filter(
                data__gte=data_rozpoczecia,
                data__lte=data_zakonczenia
            )

    suma_dochodow = queryset.aggregate(Sum('kwota'))['kwota__sum'] or 0
    suma_dochodow = round(suma_dochodow, 2)

    return render(request, 'Dochody.html', {'dochody': queryset, 'form': form, 'suma_dochodow': suma_dochodow})
def dodaj_dochod(request):
    if request.method == 'POST':
        form = DochodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_dochodow')
    else:
        form = DochodForm()
    return render(request, 'dodaj_dochod.html', {'form': form})

def usun_dochod(request, pk):
    dochod = get_object_or_404(Wydatek, pk=pk)
    dochod.delete()
    messages.success(request, 'Dochod został usunięty!')
    return redirect('lista_dochodow')


def lista_oszczednosci(request):
    form = ZakresDatForm(request.GET)
    bilans = 0

    if form.is_valid():
        data_rozpoczecia = form.cleaned_data['data_rozpoczecia']
        data_zakonczenia = form.cleaned_data['data_zakonczenia']

        if data_rozpoczecia and data_zakonczenia:
            dochody = Dochod.objects.filter(
                data__gte=data_rozpoczecia,
                data__lte=data_zakonczenia
            ).aggregate(suma=Sum('kwota', output_field=DecimalField()))['suma'] or 0
            wydatki = Wydatek.objects.filter(
                data__gte=data_rozpoczecia,
                data__lte=data_zakonczenia
            ).aggregate(suma=Sum('kwota', output_field=DecimalField()))['suma'] or 0

            bilans = dochody + wydatki  # Wydatki są ujemne

    return render(request, 'Oszczednosci.html', {
        'form': form,
        'bilans': bilans,
        'data_rozpoczecia': data_rozpoczecia,
        'data_zakonczenia': data_zakonczenia
    })
def lista_przypomnien(request):
    queryset = Przypomnienie.objects.all()

    form = ZakresDatForm(request.GET)
    if form.is_valid():
        data_rozpoczecia = form.cleaned_data['data_rozpoczecia']
        data_zakonczenia = form.cleaned_data['data_zakonczenia']
        if data_rozpoczecia and data_zakonczenia:
            queryset = queryset.filter(
                data_przypomnienia__gte=data_rozpoczecia,
                data_przypomnienia__lte=data_zakonczenia
            )

    # Sortowanie
    sort_order = request.GET.get('sort', 'asc')
    if sort_order == 'desc':
        queryset = queryset.order_by('-data_przypomnienia')
    else:
        queryset = queryset.order_by('data_przypomnienia')

    if request.method == 'POST':
        form = PrzypomnienieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_przypomnien')

    else:  # Dodano else, aby formularz był zawsze dostępny
        form = PrzypomnienieForm()

    return render(request, 'przypomnienia.html', {'przypomnienia': queryset, 'form': form})
def dodaj_przypomnienie(request):
    if request.method == 'POST':
        form = PrzypomnienieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_przypomnien')  # Przekierowanie do listy przypomnień po dodaniu
    else:
        form = PrzypomnienieForm()
    return render(request, 'przypomnienia.html', {'form': form})  # Użyj tego samego szablonu co dla listy
def usun_przypomnienie(request, pk):
    przypomnienie = get_object_or_404(Przypomnienie, pk=pk)
    przypomnienie.delete()
    messages.success(request, 'Przypomnienie zostało usunięte!')
    return redirect('lista_przypomnien')
