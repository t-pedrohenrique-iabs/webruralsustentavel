from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='gestor_index'),
    url(r'^home$', views.index, name='gestor_index'),

    url(r'^cadastro/$',views.cadastroUsuario, name='cadastro_usuario'),
    url(r'^login/$',views.loginSys, name='login'),
    url(r'^logout/$',views.logoutSys, name='logout'),

    url(r'^metas_projeto/$',views.metas_projeto, name='metas_projeto'),
    url(r'^(?P<id>[-\w\d]+)/update_meta$', views.update_meta, name='update_meta'),

    url(r'^resultado_estado/$',views.resultado_estado, name='resultado_estado'),

    url(r'^cadastro_noticias/$',views.cadastro_noticias, name='cadastro_noticias'),    
    url(r'^noticias_lista/$',views.noticias_lista, name='noticias_lista'),   
    url(r'^(?P<noticia>[-\w\d]+)/atualizar_noticia/$',views.atualizar_noticia, name='atualizar_noticia'),   
    url(r'^(?P<noticia>[-\w\d]+)/excluir_noticia/$',views.excluir_noticia, name='excluir_noticia'),   
    url(r'^(?P<noticia>[-\w\d]+)/home_noticia/$',views.home_noticia, name='home_noticia'),   

    url(r'^newsletter/$',views.newsletter, name='newsletter'),


    url(r'^noticias/$',views.noticias, name='noticias'),
    url(r'^lista_noticias/$',views.lista_noticias, name='lista_noticias'),
    url(r'^ajax_ista_noticias/$',views.ajax_ista_noticias, name='ajax_ista_noticias'),
    url(r'^ajax_del_noticias/$',views.ajax_del_noticias, name='ajax_del_noticias'),
    url(r'^ajax_capa_noticias/$',views.ajax_capa_noticias, name='ajax_capa_noticias'),


    url(r'^ajax_noticias/$',views.ajax_noticias, name='ajax_noticias'),
    
    url(r'^newsletter/$',views.newsletter_emails, name='newsletter_emails'),

    url(r'^depoimentos/$',views.depoimentos, name='depoimentos'),
    url(r'^depoimento/novo/$',views.novo_depoimento, name='novo_depoimento'),
    url(r'^depoimento/update/(?P<id_depoimento>[-\w\d]+)$',views.update_depoimento, name='update_depoimento'),


    

]
