from django.forms import ModelForm
from .models import Eletrodomestico
from .models import AnimalDomestico
from .models import MeioComunicacao
from .models import MeioTransporte
from .models import GrupoComunitario
from .models import Doenca
from .models import IdadeFilho
from .models import Curso
from .models import Familia
from .models import Pessoa
from .models import Aluno
from .models import Aluno_Cursa
from .models import Visita
from .models import Familia_eletrodomestico
from .models import Familia_Animal
from .models import Familia_Meiocomunicacao
from .models import Familia_Transporte


class EletrodomesticoForm(ModelForm):
    class Meta:
        model = Eletrodomestico
        fields = ("nome", )


class AnimalForm(ModelForm):
	class Meta:
		model = AnimalDomestico
		fields = ("especie", ) 


class MeioComunicacaoForm(ModelForm):
    class Meta:
        model = MeioComunicacao
        fields = ("nome",)

    
class TransporteForm(ModelForm):
	class Meta:
		model = MeioTransporte
		fields = ("nome",)


class GrupoComunitarioForm(ModelForm):
	class Meta:
		model = GrupoComunitario
		fields = ("nome",)


class DoencaForm(ModelForm):
	class Meta:
		model = Doenca
		fields = ("nome",)


class IdadeFilhoForm(ModelForm):
	class Meta:
		model = IdadeFilho
		fields = ("idade", )


class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

   
class FamiliaForm(ModelForm):
    class Meta:
        model = Familia
        fields = '__all__'


class PessoaForm(ModelForm):
	class Meta:
		model = Pessoa
		fields = '__all__'


class AlunoForm(ModelForm):
	class Meta:
		model = Aluno
		fields = '__all__'


class AlunoCursaForm(ModelForm):
	class Meta:
		model = Aluno_Cursa
		fields = '__all__'


class VisitaForm(ModelForm):
	class Meta:
		model = Visita
		fields ='__all__'


class FamiliaEletrodomesticoForm(ModelForm):
	class Meta:
		model = Familia_eletrodomestico
		fields ='__all__'


class FamiliaAnimalForm(ModelForm):
	class Meta:
		model = Familia_Animal
		fields ='__all__'


class FamiliaMeiocomunicacaoForm(ModelForm):
	class Meta:
		model = Familia_Meiocomunicacao
		fields ='__all__'


class FamiliaTransporteForm(ModelForm):
	class Meta:
		model = Familia_Transporte
		fields ='__all__'

