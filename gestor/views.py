from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.db.models import Max
from random import randint
import json

from gestor.models import MetasGerais, MetasPA, MetasMT, MetasRO, MetasBA, MetasMG, MetasPR, MetasRS, Noticias, NoticiasProjeto, newsletter, Depoimentos
from gestor.forms import UserModelForm, MetaProjeto, MetasPAform, MetasMTform, MetasROform, MetasBAform, MetasMGform, MetasPRform, MetasRSform, noticiaForm, depoimentoForm


@login_required
def cadastroUsuario(request):
    form = UserModelForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

        return redirect('/gestor/cadastro')

    return render(request, 'gestor/usuario/cadastro_usuario.html', locals())


def loginSys(request):
    if request.method == 'POST':

        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/gestor')


    return render(request, 'gestor/usuario/login.html', locals())


def logoutSys(request):
    logout(request)
    return redirect('/gestor/login')


@login_required
def index(request):

    return render(request, 'gestor/home.html', locals())    


def metas_projeto(request):

    registros = len(MetasGerais.objects.all())

    if registros > 0:
        meta_prs = MetasGerais.objects.all()[0]
        hideform = False
    else:
        hideform = True

    form_meta = MetaProjeto(request.POST or None)

    if request.method == 'POST':
        if form_meta.is_valid():
            form_meta.save()

        return redirect('/gestor/metas_projeto')

    return render(request, 'gestor/metas/metas_projeto.html', locals())


def update_meta(request, id):

    obj_meta = MetasGerais.objects.get(id=id)

    form_meta = MetaProjeto(request.POST or None, instance=obj_meta)

    if request.method == 'POST':
        if form_meta.is_valid():
            form_meta.save()

        return redirect('/gestor/metas_projeto')

    return render(request, 'gestor/metas/update_meta.html', locals())


def resultado_estado(request):

    try:
        objPA = MetasPA.objects.all()[0]
        PAform = MetasPAform(request.POST or None, instance=objPA)
    except:
        PAform = MetasPAform(request.POST or None)

    try:
        objMT = MetasMT.objects.all()[0]
        MTform = MetasMTform(request.POST or None, instance=objMT)
    except:
        MTform = MetasMTform(request.POST or None)

    try:
        objRO = MetasRO.objects.all()[0]
        ROform = MetasROform(request.POST or None, instance=objRO)
    except:
        ROform = MetasROform(request.POST or None)

    try:
        objBA = MetasBA.objects.all()[0]
        BAform = MetasBAform(request.POST or None, instance=objBA)
    except:
        BAform = MetasBAform(request.POST or None)

    try:
        objMG = MetasMG.objects.all()[0]
        MGform = MetasMGform(request.POST or None, instance=objMG)
    except:
        MGform = MetasMGform(request.POST or None)

    try:
        objPR = MetasPR.objects.all()[0]
        PRform = MetasPRform(request.POST or None, instance=objPR)
    except:
        PRform = MetasPRform(request.POST or None)

    try:
        objRS = MetasRS.objects.all()[0]
        RSform = MetasRSform(request.POST or None, instance=objRS)
    except:
        RSform = MetasRSform(request.POST or None)

    if request.method == 'POST':
        if request.POST['form_estados'] == 'PAformulario':
            if PAform.is_valid():
                PAform.save()
                return redirect('/gestor/resultado_estado')

        if request.POST['form_estados'] == 'MTformulario':
            if MTform.is_valid():
                MTform.save()
                return redirect('/gestor/resultado_estado')

        if request.POST['form_estados'] == 'ROformulario':
            if ROform.is_valid():
                ROform.save()
                return redirect('/gestor/resultado_estado')

        if request.POST['form_estados'] == 'BAformulario':
            if BAform.is_valid():
                BAform.save()
                return redirect('/gestor/resultado_estado')

        if request.POST['form_estados'] == 'MGformulario':
            if MGform.is_valid():
                MGform.save()
                return redirect('/gestor/resultado_estado')

        if request.POST['form_estados'] == 'PRformulario':
            if PRform.is_valid():
                PRform.save()
                return redirect('/gestor/resultado_estado')

        if request.POST['form_estados'] == 'RSformulario':
            if RSform.is_valid():
                RSform.save()
                return redirect('/gestor/resultado_estado')


    return render(request, 'gestor/metas/resultado_estado.html', locals())


@login_required
def cadastro_noticias(request):

    cadastroNoticiasForm = noticiaForm(request.POST or None)

    if request.method == 'POST':
        if cadastroNoticiasForm.is_valid():
            cadastroNoticiasForm.save()

        return redirect('/gestor/noticias_lista')


    return render(request, 'gestor/noticias/cadastro_noticias.html', locals())


@login_required
def noticias_lista(request):

    objs_noticias = NoticiasProjeto.objects.all().order_by('data_publicacao')[::-1]



    return render(request, 'gestor/noticias/noticias.html', locals())


@login_required
def atualizar_noticia(request, noticia):

    noticia_obj = NoticiasProjeto.objects.get(id=noticia)

    updateNoticiasForm = noticiaForm(request.POST or None, instance=noticia_obj)

    if request.method == 'POST':
        if updateNoticiasForm.is_valid():
            updateNoticiasForm.save()

        return redirect('/gestor/noticias_lista')


    return render(request, 'gestor/noticias/atualizar_noticia.html', locals())


@login_required
def excluir_noticia(request, noticia):

    try:
        NoticiasProjeto.objects.get(id=noticia).delete()
        deleteObj = True

    except:
        deleteObj = False


    return redirect('/gestor/noticias_lista')


@login_required
def home_noticia(request, noticia):

    objNoticia = NoticiasProjeto.objects.get(id=noticia)
    if objNoticia.show_home:
        NoticiasProjeto.objects.filter(id=noticia).update(show_home=False)
        return redirect('/gestor/noticias_lista')

    if len(NoticiasProjeto.objects.filter(show_home=True)) < 7:
        NoticiasProjeto.objects.filter(id=noticia).update(show_home=True)
    else:
        return redirect('/gestor/noticias_lista')


    return redirect('/gestor/noticias_lista')
        

def noticias(request):

    return render(request, 'gestor/noticias.html', locals())


def lista_noticias(request):

    return render(request, 'gestor/lista_noticias.html', locals())


def ajax_ista_noticias(request):
    if request.is_ajax():

        teste = Noticias.objects.filter().order_by('id')

        list_obj = []
        for x in teste:
            obj = {'key_new':x.key_new, 'data_create':x.data_create, 'titulo':x.titulo, 'chamada':x.chamada, 'conteudo':x.conteudo, 'image_link':x.image_link, 'estado':x.estado, 'destaque':x.destaque}
            list_obj.append(obj)
            # import pdb; pdb.set_trace()

        data = json.dumps(list_obj)
        return HttpResponse(data, content_type='application/json')

    else:
        raise Http404


def ajax_del_noticias(request):
    if request.is_ajax():

        Noticias.objects.filter(key_new=request.GET.get('key_new')).delete()

        result = 'deletado'

        item_obj = [result]
        data = json.dumps(item_obj)
        return HttpResponse(data, content_type='application/json')

    else:
        raise Http404


def ajax_capa_noticias(request):
    if request.is_ajax():

        # import pdb; pdb.set_trace()
        # Noticias.objects.filter(key_new=request.GET.get('key_new')).delete()
        # print request.GET.get('key')

        if request.GET.get('action_make') == 'add-capa':
            Noticias.objects.filter(key_new=request.GET.get('key')).update(destaque='true')
            result = request.GET.get('action_make')

        if request.GET.get('action_make') == 'remove-capa':
            Noticias.objects.filter(key_new=request.GET.get('key')).update(destaque='not')
            result = request.GET.get('action_make')


        # result = 'deletado'

        item_obj = [result]
        data = json.dumps(item_obj)
        return HttpResponse(data, content_type='application/json')

    else:
        raise Http404


def ajax_noticias(request):
    if request.is_ajax():

        Noticias.objects.create(key_new = randint(10000,90000),
                                data_create = request.POST.get('data_create'),
                                titulo = request.POST.get('titulo'),
                                chamada = request.POST.get('chamada'),
                                conteudo = request.POST.get('conteudo'),
                                image_link = request.POST.get('image_link'),
                                estado = request.POST.get('estado'),
                                destaque = 'not')

        item_obj = [request.POST.get('titulo')]
        data = json.dumps(item_obj)
        return HttpResponse(data, content_type='application/json')

    else:
        raise Http404


def newsletter_emails(request):

    # list_email = Usernoticias.objects.filter().order_by('id')
    # usuarios = newsletter.objects.all()


    import pdb; pdb.set_trace()

    return render(request, 'gestor/newsletter/newsletter_lista.html', locals())


def ajax_newsletter(request):
    if request.is_ajax():
        # import pdb; pdb.set_trace()
        Usernoticias.objects.create(nome = request.GET.get('nome'),
                                email = request.GET.get('email'),
                                verificado = 'false')

        item_obj = [request.GET.get('nome'), request.GET.get('email')]
        data = json.dumps(item_obj)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404


@login_required
def depoimentos(request):


    all_depoimentos = Depoimentos.objects.all().order_by('date_created')[::-1]

    return render(request, 'gestor/depoimentos/depoimentos.html', locals())


@login_required
def novo_depoimento(request):



    formDepoimento = depoimentoForm(request.POST or None)

    

    if request.method == 'POST':
        if formDepoimento.is_valid():
            formDepoimento.save()
            return redirect('/gestor/depoimentos')

    return render(request, 'gestor/depoimentos/novo_depoimento.html', locals())


@login_required
def update_depoimento(request, id_depoimento):

    obj_depoimento = Depoimentos.objects.get(id=id_depoimento)

    formDepoimento = depoimentoForm(request.POST or None, instance=obj_depoimento)

    if request.method == 'POST':
        if formDepoimento.is_valid():
            formDepoimento.save()
            return redirect('/gestor/depoimentos')

    return render(request, 'gestor/depoimentos/update_depoimento.html', locals())