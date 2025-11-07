import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Asistencia
from .forms import LoginForm, UploadFileForm, ConsultaForm
import os
from django.conf import settings
from django.db import transaction
from datetime import datetime

ADMIN_VERFRUT_PASS = os.getenv("ADMIN_VERFRUT_PASS")
ADMIN_RAPEL_PASS = os.getenv("ADMIN_RAPEL_PASS")

def login_admin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            empresa = form.cleaned_data['empresa']
            password = form.cleaned_data['password']

            if (empresa == "VERFRUT" and password == ADMIN_VERFRUT_PASS) or \
               (empresa == "RAPEL" and password == ADMIN_RAPEL_PASS):
                request.session["empresa"] = empresa
                return redirect("admin_panel")
            else:
                messages.error(request, "Contraseña incorrecta o empresa no válida")
    else:
        form = LoginForm()
    return render(request, "admin_login.html", {"form": form})

def admin_panel(request):
    empresa = request.session.get("empresa")
    if not empresa:
        return redirect("login_admin")

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            mes = form.cleaned_data["mes"]
            archivo = request.FILES["archivo"]

            try:
                df = pd.read_excel(archivo)
            except Exception as e:
                messages.error(request, f"Error al leer el archivo Excel: {e}")
                return redirect("admin_panel")

            columnas = ["IDTRABAJADOR", "APELLIDOPAT", "APELLIDOMAT", "NOMBRE", "RUT"]
            if not all(col in df.columns for col in columnas):
                messages.error(request, "El archivo no tiene las columnas requeridas.")
                return redirect("admin_panel")

            registros = []
            meses = [
                "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
            ]
            numero_mes = meses.index(mes) + 1

            for _, fila in df.iterrows():
                dni = str(fila["RUT"])
                nombre = f"{fila['APELLIDOPAT']} {fila['APELLIDOMAT']} {fila['NOMBRE']}".strip()
                for col in df.columns[5:]:
                    valor = fila[col]
                    if pd.notna(valor) and str(valor).strip() != "":
                        try:
                            dia = int(col)
                            fecha = f"2025-{str(numero_mes).zfill(2)}-{str(dia).zfill(2)}"
                        except:
                            fecha = str(col)

                        registros.append(
                            Asistencia(
                                dni=dni,
                                nombre=nombre,
                                fecha=fecha,
                                horas_trabajadas=str(valor),
                                mes=mes,
                                empresa=empresa
                            )
                        )

            with transaction.atomic():
                Asistencia.objects.filter(empresa=empresa, mes=mes).delete()
                Asistencia.objects.bulk_create(registros)

            messages.success(request, f"Datos importados correctamente para {empresa} ({len(registros)} registros)")
            return redirect("admin_panel")

    else:
        form = UploadFileForm()

    registros = Asistencia.objects.filter(empresa=empresa).order_by("-fecha")[:20]
    return render(request, "admin_panel.html", {"empresa": empresa, "form": form, "registros": registros})

def logout_admin(request):
    request.session.pop("empresa", None)
    return redirect("login_admin")

def consulta(request):
    df = None
    total_horas = 0
    nombre_trabajador = None

    if request.method == "POST":
        form = ConsultaForm(request.POST)
        if form.is_valid():
            empresa = form.cleaned_data["empresa"]
            dni = form.cleaned_data["dni"].strip()
            mes = form.cleaned_data["mes"]

            registros = Asistencia.objects.filter(
                dni=dni, empresa__iexact=empresa, mes__iexact=mes
            ).order_by("fecha")

            if not registros.exists():
                messages.warning(request, "No se encontraron registros para tu DNI en este mes")
            else:
                df = list(registros.values("nombre", "fecha", "horas_trabajadas"))
                # calcular total
                total_h = 0.0
                for r in df:
                    try:
                        total_h += float(r.get("horas_trabajadas") or 0)
                    except:
                        # si no es numérico, tratar como 0
                        pass
                total_horas = round(total_h, 2)
                nombre_trabajador = df[0]["nombre"]
    else:
        form = ConsultaForm()

    return render(request, "consulta.html", {
        "form": form,
        "df": df,
        "total_horas": total_horas,
        "nombre": nombre_trabajador
    })
