from django.utils import timezone
from django import forms
from .models import Wydatek, Dochod, Oszczednosc, Przypomnienie

class WydatekForm(forms.ModelForm):
    class Meta:
        model = Wydatek
        fields = ['kwota', 'kategoria', 'data']  # Dodajemy pole data do formularza
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),  # Dodajemy widget DateInput
        }


class DochodForm(forms.ModelForm):
    class Meta:
        model = Dochod
        fields = ['kwota', 'kategoria', 'data']  # Dodajemy pole data do formularza
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),  # Dodajemy widget DateInput
        }
class OszczednoscForm(forms.ModelForm):
    class Meta:
        model = Oszczednosc
        fields = ['kwota', 'kategoria']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),  # Dodajemy widget DateInput
        }


class PrzypomnienieForm(forms.ModelForm):
    class Meta:
        model = Przypomnienie
        fields = ['tytuł', 'opis', 'data_przypomnienia']
        widgets = {
            'data_przypomnienia': forms.DateInput(attrs={'type': 'date'}),  # Dodajemy widget DateInput
        }


class ZakresDatForm(forms.Form):
    data_rozpoczecia = forms.DateField(
        required=False,
        label='Data rozpoczęcia',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    data_zakonczenia = forms.DateField(
        required=False,
        label='Data zakończenia',
        widget=forms.DateInput(attrs={'type': 'date'})
    )



