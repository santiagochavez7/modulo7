from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# vistas.py
from .modelos import Laboratorio, DirectorGeneral, Producto


def inicio(request):
    return render(request, 'investigacion/principal.html')

class LaboratorioListView(ListView):
    model = Laboratorio
    # Cambio del nombre del template a 'lista_investigacion.html'
    template_name = 'investigacion/lista_investigacion.html'
    context_object_name = 'laboratorios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['visit_count'] = self.request.session.get('visit_count', 0)
        self.request.session['visit_count'] = context['visit_count'] + 1
        return context

class LaboratorioCreateView(CreateView):
    model = Laboratorio
    # Cambio del nombre del template a 'formulario_investigacion.html'
    template_name = 'investigacion/formulario_investigacion.html'
    fields = ['nombre', 'ciudad', 'pais']
    # Cambio del nombre de la URL en 'reverse_lazy'
    success_url = reverse_lazy('lista_investigacion')

class LaboratorioUpdateView(UpdateView):
    model = Laboratorio
    # Cambio del nombre del template a 'formulario_investigacion.html'
    template_name = 'investigacion/formulario_investigacion.html'
    fields = ['nombre', 'ciudad', 'pais']
    # Cambio del nombre de la URL en 'reverse_lazy'
    success_url = reverse_lazy('lista_investigacion')

class LaboratorioDeleteView(DeleteView):
    model = Laboratorio
    # Cambio del nombre del template a 'confirmacion_eliminar.html'
    template_name = 'investigacion/confirmacion_eliminar.html'
    # Cambio del nombre de la URL en 'reverse_lazy'
    success_url = reverse_lazy('lista_investigacion')
