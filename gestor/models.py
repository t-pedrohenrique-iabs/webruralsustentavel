#_x -- coding: utf8 --
# vim: set fileencoding=utf8 :
from django.db import models
import datetime

class Noticias(models.Model):
    key_new = models.IntegerField(null=True, blank=True, verbose_name=u"Chave da noticia")
    data_create = models.CharField(max_length=500, blank=True, null=True, verbose_name=u"Data da noticia")
    data_post = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name=u"Data da noticia post")
    titulo = models.CharField(max_length=500, blank=True, null=True, verbose_name=u"Titulo")
    chamada = models.CharField(max_length=500, blank=True, null=True, verbose_name=u"Chamada")
    conteudo = models.TextField(max_length=5000, blank=True, null=True, verbose_name=u"Conteudo")
    image_link = models.CharField(max_length=500, blank=True, null=True, verbose_name=u"Link da imagem")
    estado = models.CharField(max_length=500, blank=True, null=True, verbose_name=u"Estado da materia")
    destaque = models.CharField(max_length=500, blank=True, null=True, verbose_name=u"Destaque")

class MetasGerais(models.Model):
    unidade_demonstrativa  = models.IntegerField(blank=True, null=True, verbose_name=u"Unidade Demonstrativa")
    unidade_multiplicadora = models.IntegerField(blank=True, null=True, verbose_name=u"Unidade Multiplicadora")
    dia_campo              = models.IntegerField(blank=True, null=True, verbose_name=u"Dia de Campo")
    produtores_capacitados = models.IntegerField(blank=True, null=True, verbose_name=u"Produtores Capacitados")
    atecs_treinados        = models.IntegerField(blank=True, null=True, verbose_name=u"ATECs Treinados")

class MetasPA(models.Model):
    unidade_demonstrativa  = models.IntegerField(blank=True, null=True, verbose_name=u"Unidade Demonstrativa")
    unidade_multiplicadora = models.IntegerField(blank=True, null=True, verbose_name=u"Unidade Multiplicadora")
    dia_campo              = models.IntegerField(blank=True, null=True, verbose_name=u"Dia de Campo")
    produtores_capacitados = models.IntegerField(blank=True, null=True, verbose_name=u"Produtores Capacitados")
    atecs_treinados        = models.IntegerField(blank=True, null=True, verbose_name=u"ATECs Treinados")

class MetasMT(models.Model):
    unidade_demonstrativa  = models.IntegerField(blank=True, null=True, verbose_name=u"Unidade Demonstrativa")
    unidade_multiplicadora = models.IntegerField(blank=True, null=True, verbose_name=u"Unidade Multiplicadora")
    dia_campo              = models.IntegerField(blank=True, null=True, verbose_name=u"Dia de Campo")
    produtores_capacitados = models.IntegerField(blank=True, null=True, verbose_name=u"Produtores Capacitados")
    atecs_treinados        = models.IntegerField(blank=True, null=True, verbose_name=u"ATECs Treinados")

class MetasRO(models.Model):
    unidade_demonstrativa  = models.IntegerField(blank=True, null=True, verbose_name=u"Unidade Demonstrativa")
    unidade_multiplicadora = models.IntegerField(blank=True, null=True, verbose_name=u"Unidade Multiplicadora")
    dia_campo              = models.IntegerField(blank=True, null=True, verbose_name=u"Dia de Campo")
    produtores_capacitados = models.IntegerField(blank=True, null=True, verbose_name=u"Produtores Capacitados")
    atecs_treinados        = models.IntegerField(blank=True, null=True, verbose_name=u"ATECs Treinados")

class MetasBA(models.Model):
    unidade_demonstrativa  = models.IntegerField(blank=True, null=True, verbose_name=u"Unidade Demonstrativa")
    unidade_multiplicadora = models.IntegerField(blank=True, null=True, verbose_name=u"Unidade Multiplicadora")
    dia_campo              = models.IntegerField(blank=True, null=True, verbose_name=u"Dia de Campo")
    produtores_capacitados = models.IntegerField(blank=True, null=True, verbose_name=u"Produtores Capacitados")
    atecs_treinados        = models.IntegerField(blank=True, null=True, verbose_name=u"ATECs Treinados")

class MetasMG(models.Model):
    unidade_demonstrativa  = models.IntegerField(blank=True, null=True, verbose_name=u"Unidade Demonstrativa")
    unidade_multiplicadora = models.IntegerField(blank=True, null=True, verbose_name=u"Unidade Multiplicadora")
    dia_campo              = models.IntegerField(blank=True, null=True, verbose_name=u"Dia de Campo")
    produtores_capacitados = models.IntegerField(blank=True, null=True, verbose_name=u"Produtores Capacitados")
    atecs_treinados        = models.IntegerField(blank=True, null=True, verbose_name=u"ATECs Treinados")

class MetasPR(models.Model):
    unidade_demonstrativa  = models.IntegerField(blank=True, null=True, verbose_name=u"Unidade Demonstrativa")
    unidade_multiplicadora = models.IntegerField(blank=True, null=True, verbose_name=u"Unidade Multiplicadora")
    dia_campo              = models.IntegerField(blank=True, null=True, verbose_name=u"Dia de Campo")
    produtores_capacitados = models.IntegerField(blank=True, null=True, verbose_name=u"Produtores Capacitados")
    atecs_treinados        = models.IntegerField(blank=True, null=True, verbose_name=u"ATECs Treinados")

class MetasRS(models.Model):
    unidade_demonstrativa  = models.IntegerField(blank=True, null=True, verbose_name=u"Unidade Demonstrativa")
    unidade_multiplicadora = models.IntegerField(blank=True, null=True, verbose_name=u"Unidade Multiplicadora")
    dia_campo              = models.IntegerField(blank=True, null=True, verbose_name=u"Dia de Campo")
    produtores_capacitados = models.IntegerField(blank=True, null=True, verbose_name=u"Produtores Capacitados")
    atecs_treinados        = models.IntegerField(blank=True, null=True, verbose_name=u"ATECs Treinados")


class NoticiasProjeto(models.Model):
    CHOICES_ESTADO = (
        ("PA" , "Pará"),
        ("MT" , "Mato Grosso"),
        ("RO" , "Rondônia"),
        ("RS" , "Rio Grande do Sul"),
        ("BA" , "Bahia"),
        ("PR" , "Paraná"),
        ("MG" , "Minas Gerais"),
        ("DF" , "Brasília")
    )

    show_home       = models.NullBooleanField(default=False, null=True, blank=True)
    titulo          = models.CharField(max_length=500, blank=True, null=False, verbose_name=u"Título da notícia")
    chamada         = models.CharField(max_length=500, blank=True, null=False, verbose_name=u"Chamada da notícia")
    data_criacao    = models.DateTimeField(auto_now_add=True)
    data_publicacao = models.DateField(default=datetime.date.today, verbose_name=u"Data da publicação")
    img_noticia     = models.CharField(max_length=1000,   blank=True, null=False, verbose_name=u"Imagem da notícias")
    img_credito     = models.CharField(max_length=1000,   blank=True, null=False, verbose_name=u"Creditos da imagens")
    album_one       = models.CharField(max_length=1000,   blank=True, null=False, verbose_name=u"Álbum imagem")
    album_two       = models.CharField(max_length=1000,   blank=True, null=False, verbose_name=u"Álbum imagem")
    album_three     = models.CharField(max_length=1000,   blank=True, null=False, verbose_name=u"Álbum imagem")
    album_four      = models.CharField(max_length=1000,   blank=True, null=False, verbose_name=u"Álbum imagem")
    album_five      = models.CharField(max_length=1000,   blank=True, null=False, verbose_name=u"Álbum imagem")
    album_six       = models.CharField(max_length=1000,   blank=True, null=False, verbose_name=u"Álbum imagem")
    conteudo        = models.TextField(max_length=10000,  blank=True, null=False, verbose_name=u"Conteúdo da notícias")
    video           = models.CharField(max_length=1000,   blank=True, null=False, verbose_name=u"Vídeo")
    video_descricao = models.CharField(max_length=1000,   blank=True, null=False, verbose_name=u"Descrição do vídeo")
    estado          = models.CharField(max_length=150,    blank=True, null=True, choices=CHOICES_ESTADO, default='DF', verbose_name=u"Estado")


class newsletter(models.Model):
    incluido         = models.NullBooleanField(default=False, null=True, blank=True)
    nome_user        = models.CharField(max_length=500, blank=True, null=False, verbose_name=u"Título da notícia")
    email_user       = models.CharField(max_length=500, blank=True, null=False, verbose_name=u"Chamada da notícia")
    data_solicitacao = models.DateTimeField(auto_now_add=True)


class Depoimentos(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    titulo      = models.CharField(max_length=1000, blank=True, null=True, verbose_name=u"Titulo")
    descricao   = models.TextField(max_length=3000, blank=True, null=True, verbose_name=u"Conteudo")
    embed_link  = models.CharField(max_length=2000, blank=True, null=True, verbose_name=u"Link do Embrad do video")
    link_img    = models.CharField(max_length=2000, blank=True, null=True, verbose_name=u"Link da imagem")
