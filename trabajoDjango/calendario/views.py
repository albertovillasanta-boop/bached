from datetime import datetime
from django.shortcuts import render

def calendario(request, fecha):

    fecha_obj = datetime.strptime(fecha, "%d-%m-%Y")

    mi_dia = fecha_obj.day
    mi_mes = fecha_obj.month
    mi_ano = fecha_obj.year

    mensaje = f"La fecha introducida es {mi_dia}/{mi_mes}/{mi_ano}"

    return render(request, 'calendario/fecha.html', {
    'dia': mi_dia,
    'mes': mi_mes,
    'ano': mi_ano,
    'mensaje': mensaje
    })