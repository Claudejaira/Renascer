from django.conf.urls import url

from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.decorators import login_required

from .views import EletrodomesticoView
from .views import AnimalView
from .views import MeioComunicacaoView
from .views import TransporteView
from .views import GrupoComunitarioView
from .views import DoencaView
from .views import IdadeFilhoView
from .views import CursoView
from .views import FamiliaView
from .views import PessoaView
from .views import AlunoView
from .views import AlunoCursaView
from .views import VisitaView
from .views import FamiliaEletrodomesticoView
from .views import FamiliaAnimalView
from .views import FamiliaMeiocomunicacaoView
from .views import FamiliaTransporteView
from .views import home


urlpatterns = [
    url(r'^eletrodomestico/',
        EletrodomesticoView.as_view(),
        name='eletromestico'),
    url(r'^eletrodomestico/list',
        EletrodomesticoView.as_view(),
        name='eletrodomestico_list'),

    url(r'^animal/',
        AnimalView.as_view(),
        name='animal'),
    url(r'^animal/list',
        AnimalView.as_view(),
        name='animal_list'),

    url(r'^meiocomunicacao/',
        MeioComunicacaoView.as_view(),
        name='meiocomunicacao'),
    url(r'^meiocomunicacao/list',
        MeioComunicacaoView.as_view(),
        name='animal_list'),

    url(r'^meiotransporte/',
        TransporteView.as_view(),
        name='meiotransporte'),
    url(r'^meiotransporte/list',
        TransporteView.as_view(),
        name='meiotransporte_list'),

    url(r'^grupocomunitario/',
        GrupoComunitarioView.as_view(),
        name='grupocomunitario'),
    url(r'^grupocomunitario/list',
        GrupoComunitarioView.as_view(),
        name='grupocomunitario_list'),

    url(r'^doenca/',
        DoencaView.as_view(),
        name='doenca'),
    url(r'^doenca/list',
        DoencaView.as_view(),
        name='doenca_list'),

    url(r'^idadefilho/',
        IdadeFilhoView.as_view(),
        name='idadefilho'),
    url(r'^idadefilho/list',
        IdadeFilhoView.as_view(),
        name='idadefilho_list'),

    url(r'^curso/',
        login_required(CursoView.as_view()),
        name='curso'),
    url(r'^curso/list',
        CursoView.as_view(),
        name='curso_list'),

    url(r'^familia/',
        FamiliaView.as_view(),
        name='familia'),
    url(r'^familia/list',
        FamiliaView.as_view(),
        name='familia_list'),

    url(r'^pessoa/',
        PessoaView.as_view(),
        name='pessoa'),
    url(r'^pessoa/list',
        PessoaView.as_view(),
        name='pessoa_list'),

    url(r'^aluno/',
        login_required(AlunoView.as_view()),
        name='aluno'),
    url(r'^aluno/list',
        AlunoView.as_view(),
        name='aluno_list'),

    url(r'^alunocursa/',
        AlunoCursaView.as_view(),
        name='alunocursa'),
    url(r'^alunocursa/list',
        AlunoCursaView.as_view(),
        name='alunocursa_list'),

    url(r'^visita/',
        login_required(VisitaView.as_view()),
        name='visita'),
    url(r'^visita/list',
        VisitaView.as_view(),
        name='visita_list'),

    url(r'^familiaeletrodomestico/',
        FamiliaEletrodomesticoView.as_view(),
        name='familiaeletrodomestico'),
    url(r'^familiaeletrodomestico/list',
        FamiliaEletrodomesticoView.as_view(),
        name='familiaeletrodomestico_list'),

    url(r'^familiaanimal/',
        FamiliaAnimalView.as_view(),
        name='familiaanimal'),
    url(r'^familiaanimal/list',
        FamiliaAnimalView.as_view(),
        name='familiaanimal_list'),

    url(r'^familiameiocomunicacao/',
        FamiliaMeiocomunicacaoView.as_view(),
        name='familiameiocomunicacao'),
    url(r'^familiameiocomunicacao/list',
        FamiliaMeiocomunicacaoView.as_view(),
        name='familiameiocomunicacao_list'),

    url(r'^familiatransporte/',
        FamiliaTransporteView.as_view(),
        name='familiatransporte'),
    url(r'^familiatransporte/list',
        FamiliaTransporteView.as_view(),
        name='familiatransporte_list'),

    # post views
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^logout-then-login/$', logout_then_login,
        name='logout_then_login'),

    url(r'^$', home, name='home'),

]
