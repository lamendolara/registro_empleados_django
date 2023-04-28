from django.shortcuts import render
from django.views.generic import (
    ListView,
)
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from applications.persona.models import Empleado
from .models import Departamento
from .forms import NewDepartamentoForm


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = 'departamentos'
    

class NewDepartamentoView(FormView):
    """En esta clase lo que se hace es implementar la entrada
    de un nuevo registro mediante un formulario ligado a dos modelos Departamento y Persona
    el requerimiento es que solo se cree un Departamento nuevo si hay un empleado registrado en él"""
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = reverse_lazy('departamento_app:departamento_list')

    def form_valid(self, form):
        print('****estamos en el form_valid')
        depa = Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shorname']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        #En empleado realizando de esta manera con Create no es necesario guardar con save
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa

        )
        return super(NewDepartamentoView, self).form_valid(form)

