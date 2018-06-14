from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='web_home'),
    url(r'^tecnologias/$', views.tecnologias, name='web_tecnologias'),
    url(r'^participe/$', views.participe, name='web_participe'),
    url(r'^resultados_alcancados/$', views.resultados_alcancados, name='resultados_alcancados'),

    url(r'^destaque/$', views.destaque, name='web_destaque'),
    url(r'^destaque/(?P<chave>[-\w\d]+)/$', views.materia, name='web_materia'),
    url(r'^materia/ajax_materia/$', views.ajax_materia, name='web_ajax_materia'),

    url(r'^downloads/$', views.downloads, name='web_downloads'),
    url(r'^sobre/$', views.sobre, name='web_sobre'),
    url(r'^projetoAcoes/$', views.projetoAcoes, name='web_projetoAcoes'),
    url(r'^beneficiario/$', views.beneficiario, name='web_beneficiario'),
    url(r'^instituicao_aprovada/$', views.instituicao_aprovada, name='web_instituicao_aprovada'),

    url(r'^flipbook_doctec_gestao/$', views.flipbook_doctec_gestao, name='web_flipbook_doctec_gestao'),
    url(r'^flipbook_doctec_ilpf/$', views.flipbook_doctec_ilpf, name='web_flipbook_doctec_ilpf'),
    url(r'^flipbook_doctec_rad/$', views.flipbook_doctec_rad, name='web_flipbook_doctec_rad'),
    url(r'^flipbook_doctec_pfc/$', views.flipbook_doctec_pfc, name='web_flipbook_doctec_pfc'),
    url(r'^flipbook_doctec_msfn/$', views.flipbook_doctec_msfn, name='web_flipbook_doctec_msfn'),

    url(r'^informativo/(?P<informativo_flipbook>[-\w\d]+)$', views.informativo_flipbook, name='informativo_flipbook'),

    url(r'^infografico/(?P<infografico>[-\w\d]+)$', views.infografico, name='infografico'),

    url(r'^noticia/(?P<noticia_id>[-\w\d]+)/prs$', views.visualizar_noticia, name='visualizar_noticia'),
    url(r'^destaques/$', views.destaques_lista, name='destaques_lista'),

    url(r'^depoimento/(?P<id_depoimento>[-\w\d]+)/video$', views.video_depoimento, name='video_depoimento'),

    url(r'^videos/(?P<ator>[-\w\d]+)/depoimento$', views.depoimento, name='web_depoimento'),
    url(r'^chamadapiloto/$', views.chamadapiloto, name='web_chamadapiloto'),
    url(r'^chamadaud/$', views.chamadaud, name='web_chamadaud'),
    url(r'^chamada_direcionada/$', views.chamada_direcionada, name='web_chamada_direcionada'),
    url(r'^chamada_um/$', views.chamada_um, name='web_chamada_um'),
    url(r'^mudas_insumos/$', views.mudas_insumos, name='web_mudas_insumos'),

    url(r'^modulofiscal/$', views.modulofiscal, name='web_modulofiscal'),
    url(r'^historiarural/$', views.historiarural, name='web_historiarural'),
    url(r'^resultado/$', views.resultado, name='resultado'),
    url(r'^resultado_ud/$', views.resultado_ud, name='resultado_ud'),
    url(r'^select_resultado/$', views.select_resultado, name='select_resultado'),

    url(r'^janela_conhecimento/$', views.janela_conhecimento, name='janela_conhecimento'),

    url(r'^edital_ud/$', views.edital_ud, name='web_edital_ud'),
    url(r'^edital_um_direcionada/$', views.edital_um_direcionada, name='edital_um_direcionada'),
    url(r'^en/$', views.web_en, name='web_en'),
    url(r'^es/$', views.web_es, name='web_es'),


]
