from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
  #  Do wydatków
    path('Wydatki/', views.lista_wydatkow, name='lista_wydatkow'),
    path('dodaj_wydatek/', views.dodaj_wydatek, name='dodaj_wydatek'),
    path('usun_wydatek/<int:pk>/', views.usun_wydatek, name='usun_wydatek'),

    #  Do dochodów
    path('Dochody/', views.lista_dochodow, name='lista_dochodow'),
    path('dodaj_dochod/', views.dodaj_dochod, name='dodaj_dochod'),
    path('usun_dochod/<int:pk>/', views.usun_dochod, name='usun_dochod'),

    path('Przypomnienia/', views.lista_przypomnien, name='lista_przypomnien'),  # Poprawiono nazwę URL
    path('dodaj_przypomnienie/', views.dodaj_przypomnienie, name='dodaj_przypomnienie'),
    path('usun_przypomnienie/<int:pk>/', views.usun_przypomnienie, name='usun_przypomnienie'),

    #  Do oszczędności
    path('Oszczednosci/', views.lista_oszczednosci, name='Oszczednosci'),
]
