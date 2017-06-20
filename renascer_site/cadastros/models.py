from django.db import models

# Create your models here.

# Pessoa herda de models.Model


class Curso(models.Model):
	nome= models.CharField(max_length=100)
	comunidade_fornecedora= models.CharField(max_length=100)
	turno_manha= models.BooleanField()
	turno_tarde= models.BooleanField() 
	turno_noite= models.BooleanField()
	semestres= models.IntegerField()
	professor= models.CharField(max_length=100)


class Eletrodomestico(models.Model):
	nome = models.CharField(max_length=100)


class MeioComunicacao(models.Model):
	nome = models.CharField(max_length= 100)


class AnimalDomestico(models.Model):
	cao = models.BooleanField()  #quando a caixa for marcada aparecerá um campo para a quantidade
	quantidade_cao = models.IntegerField()
	gato = models.BooleanField()
	quantidade_gato = models.IntegerField()
	outros_animais = models.CharField(max_length=100) #pedir quantidade de cada espécie



class MeioTransporte(models.Model):
	nome = models.CharField(max_length= 50)


class GrupoComunitario(models.Model):
	nome = models.CharField(max_length=100)


class Doenca(models.Model):
	nome = models.CharField(max_length=50)


class Familia(models.Model):
	
	logradouro= models.CharField(max_length=100)
	nr= models.IntegerField()
	bairro= models.CharField(max_length=100)
	cidade=models.CharField(max_length=100)
	estado= models.CharField(max_length=100)
	ponto_de_ref= models.CharField(max_length=100)
	cep= models.CharField(max_length=8)
	responsaveis = models.CharField(max_length=100)
	comunidade = models.CharField(max_length=70)
	renda = models.DecimalField(max_digits=8 , decimal_places=2)
	casa_tijolo = models.BooleanField()
	casa_telha_revestida = models.BooleanField()
	casa_telha_nao_revestida = models.BooleanField()
	casa_madeira = models.BooleanField()
	casa_material_aproveitado = models.BooleanField()
	casa_outros = models.BooleanField()
	numero_casa_comodo = models.IntegerField()
	energia_eletrica = models.BooleanField()
	DESTINO_LIXO_CHOICES = (
					 ('COLETA_PUBLICA', 'Coleta pública'),
					 ('QUEIMADO', 'Queimado'),
					 ('CEU_ABERTO', 'Céu aberto'),
					 ('ENTERRADO', 'Enterrado'),
					)
	destino_lixo = models.CharField(
			max_length=14,
			choices= DESTINO_LIXO_CHOICES,
			) 
	TRATAMENTO_AGUA_CHOICES = (
								('FILTRADA', 'Filtrada'),
								('FERVIDA', 'Fervida'),
								('CLORADA', 'Clorada'),
								('SEM_TRATAMENTO', 'Sem tratamento'),
							  )
	tratamento_agua = models.CharField(
			max_length=14,
			choices= TRATAMENTO_AGUA_CHOICES,
			) 
	ABASTECIMENTO_AGUA_CHOICES = (
						  ('CAGECE', 'Cagece'),
						  ('BOMBA', 'Bomba'),
						  ('CHAFARIZ', 'Chafariz'),
						  ('CACIMBA', 'Cacimba'),
						 )
	abastecimento_agua = models.CharField(
			max_length= 8,
			choices= ABASTECIMENTO_AGUA_CHOICES,
			) 
	DESTINO_FEZES_URINA_CHOICES = (
									('FOSSA', 'Fossa séptica'),
									('CEU_ABERTO', 'Céu aberto'),
									('ESGOTO', 'Esgoto'),
									('OUTROS', 'Outros'),
								  )
	destino_fezes_urina = models.CharField(
			max_length= 10,
			choices= DESTINO_FEZES_URINA_CHOICES,
			)
	doencas = models.ManyToManyField(Doenca)
	eletrodomestico = models.ManyToManyField(Eletrodomestico)
	meiosComunicao = models.ManyToManyField(MeioComunicacao)
	animaisDomesticos = models.ManyToManyField(AnimalDomestico)
	guposComunitarios = models.ManyToManyField(GrupoComunitario)
	meio_transporte = models.ManyToManyField(MeioTransporte)
	doencas_outras = models.CharField(max_length= 100, null=True)
	eletrodomestico_outros = models.CharField(max_length=100, null=True)
	meios_comunicacao_outros = models.CharField(max_length= 100, null=True)
	animais_domestico_outros = models.CharField(max_length=100, null=True)
	grupos_comunitarios_outros = models.CharField(max_length= 100, null=True)
	meio_transporte_outros = models.CharField(max_length= 100, null=True)
	batizada = models.BooleanField()
	crismada = models.BooleanField()
	casada = models.BooleanField()
	religiao_familia = models.CharField(max_length=100)
	quantos_poderia_fazer_curso = models.IntegerField()
	quantos_encaminhados = models.IntegerField()
	tipo_encaminhamento = models.CharField(max_length=100)



class Pessoa(models.Model):
	familia = models.ForeignKey(Familia)
	nome = models.CharField(max_length=100)
	SEXO_CHOICES = (
					('F', 'Feminino'),
					('M', 'Masculino'),
				   )
	sexo= models.CharField(
		max_length =1,
		choices = SEXO_CHOICES,
		)
	data_nascimento = models.DateField()
	FREQUENTA_ESCOLA_CHOICES = (
								('S', 'Sim'),
								('N', 'Não'),
								('SR', 'Sem resposta'),
							)
	frequenta_escola = models.CharField(
			max_length = 2,
			choices = FREQUENTA_ESCOLA_CHOICES,
			)
	ocupacao=models.CharField(max_length=100)
	funcao=models.CharField(max_length=100)
	
	USA_DROGAS_CHOICES = (
						 		('S', 'Sim'),
								('N', 'Não'),
						 )
	usa_droga=models.CharField(
			max_length = 1,
			choices = USA_DROGAS_CHOICES,
		)
	usa_maconha=models.BooleanField()
	usa_cola=models.BooleanField()
	usa_alcool=models.BooleanField()
	usa_cigarro=models.BooleanField()
	usa_ripinol=models.BooleanField()
	usa_aranha=models.BooleanField()
	usa_cocaina=models.BooleanField()
	usa_crack=models.BooleanField()
	encaminhado= models.IntegerField()


class Aluno(models.Model):
	#-----------CABEÇALHO--------------
	pessoa = models.OneToOneField(Pessoa)
	curso = models.ManyToManyField(Curso)
	data_inscricao = models.DateField()
	CURSO_TURNO_CHOICES = (
							('M', 'Manhã'),
							('T', 'Tarde'),
							('N', 'Noite'),
						  )
	curso_turno = models.CharField(
			max_length = 1,
			choices = CURSO_TURNO_CHOICES,
			)

	ANDAMENTO_CURSO_CHOICES = (
								('FREQUENTA','Frequenta'),
								('DESISTIU', 'Desistiu'),
							  )
	andamento_curso= models.CharField(
			max_length= 9,
			choices= ANDAMENTO_CURSO_CHOICES,
		)
	porque_desistiu = models.CharField(max_length=100)

	#-----------DADOS PESSOAIS----------
	TEM_APELIDO_CHOICES = (
							('S', 'Sim'),
							('N', 'Não'),
						  )
	apelido= models.CharField(
			max_length = 1,
			choices = TEM_APELIDO_CHOICES,
			)
	apelido_qual= models.CharField(max_length=100)

	GOSTA_APELIDO_CHOICES = (
							  ('S', 'Sim'),
							  ('N', 'Não'),
							)
	gosta_apelido= models.CharField(
			max_length = 1,
			choices = GOSTA_APELIDO_CHOICES,
			) 
	tel_residencial= models.CharField(max_length=20, null=True) # não obrigatório preenchimento
	tel_celular= models.CharField(max_length=20, null=True) # não obrigatório preenchimento
	natural= models.CharField(max_length=100, null=True) # não obrigatório preenchimento
	rg= models.CharField(max_length=20)
	ESTADO_CIVIL_CHOICES = (
					 ('S', 'Solteira(o)'),
					 ('C', 'Casada(o)'),
					 ('J', 'Junta(o)'),
				   )
	estado_civil= models.CharField(
			max_length = 12,
			choices = ESTADO_CIVIL_CHOICES,
			)
	outro_estado_civil= models.CharField(max_length=100, null=True) # não obrigatório preenchimento
	quantidade_filhos= models.IntegerField(null=True) # não obrigatório preenchimento
	quantidade_aborto= models.IntegerField(null=True) # não obrigatório preenchimento
	anticoncepcional= models.CharField(max_length=70, null=True) # não obrigatório preenchimento
	quantidade_companheiros= models.IntegerField(null=True) # não obrigatório preenchimento 
	nome_companheiro_atual= models.CharField(max_length=100, null=True) # não obrigatório preenchimento
	idade_companheiro_atual= models.IntegerField(null=True) # não obrigatório preenchimento
	COMPANHEIRO_TRABALHA_CHOICES =(
									('S', 'Sim'),
							  		('N', 'Não'),
								  ) 
	companheiro_profissao= models.CharField(
			max_length = 1,
			choices = COMPANHEIRO_TRABALHA_CHOICES, null=True
			) # não obrigatório preenchimento
	companheiro_ocupacao= models.CharField(max_length=100, null=True) # não obrigatório preenchimento
	companheiro_local_profissao= models.CharField(max_length=100, null=True) # não obrigatório preenchimento
	renda_companheiro= models.DecimalField(null=True, max_digits=8, decimal_places=2) # não obrigatório preenchimento
	obs_companheiro_profissao= models.CharField(max_length=100, null=True)

	#----------DADOS ESCOLARES------------
	serie_cursando= models.IntegerField(null=True)
	grau_cursando= models.CharField(max_length=100, null=True)
	TURNO_ESCOLA_CHOICES = (('M', 'Manhã'),
							('T', 'Tarde'),
							('N', 'Noite'),
							('I', 'Integral'),
						   )
	turno_estudando= models.CharField(
			max_length = 1,
			choices = TURNO_ESCOLA_CHOICES, null=True
			) 
	ultima_serie_concluida= models.IntegerField(null=True)

	#----------SITUAÇÃO ECONÔMICA E PROFISSIONAL-------------
	ATIVIDADE_REMUNERADA_CHOICES = (
									('S', 'Sim'),
							  		('N', 'Não'),
								   )

	atividade_remunerada = models.CharField(
			max_length = 1,
			choices = ATIVIDADE_REMUNERADA_CHOICES,
			)
	atividade_nome = models.CharField(max_length= 100, null=True)
	local_atividade = models.CharField(max_length= 100, null=True)
	atividade_renda = models.DecimalField(null=True, max_digits=8, decimal_places=2)

	#----------SITUAÇÃO FAMILIAR----------
	nome_pai= models.CharField(max_length=100, null=True)
	PAI_SITUACAO_CHOICES = (
					 ('PRESENTE', 'Presente'),
					 ('FALECIDO', 'Falecido'),
					 ('DESCONHECIDO', 'Desconhecido'),
					 ('ADOTIVO', 'Adotivo'),
					 ('SEPARADO', 'Separado'),
					 ('NOVAFAMILIA', 'Nova família'),
					 ('ABANDONO', 'Abandono'),
					 ('OUTROS', 'Outros'),
				   )
	pai_situacao= models.CharField(
			max_length = 12,
			choices = PAI_SITUACAO_CHOICES,
			) 
	outro_situacao_pai = models.CharField(null=True, max_length=100) 
	pai_profissao= models.CharField(max_length=100, null=True)
	pai_renda= models.DecimalField(null=True, max_digits=8, decimal_places=2)
	nome_mae= models.CharField(max_length=100, null=True)
	MAE_SITUACAO_CHOICES= (
							('PRESENTE', 'Presente'),
					 		('FALECIDA', 'Falecida'),
							('DESCONHECIDA', 'Desconhecida'),
							('ADOTIVA', 'Adotiva'),
							('SEPARADA', 'Separada'),
							('NOVAFAMILIA', 'Nova família'),
							('ABANDONO', 'Abandono'),
							('OUTROS', 'Outros'),
						  )
	mae_situacao= models.CharField(
			max_length = 12,
			choices = MAE_SITUACAO_CHOICES,
			) 
	outro_situacao_mae = models.CharField(null=True, max_length=100) 
	mae_profissao= models.CharField(max_length=100, null=True)
	mae_renda= models.DecimalField(null=True, max_digits=8, decimal_places=2)
	atual_responsavel= models.CharField(max_length=100)
	idade_saiu_casa= models.IntegerField(null=True)
	porque_saiu_casa= models.CharField(max_length=100, null=True)
	atualmente_mora_com= models.CharField(max_length=100, null=True)
	RESIDENCIA_SITUACAO_CHOICES= (
								  ('PROPRIA', 'Própria'),
								  ('ALUGADA', 'Alugada'),
								  ('OCUPADA', 'Ocupada'),
								  ('DOADA', 'Doada'),
								  ('OUTRA', 'Outra'),
								 )
	situacao_residencia=models.CharField(
			max_length= 7,
			choices= RESIDENCIA_SITUACAO_CHOICES,
			)
	situacao_residencia_outro=models.CharField(max_length=100, null=True)
	violencia_fisica=models.BooleanField()
	violencia_psicologica=models.BooleanField()
	violencia_sexual=models.BooleanField()
	violencia_pais=models.BooleanField()
	violencia_parceiros=models.BooleanField()
	violencia_outros=models.BooleanField()

	#----------SITUAÇÃO SOCIAL/RELIGIOSA/SAÚDE-----------------
	GRUPO_RELIGIOSO_CHOICES = (
							   ('S', 'Sim'),
							   ('N', 'Não'),
							  )

	pertence_grupo_religioso=models.CharField(
		max_length = 1,
		choices = GRUPO_RELIGIOSO_CHOICES,
		)
	atividades_preferidas=models.CharField(max_length=100)
	sonhos=models.CharField(max_length=100)
	religiao=models.CharField(max_length=50)
	igreja_frequenta=models.CharField(max_length=100)
	batizada=models.BooleanField()
	crismada=models.BooleanField()
	casada=models.BooleanField()
	idade_inicial_uso_droga=models.IntegerField()
	porque_usa_droga=models.CharField(max_length=100)
	frequencia_droga= models.CharField(max_length=100)
	ultima_vez_uso_droga= models.CharField(max_length=100)
	quantidade_consumo_fumo= models.CharField(max_length=100)


class IdadeFilho(models.Model):
	idade_filhos = models.ForeignKey(Aluno) 
	idade = models.IntegerField()


class Visita(models.Model):
	familia = models.ForeignKey(Familia)
	id_registro_visita = models.CharField(max_length=100)
	id_registro_geral = models.CharField(max_length=10)
	data = models.DateField()
	visitante = models.CharField(max_length=100)
	STATUS_CASA_CHOICES = (
							('CASA_FECHADA', 'Casa fechada'),
							('MUDOU', 'Mudou-se'),
						  )
	status_casa = models.CharField(
			max_length= 12,
			choices= STATUS_CASA_CHOICES,null=True
			)
	obs_visita = models.CharField(max_length=100)
	obs_geral = models.CharField(max_length=100)





"""
class Moradores:
	pass


class Drogas: 
	pass
"""
