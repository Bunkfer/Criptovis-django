from django.contrib import messages
from django.shortcuts import render, redirect
import yfinance as yf
from datetime import datetime
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from .forms import CustomUserCreationForm, ContactoForm
from django.contrib.auth import authenticate, login
import json



def home(request):
    if request.method == 'POST':
        moneda = request.POST.get('opcion_seleccionada')
        if moneda != "General":
            labels, data = graf(moneda)
            context = {
                'labels': labels,
                'data': data,
                'moneda': moneda
            }
            return render(request, "app/Home.html", context)
        else:
            return render(request, "app/Home.html")
    else:
        return render(request, "app/Home.html")


def prediccion(request):
    if request.method == 'POST':
        moneda = request.POST.get('opcion_seleccionada')
        if moneda != "General":
            labels, data = graf(moneda)
            y_test, y_pred, labels2 = predict(moneda)
            return render(request, "Prediccion.html", {'labels': labels,
                                                       'data': data, 'moneda': moneda, 'y_test': y_test,
                                                       'y_pred': y_pred, 'labels2': labels2})
        else:
            return render(request, "Prediccion.html")
    else:
        return render(request, "Prediccion.html")


def contact(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Guardado"
        else:
            data["form"] = formulario
    return render(request, "Contact.html", data)


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],
                                password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro correcto")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, "registration/resistro.html", data)


def graf(moneda):
    cripto = yf.download(moneda, start='2015-01-01',
                         end=f"{datetime.today().year}-{datetime.today().month}-{datetime.today().day}")
    x = np.array(cripto['Close'])
    y = cripto.index[-len(x):]
    #data = list(x)
    data = [float(val) for val in x]
    labels = []
    for i in y:  #labels.append(str(i.day) + "-" + str(i.month_name()[:3]) + "-" + str(i.year))
         labels.append(f"{i.day}-{i.strftime('%b')}-{i.year}")
    return labels, data


def predict(moneda):
    # Utilizaremos la base de datos yfinance para tener el valor de las monedas
    cripto = yf.download(moneda, start='2015-01-01',
                         end=f"{datetime.today().year}-{datetime.today().month}-{datetime.today().day}")

    # Calcularemos el promedio de la moneda por una ventana en especifico
    cripto['RollingMean'] = cripto['Close'].rolling(5).mean()

    # Preparacion de la informacion
    cripto.dropna(inplace=True)
    X = np.array(cripto['RollingMean']).reshape(-1, 1)
    y = np.array(cripto['Close'])

    '''En este caso estamos usando un random state para que la seleccion de datos
    sea sempre la misma y no varien los datos al volver a correr el programa
    '''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

    # Crear y entrenar el modelo de regresión lineal
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predice el precio de la moneda usando el modelo
    y_pred = model.predict(X_test)

    """
    y = cripto.index[-len(y_test):]
    labels2 = []
    for i in y:  labels2.append(str(i.day) + "-" + str(i.month_name()[:3]) + "-" + str(i.year))
    return list(y_test), list(y_pred), labels2
    """

    y_dates = cripto.index[-len(y_test):]
    labels2 = [f"{i.day}-{i.strftime('%b')}-{i.year}" for i in y_dates]

    # Convert numpy floats to python floats para JSON
    y_test_list = [float(val) for val in y_test]
    y_pred_list = [float(val) for val in y_pred]

    return y_test_list, y_pred_list, labels2
