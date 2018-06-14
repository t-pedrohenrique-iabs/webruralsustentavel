from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.db.models import Max

from gestor.models import MetasGerais, MetasPA, MetasMT, MetasRO, MetasBA, MetasMG, MetasPR, MetasRS, Noticias, NoticiasProjeto, Depoimentos
from gestor.forms import newsletterForm

import json

# Create your views here.
def home(request):

    try:
        result_pa = MetasPA.objects.all()[0]
        result_mt = MetasMT.objects.all()[0]
        result_ro = MetasRO.objects.all()[0]
        result_ba = MetasBA.objects.all()[0] 
        result_mg = MetasMG.objects.all()[0]
        result_pr = MetasPR.objects.all()[0]
        result_rs = MetasRS.objects.all()[0]
    except:
        meta_uf = False

    try:
        metageral_prs = MetasGerais.objects.all()[0]
    except:
        meta_all = False


    try:
        destaque_new = Noticias.objects.filter(destaque='true')

        new_destaque_one = destaque_new[0]
        new_destaque_two = destaque_new[1]

    except:
        all_new = Noticias.objects.all()
        size_db = len(all_new)
        cont_for = 0
        for x in all_new:
            cont_for = cont_for + 1
            atual_count = size_db-1
            if cont_for == atual_count:
                new_destaque_one = x
            if cont_for == size_db:
                new_destaque_two =x


    try:
        objNoticia = NoticiasProjeto.objects.filter(show_home=True).order_by('data_publicacao')[::-1]

        if len(objNoticia) == 7:
            noticia_um     = objNoticia[0]
            noticia_dois   = objNoticia[1]
            noticia_tres   = objNoticia[2]
            noticia_quatro = objNoticia[3]
            noticia_cinco  = objNoticia[4]
            noticia_seis   = objNoticia[5]
            noticia_sete   = objNoticia[6]

        else:
            objNoticia = NoticiasProjeto.objects.all().order_by('data_publicacao')[::-1]
            noticia_um     = objNoticia[0]
            noticia_dois   = objNoticia[1]
            noticia_tres   = objNoticia[2]
            noticia_quatro = objNoticia[3]
            noticia_cinco  = objNoticia[4]
            noticia_seis   = objNoticia[5]
            noticia_sete   = objNoticia[6]

        # import pdb; pdb.set_trace()

    except:
        var_float = True


    fromNewsletter = newsletterForm(request.POST or None)

    if request.method == 'POST':
        if fromNewsletter.is_valid():
            fromNewsletter.save()




    # return render(request, 'site/home.html', locals())
    return render(request, 'site/home/index.html', locals())


def visualizar_noticia(request, noticia_id):

    try:
        noticia = NoticiasProjeto.objects.get(id=noticia_id)
    except:
        noticia_invalida = True
    

    return render(request, 'site/noticia/visualizar.html', locals())


def destaques_lista(request):

    try:
        noticias = NoticiasProjeto.objects.all().order_by('data_publicacao')[::-1]
    except:
        noticia_invalida = True

    return render(request, 'site/noticia/lista.html', locals())


def tecnologias(request):

    return render(request, 'site/tecnologias.html')

def participe(request):

    return render(request, 'site/participe.html')

def destaque(request):
    teste = Noticias.objects.filter()
    return render(request, 'site/destaque.html', locals())

def materia(request, chave):
    # import pdb; pdb.set_trace()\\

    materia = Noticias.objects.get(key_new=chave)

    # import pdb; pdb.set_trace()

    listobj = []

    # obj = {'conteudo':materia.conteudo}
    obj = materia.conteudo

    # listobj.append(obj)

    data = json.dumps(obj)

    return render(request, 'site/materia.html', locals())


def ajax_materia(request):
    if request.is_ajax():


        teste = Noticias.objects.get(key_new=request.GET.get('key_new'))

        # import pdb; pdb.set_trace()

        list_obj = [teste.conteudo]

        data = json.dumps(list_obj)
        return HttpResponse(data, content_type='application/json')

    else:
        raise Http404
    return render(request, 'site/destaque.html', locals())


def downloads(request):

    return render(request, 'site/downloads.html')

def sobre(request):

    return render(request, 'site/sobre.html')

def resultados_alcancados(request):

    return render(request, 'site/resultados_alcancados.html')

def projetoAcoes(request):

    return render(request, 'site/projetoAcoes.html')

def beneficiario(request):

    return render(request, 'site/beneficiario.html')

def instituicao_aprovada(request):

    return render(request, 'site/instituicao_aprovada.html')

def flipbook_doctec_gestao(request):
    return render(request, 'site/flipbook_doctec_gestao.html')

def flipbook_doctec_ilpf(request):
    return render(request, 'site/flipbook_doctec_ilpf.html')

def flipbook_doctec_rad(request):
    return render(request, 'site/flipbook_doctec_rad.html')

def flipbook_doctec_pfc(request):
    return render(request, 'site/flipbook_doctec_pfc.html')

def flipbook_doctec_msfn(request):
    return render(request, 'site/flipbook_doctec_msfn.html')

def chamadapiloto(request):
    return render(request, 'site/chamadapiloto.html')

def chamadaud(request):

    return render(request, 'site/chamadaud.html')

def chamada_direcionada(request):

    return render(request, 'site/chamada_direcionada.html')

def chamada_um(request):

    return render(request, 'site/chamada_um.html')


def edital_um_direcionada(request):

    return render(request, 'site/um_direcionada.html')



def depoimento(request, ator):
    # import pdb; pdb.set_trace()
    if ator == 'ronivonCastro':
        return render(request, 'site/depoimento_ronivonCastro.html', locals())
    if ator == 'donaeva':
        return render(request, 'site/depoimento_donaeva.html', locals())
    if ator == 'ericoribeiro':
        return render(request, 'site/depoimento_ericoribeiro.html', locals())
    if ator == 'prodtucuma':
        return render(request, 'site/depoimento_prodtucuma.html', locals())
    if ator == 'celio':
        return render(request, 'site/depoimento_celio.html', locals())
    if ator == 'silviojose':
        return render(request, 'site/depoimento_silviojose.html', locals())
    if ator == 'recital':
        return render(request, 'site/depoimento_cordel.html', locals())
    if ator == 'altervir':
        return render(request, 'site/depoimento_altervir.html', locals())
    if ator == 'luiz_eugenio':
        return render(request, 'site/depoimento_luizEugenio.html', locals())
    if ator == 'adenir_barba':
        return render(request, 'site/depoimento_adenir_barba.html', locals())
    if ator == 'rafael_hirley':
        return render(request, 'site/depoimento_rafael_hirley.html', locals())
    if ator == 'rudimar_barea':
        return render(request, 'site/depoimento_rudimar_barea.html', locals())
    if ator == 'gedeon_ramos':
        return render(request, 'site/depoimento_gedeon_ramos.html', locals())


    return HttpResponseRedirect('/')


def modulofiscal(request):

    return render(request, 'site/modulofiscal.html')

def historiarural(request):

    return render(request, 'site/historiarural.html')

def edital_ud(request):

    return render(request, 'site/edital_ud.html')


def resultado(request):

    return render(request, 'site/resultado.html')


def janela_conhecimento(request):

    all_depoimentos = Depoimentos.objects.all().order_by('date_created')[::-1]

    return render(request, 'site/janela_conhecimento.html', locals())


def video_depoimento(request, id_depoimento):

    video_depoimento = Depoimentos.objects.get(id=id_depoimento)

    return render(request, 'site/videos/video_depoimento.html', locals())


def infografico(request, infografico):
    # import pdb; pdb.set_trace()
    if infografico == 'info_car':
        return render(request, 'site/infografico_car.html', locals())

    if infografico == 'info_florestasnativas':
        return render(request, 'site/infografico_florestasnativas.html', locals())

    if infografico == 'info_ilpf':
        return render(request, 'site/infografico_ilpf.html', locals())

    if infografico == 'info_saf':
        return render(request, 'site/infografico_saf.html', locals())

    if infografico == 'info_ud':
        return render(request, 'site/infografico_ud.html', locals())

    if infografico == 'info_um':
        return render(request, 'site/infografico_um.html', locals())

    if infografico == 'info_rad_f':
        return render(request, 'site/infografico_radf.html', locals())

    if infografico == 'info_pfc':
        return render(request, 'site/infografico_florestascomercias.html', locals())

    if infografico == 'info_gestao':
        return render(request, 'site/infografico_gestao.html', locals())

    if infografico == 'info_rad_p':
        return render(request, 'site/infografico_rad_p.html', locals())

    return HttpResponseRedirect('/')


def informativo_flipbook(request, informativo_flipbook):
    # import pdb; pdb.set_trace()
    if informativo_flipbook == 'gestao_propriedade':
        return render(request, 'site/informativo_flipbook_1.html', locals())

    if informativo_flipbook == 'ilpf':
        return render(request, 'site/informativo_flipbook_2.html', locals())

    if informativo_flipbook == 'rad':
        return render(request, 'site/informativo_flipbook_3.html', locals())

    if informativo_flipbook == 'florestas_comerciais':
        return render(request, 'site/informativo_flipbook_4.html', locals())

    if informativo_flipbook == 'florestas_nativas':
        return render(request, 'site/informativo_flipbook_5.html', locals())

    return HttpResponseRedirect('/')


def web_en(request):

    # id_row = Total_Metas.objects.all().aggregate(Max('id'))['id__max']
    # meta_atual = Total_Metas.objects.get(id=id_row)

    try:
        result_pa = MetasPA.objects.all()[0]
        result_mt = MetasMT.objects.all()[0]
        result_ro = MetasRO.objects.all()[0]
        result_ba = MetasBA.objects.all()[0] 
        result_mg = MetasMG.objects.all()[0]
        result_pr = MetasPR.objects.all()[0]
        result_rs = MetasRS.objects.all()[0]
    except:
        meta_uf = False

    try:
        metageral_prs = MetasGerais.objects.all()[0]
    except:
        meta_all = False

    return render(request, 'site/site_en.html', locals())


def web_es(request):

    # id_row = Total_Metas.objects.all().aggregate(Max('id'))['id__max']
    # meta_atual = Total_Metas.objects.get(id=id_row)

    try:
        result_pa = MetasPA.objects.all()[0]
        result_mt = MetasMT.objects.all()[0]
        result_ro = MetasRO.objects.all()[0]
        result_ba = MetasBA.objects.all()[0] 
        result_mg = MetasMG.objects.all()[0]
        result_pr = MetasPR.objects.all()[0]
        result_rs = MetasRS.objects.all()[0]
    except:
        meta_uf = False

    try:
        metageral_prs = MetasGerais.objects.all()[0]
    except:
        meta_all = False

    return render(request, 'site/site_es.html', locals())


def resultado_ud(request):

    return render(request, 'site/resultado_ud.html')

def select_resultado(request):

    # fromNewsletter = newsletterForm(request.POST or None)

    return render(request, 'site/select_resultado.html')


def mudas_insumos(request):

    return render(request, 'site/editais/mudas_insumos.html')