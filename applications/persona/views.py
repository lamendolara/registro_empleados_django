from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView

)
# models
from .models import Empleado
# forms
from .forms import EmpleadoForm


class InicioView(TemplateView):
    """Vista que carga la pagina de inicio"""
    template_name = "inicio.html"


class ListAllEmpleados(ListView):
    """Lista de todos los empleados"""
    template_name = 'persona/list_all.html'
    paginate_by = 4  # Paginación de 4 resultados por pag
    ordering = 'last_name'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", "")
        #icontains : Busca la palabra clave dentro de full name. Siempre busca cadenas con similutudes.
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave)
        return lista


class ListEmpleadosAdmin(ListView):
    """Lista de todos los empleados"""
    template_name = 'persona/lista_empleados.html'
    paginate_by = 8  # Paginación de 8 resultados por pag
    ordering = 'last_name'
    context_object_name = 'empleados'
    #Al no tener 'def get_queryset()' debe incluirse siempre el Model
    model = Empleado


class ListByAreaEmpleado(ListView):
    """Lista de empleados de un área"""
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name=area)
        return lista


class ListByJobEmpleado(ListView):
    """Lista de empleados según tipo de trabajo, este no es muy funcional porque los valores de 'trabajo' son números"""
    template_name = 'persona/by_job.html'
    context_object_name = 'by_job'

    def get_queryset(self):
        print('****************')
        palabra_clave = self.request.GET.get("job", "")
        print(palabra_clave)
        lista = Empleado.objects.filter(
            job=palabra_clave)
        print('lista resultado:', lista)
        return lista


class ListEmpleadosByKword(ListView):
    """Lista empleados por palabra clave"""
    template_name = 'persona/by_kword.html'
    context_object_name = 'by_first_name'

    def get_queryset(self):
        print('****************')
        palabra_clave = self.request.GET.get("kword", "")
        lista = Empleado.objects.filter(
            first_name=palabra_clave)
        return lista


class ListHabilidadesEmpleado(ListView):
    """Lista de empleados por habilidades"""
    template_name = "persona/habilidades.html"
    context_object_name = 'habilidades'

    def get_queryset(self):
        id_empleado = self.request.GET.get("idEmpleado", '')
        empleado = Empleado.objects.get(id=id_empleado)
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    # #Ejemplo de cambio en un método de detail view
    # def get_context_data(self, **kwargs):
    #     context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
    #     context['titulo'] = 'Ejemplo de get_context_data' #poner en HTML {{ titulo }}
    #     return context


class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    #fields para que se habiliten todos los campos de la clase usar :  '__all__'
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_all')

    def form_valid(self, form):
        """Si el formulario es validado, guarda el campo asociado."""
        #el commit false es porque no es buena práctica guardar dos veces en una func.
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    form_class = EmpleadoForm
    # fields = [
    #     'first_name',
    #     'last_name',
    #     'job',
    #     'departamento',
    #     'habilidades',
    #     'avatar',
    #
    # ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    #El metodo post se ejecuta antes del metodo form_valid, se pueden interceptar datos aun no guardados ni validados.
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('**************METODO POST*************')
        print('=================')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('**************METODO FORM VALID*************')
        print('***************************')
        return super(EmpleadoUpdateView, self).form_valid(form)


class DeleteSuccessView(TemplateView):
    template_name = "persona/delete_success.html"


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    #el Template en este caso se utiliza como mensaje de confirmación
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')


