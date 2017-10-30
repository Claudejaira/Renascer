from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View

from .forms import EletrodomesticoForm
from .forms import AnimalForm
from .forms import MeioComunicacaoForm
from .forms import TransporteForm
from .forms import GrupoComunitarioForm
from .forms import DoencaForm
from .forms import IdadeFilhoForm
from .forms import CursoForm
from .forms import FamiliaForm
from .forms import PessoaForm
from .forms import AlunoForm
from .forms import AlunoCursaForm
from .forms import VisitaForm
from .forms import FamiliaEletrodomesticoForm
from .forms import FamiliaAnimalForm
from .forms import FamiliaMeiocomunicacaoForm
from .forms import FamiliaTransporteForm


class EletrodomesticoView(View):
    def get(self, request, *args, **kwargs):
        form = EletrodomesticoForm()
        return render(request,
                      'cadastros/eletrodomestico.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = EletrodomesticoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})


class AnimalView(View):
    def get(self, request, *args, **kwargs):
        form = AnimalForm()
        return render(request,
                      'cadastros/animal.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})


class MeioComunicacaoView(View):
    def get(self, request, *args, **kwargs):
        form = MeioComunicacaoForm()
        return render(
            request,
            'cadastros/meiocomunicacao.html',
            {'form': form})

    def post(self, request, *args, **kwargs):
        form = MeioComunicacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})


class TransporteView(View):

    def get(self, request, *args, **kwargs):
        form = TransporteForm()
        return render(request,
                      'cadastros/meiotransporte.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TransporteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})


class GrupoComunitarioView(View):
    def get(self, request, *args, **kwargs):
        form = GrupoComunitarioForm()
        return render(request,
                      'cadastros/grupocomunitario.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = GrupoComunitarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})


class DoencaView(View):
    def get(self, request, *args, **kwargs):
        form = DoencaForm()
        return render(request,
                      'cadastros/doenca.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = DoencaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
        return render(request, self.template_name, {'form': form})


class IdadeFilhoView(View):
    def get(self, request, *args, **kwargs):
        form = IdadeFilhoForm()
        return render(request,
                      'cadastros/idadefilho.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = IdadeFilhoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})


class CursoView(View):
    def get(self, request, *args, **kwargs):
        form = CursoForm()
        return render(request,
                      'cadastros/curso.html', 
                      {'form': form, 'section': 'curso'})

    def post(self, request, *args, **kwargs):
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
        return render(request, 'cadastros/curso.html',
            {'form': form, 'section': 'curso'})


class FamiliaView(View):
    def get(self, request, *args, **kwargs):
        form = FamiliaForm()
        return render(request,
                      'cadastros/familia.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = FamiliaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
        return render(request, 'cadastros/familia.html', {'form': form})


class PessoaView(View):
    def get(self, request, *args, **kwargs):
        form = PessoaForm()
        return render(request,
                      'cadastros/pessoa.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
        return render(request, 'cadastros/pessoa.html', {'form': form})


class AlunoView(View):
    def get(self, request, *args, **kwargs):
        form = AlunoForm()
        return render(request,
                      'cadastros/aluno.html',
                      {'form': form, 'section': 'aluno'})

    def post(self, request, *args, **kwargs):
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
        return render(
            request,
            'cadastros/aluno.html',
            {'form': form, 'section': 'aluno'}
        )


class AlunoCursaView(View):
    def get(self, request, *args, **kwargs):
        form = AlunoCursaForm()
        return render(request,
                      'cadastros/alunocursa.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AlunoCursaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')

        return render(request, 'cadastros/alunocursa.html', {'form': form})


class VisitaView(View):
    def get(self, request, *args, **kwargs):
        form = VisitaForm()
        return render(request,
                      'cadastros/visita.html',
                       {'form': form, 'section': 'visita'})

    def post(self, request, *args, **kwargs):
        form = VisitaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')

        return render(request, 'cadastros/visita.html', 
            {'form': form, 'section': 'visita'})


class FamiliaEletrodomesticoView(View):
    def get(self, request, *args, **kwargs):
        form = FamiliaEletrodomesticoForm()
        return render(request,
                      'cadastros/familiaeletrodomestico.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = FamiliaEletrodomesticoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')

        return render(request,
                      'cadastros/familiaeletrodomestico.html', {'form': form})


class FamiliaAnimalView(View):
    def get(self, request, *args, **kwargs):
        form = FamiliaAnimalForm()
        return render(request,
                      'cadastros/familiaanimal.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = FamiliaAnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')

        return render(request,
                      'cadastros/familiaanimal.html', {'form': form})


class FamiliaMeiocomunicacaoView(View):
    def get(self, request, *args, **kwargs):
        form = FamiliaMeiocomunicacaoForm()
        return render(request,
                      'cadastros/familiameiocomunicacao.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = FamiliaMeiocomunicacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')

        return render(request, 'cadastros/familiameiocomunicacao.html',
                      {'form': form})


class FamiliaTransporteView(View):
    def get(self, request, *args, **kwargs):
        form = FamiliaTransporteForm()
        return render(request,
                      'cadastros/familiatransporte.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = FamiliaTransporteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')

        return render(request, 'cadastros/familiatransporte.html',
                      {'form': form})


@login_required
def home(request):
    return render(
        request,
        'cadastros/home.html',
        {'section': 'home'}
    )
