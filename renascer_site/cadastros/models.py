from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


SIM_NAO_CHOICES = (
                    ('S', 'Sim'),
                    ('N', 'Não'),
                )
SIM_NAO_SR_CHOICES = (
                        ('S', 'Sim'),
                        ('N', 'Não'),
                        ('SR', 'Sem resposta'),
                     )


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    comunidade_fornecedora = models.CharField(max_length=100)
    turno_manha = models.BooleanField()
    turno_tarde = models.BooleanField() 
    turno_noite = models.BooleanField()
    semestres = models.PositiveIntegerField()
    professor= models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Eletrodomestico(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class MeioComunicacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class AnimalDomestico(models.Model):
    especie = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.especie


class MeioTransporte(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class GrupoComunitario(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Doenca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Familia(models.Model):
    logradouro = models.CharField(max_length=100)
    nr = models.PositiveIntegerField()
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    ponto_de_ref = models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField(max_length=8, null=True, blank=True)
    responsaveis = models.CharField(max_length=100, null=True, blank=True)
    comunidade = models.CharField(max_length=70, null=True, blank=True)
    RENDA_CHOICES = (
                        ('1SM','1 salário mínimo'),
                        ('1a2SM','1 a 2 salários mínimos'),
                        ('+2SM','Mais de 2 salários mínimos'),
                        ('SR','Sem resposta'),
                        ('DES','Desemprego'),
                    )

    renda = models.CharField(
                      max_length=5,
                      choices=RENDA_CHOICES,
                      null=True,
                      blank=True
                    )
    casa_tijolo = models.NullBooleanField(null=True, blank=True)
    casa_madeira = models.NullBooleanField(null=True, blank=True)
    casa_material_aproveitado = models.NullBooleanField(null=True, blank=True)
    
    casa_outros = models.CharField(max_length= 100,blank=True, null=True)

    CASA_TELHA_CHOICES = (
                ('TETO REVESTIDO', 'Teto revestido'),
                ('TETO NAO REVESTIDO', 'Teto sem revestimento'),

        )
    casa_telha = models.CharField(
            max_length =18,
            choices= CASA_TELHA_CHOICES,
            null=True,
            blank=True
        )
    numero_casa_comodo = models.PositiveIntegerField(null=True, blank=True)
    energia_eletrica = models.NullBooleanField(null=True, blank=True)
    DESTINO_LIXO_CHOICES = (
                     ('COLETA_PUBLICA', 'Coleta pública'),
                     ('QUEIMADO', 'Queimado'),
                     ('CEU_ABERTO', 'Céu aberto'),
                     ('ENTERRADO', 'Enterrado'),
                    )
    destino_lixo = models.CharField(
            max_length=14,
            choices= DESTINO_LIXO_CHOICES,
            null=True,
            blank=True
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
            null=True,
            blank=True
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
            null=True, 
            blank=True
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
            null=True, 
            blank=True
            )
    destino_fezes_urina_outros = models.CharField(max_length=100, null=True, blank=True)
    doencas = models.ManyToManyField(Doenca, null=True, blank=True)
    eletrodomestico = models.ManyToManyField(Eletrodomestico, through='Familia_eletrodomestico', null=True, blank=True)
    meiosComunicao = models.ManyToManyField(MeioComunicacao, through='Familia_Meiocomunicacao', null=True, blank=True)
    animaisDomesticos = models.ManyToManyField(AnimalDomestico, through='Familia_Animal', null=True, blank=True)
    guposComunitarios = models.ManyToManyField(GrupoComunitario, null=True, blank=True)
    meio_transporte = models.ManyToManyField(MeioTransporte, through='Familia_Transporte', null=True, blank=True)
    quantos_poderia_fazer_curso = models.PositiveIntegerField(null=True, blank=True)
    quantos_encaminhados = models.PositiveIntegerField(null=True, blank=True)
    tipo_encaminhamento = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.id)


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
    frequenta_escola = models.CharField(
            max_length = 2,
            choices = SIM_NAO_SR_CHOICES, null=True, blank=True
            )
    alfabetizado = models.CharField(
            max_length = 2,   
            choices = SIM_NAO_SR_CHOICES, null=True, blank=True
            )
    ocupacao=models.CharField(max_length=100, null=True, blank=True)
    funcao=models.CharField(max_length=100, null=True, blank=True)
    usa_droga=models.CharField(
            max_length = 1,
            choices = SIM_NAO_CHOICES, null=True, blank=True)
    usa_maconha=models.NullBooleanField(null=True, blank=True)
    usa_cola=models.NullBooleanField(null=True, blank=True)
    usa_alcool=models.NullBooleanField(null=True, blank=True)
    usa_cigarro=models.NullBooleanField(null=True, blank=True)
    usa_ripinol=models.NullBooleanField(null=True, blank=True)
    usa_aranha=models.NullBooleanField(null=True, blank=True)
    usa_cocaina=models.NullBooleanField(null=True, blank=True)
    usa_crack=models.NullBooleanField(null=True, blank=True)
    pertence_grupo_religioso=models.CharField(
        max_length = 1,
        choices = SIM_NAO_CHOICES, null=True, blank=True)
    religiao=models.CharField(max_length=50,null=True, blank=True)
    igreja_frequenta=models.CharField(max_length=100, null=True, blank=True)
    batizada=models.NullBooleanField(null=True, blank=True)
    crismada=models.NullBooleanField(null=True, blank=True)
    casada=models.NullBooleanField(null=True, blank=True)

    def __str__(self):
        return self.nome

class IdadeFilho(models.Model):
    idade = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.idade)

class Aluno(models.Model):
    #-----------CABEÇALHO--------------
    pessoa = models.OneToOneField(Pessoa)
    curso = models.ManyToManyField(Curso, through='Aluno_Cursa')
    #-----------DADOS PESSOAIS----------    
    apelido= models.CharField(
            max_length = 1,
            choices = SIM_NAO_CHOICES, null=True, blank=True)
    apelido_qual= models.CharField(max_length=100, null=True, blank=True)
    gosta_apelido= models.CharField(
            max_length = 1,
            choices = SIM_NAO_CHOICES, null=True, blank=True
            ) 
    tel_residencial= models.CharField(max_length=20, null=True, blank=True)
    tel_celular= models.CharField(max_length=20, null=True, blank=True)
    natural= models.CharField(max_length=100, null=True, blank=True)
    rg= models.CharField(max_length=20, null=True, blank=True)
    ESTADO_CIVIL_CHOICES = (
                     ('S', 'Solteira(o)'),
                     ('C', 'Casada(o)'),
                     ('J', 'Junta(o)'),
                   )
    estado_civil= models.CharField(
            max_length = 12,
            choices = ESTADO_CIVIL_CHOICES, 
            null=True, 
            blank=True
            )
    outro_estado_civil= models.CharField(max_length=100, null=True, blank=True)
    quantidade_filhos= models.PositiveIntegerField(null=True, blank=True)
    filho_idade = models.ManyToManyField(IdadeFilho, null=True, blank=True)
    quantidade_aborto= models.PositiveIntegerField(null=True, blank=True)
    anticoncepcional= models.CharField(max_length=70, null=True, blank=True) 
    quantidade_companheiros= models.PositiveIntegerField(null=True, blank=True)  
    nome_companheiro_atual= models.CharField(max_length=100, null=True, blank=True) 
    idade_companheiro_atual= models.PositiveIntegerField(null=True, blank=True)
    companheiro_profissao= models.CharField(
            max_length = 1,
            choices = SIM_NAO_CHOICES, null=True, blank=True
            ) 
    companheiro_ocupacao= models.CharField(max_length=100, null=True, blank=True) 
    companheiro_local_profissao= models.CharField(max_length=100, null=True, blank=True) 
    renda_companheiro= models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))]) # não obrigatório preenchimento
    obs_companheiro_profissao= models.CharField(max_length=100, null=True, blank=True)
    #----------DADOS ESCOLARES------------
    nome_da_escola= models.CharField(max_length=100, null=True, blank=True)
    serie_cursando= models.CharField(max_length=100, null=True, blank=True)
    grau_cursando= models.CharField(max_length=100, null=True, blank=True)
    TURNO_ESCOLA_CHOICES = (('M', 'Manhã'),
                            ('T', 'Tarde'),
                            ('N', 'Noite'),
                            ('I', 'Integral'),
                           )
    turno_estudando= models.CharField(
            max_length = 1,
            choices = TURNO_ESCOLA_CHOICES, null=True, blank=True)

    ultima_serie_concluida= models.CharField(max_length=100, null=True, blank=True)
    #----------SITUAÇÃO ECONÔMICA E PROFISSIONAL-------------
    atividade_remunerada = models.CharField(
            max_length = 1,
            choices = SIM_NAO_CHOICES, null=True, blank=True
            )
    atividade_nome = models.CharField(max_length= 100, null=True, blank=True)
    local_atividade = models.CharField(max_length= 100, null=True, blank=True)
    atividade_renda = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])

    #----------SITUAÇÃO FAMILIAR----------
    nome_pai= models.CharField(max_length=100, null=True, blank=True)
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
            choices = PAI_SITUACAO_CHOICES, null=True, blank=True
            ) 
    outro_situacao_pai = models.CharField(max_length=100, null=True, blank=True) 
    pai_profissao= models.CharField(max_length=100, null=True, blank=True)
    pai_renda= models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    nome_mae= models.CharField(max_length=100, null=True, blank=True)
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
            choices = MAE_SITUACAO_CHOICES,null=True, blank=True
            ) 
    outro_situacao_mae = models.CharField(null=True, blank=True, max_length=100) 
    mae_profissao= models.CharField(max_length=100, null=True, blank=True)
    mae_renda= models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    atual_responsavel= models.CharField(max_length=100, null=True, blank=True)
    saiu_de_casa = models.CharField(
            max_length= 3,
            choices= SIM_NAO_CHOICES, null=True, blank=True
            )
    idade_saiu_casa= models.PositiveIntegerField(null=True, blank=True)
    porque_saiu_casa= models.CharField(max_length=100, null=True, blank=True)
    atualmente_mora_com= models.CharField(max_length=100, null=True, blank=True)
    RESIDENCIA_SITUACAO_CHOICES= (
                                  ('PROPRIA', 'Própria'),
                                  ('ALUGADA', 'Alugada'),
                                  ('OCUPADA', 'Ocupada'),
                                  ('DOADA', 'Doada'),
                                  ('OUTRA', 'Outra'),
                                 )
    situacao_residencia=models.CharField(
            max_length= 7,
            choices= RESIDENCIA_SITUACAO_CHOICES, null=True, blank=True
            )
    situacao_residencia_outro=models.CharField(max_length=100, null=True, blank=True)
    sofre_violencia = models.CharField(
            max_length= 3,
            choices= SIM_NAO_CHOICES, null=True, blank=True
            )
    violencia_fisica=models.NullBooleanField(null=True, blank=True)
    violencia_psicologica=models.NullBooleanField(null=True, blank=True)
    violencia_sexual=models.NullBooleanField(null=True, blank=True)
    violencia_pais=models.NullBooleanField(null=True, blank=True)
    violencia_parceiros=models.NullBooleanField(null=True, blank=True)
    violencia_outros=models.NullBooleanField(null=True, blank=True)
    atividades_preferidas=models.CharField(max_length=100, null=True, blank=True)
    sonhos=models.CharField(max_length=100, null=True, blank=True)
    idade_inicial_uso_droga=models.PositiveIntegerField(null=True, blank=True)
    porque_usa_droga=models.CharField(max_length=100, null=True, blank=True)
    frequencia_droga= models.CharField(max_length=100, null=True, blank=True)
    ultima_vez_uso_droga= models.CharField(max_length=100, null=True, blank=True)
    quantidade_consumo_fumo= models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return (self.pessoa.nome)


class Aluno_Cursa(models.Model):
    aluno = models.ForeignKey(Aluno)
    curso = models.ForeignKey(Curso)
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
            choices= ANDAMENTO_CURSO_CHOICES, null=True, blank=True
        )
    porque_desistiu = models.CharField(max_length=100, null=True, blank=True)


class Visita(models.Model):
    familia = models.ForeignKey(Familia)
    data = models.DateField()
    visitante = models.CharField(max_length=100)
    SITUACAO_VISITA_CHOICES= (
                                ('CASA_FECHADA','Casa fechada'),
                                ('MUDOU-SE','Mudou-se'),
                                ('VISITADA','Visitada'),

        )
    situacao_visita= models.CharField(max_length= 12, choices= SITUACAO_VISITA_CHOICES, 
        null=True, blank=True)

    obs_visita = models.CharField(max_length=100, null=True, blank=True)
    obs_geral = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Familia_eletrodomestico(models.Model):
    familia = models.ForeignKey(Familia)
    eletrodomestico = models.ForeignKey(Eletrodomestico)
    quantidade = models.PositiveIntegerField()


class Familia_Animal(models.Model):
    familia = models.ForeignKey(Familia)
    animal_domestico = models.ForeignKey(AnimalDomestico)
    quantidade = models.PositiveIntegerField()


class Familia_Meiocomunicacao(models.Model):
    familia = models.ForeignKey(Familia)
    meioComunicacao = models.ForeignKey(MeioComunicacao)
    quantidade = models.PositiveIntegerField()


class Familia_Transporte(models.Model):
    familia = models.ForeignKey(Familia)
    transporte = models.ForeignKey(MeioTransporte)
    quantidade = models.PositiveIntegerField()
