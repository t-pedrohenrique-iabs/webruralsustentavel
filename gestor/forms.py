# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models	import User

from gestor.models import MetasGerais, MetasPA, MetasMT, MetasRO, MetasBA, MetasMG, MetasPR, MetasRS, NoticiasProjeto, newsletter, Depoimentos


class UserModelForm(forms.ModelForm):

	User._meta.get_field('first_name').blank = False
	User._meta.get_field('last_name').blank = False
	User._meta.get_field('email').blank = False
	User._meta.get_field('username').blank = False
	User._meta.get_field('password').blank = False

	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password']
		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Primeiro nome'}),
			'last_name':  forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Segundo nome'}),
			'email':      forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'E-mail'}),
			'username':   forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Usuário'}),
			'password':   forms.PasswordInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Senha'}),
		}

		erros_messages = {
			'first_name': {
				'required': 'Este campo é obrigatrio'
			},
			'last_name': {
				'required': 'Este campo é obrigatrio'
			},
			'email': {
				'required': 'Este campo é obrigatrio'
			},
			'username': {
				'required': 'Este campo é obrigatrio'
			},
			'password': {
				'required': 'Este campo é obrigatrio'
			}
		}

	def save(self, commit=True):
		user = super(UserModelForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user


class noticiaForm(forms.ModelForm):

	class Meta:
		model = NoticiasProjeto
		fields = ['show_home','titulo','chamada','data_publicacao','img_noticia','img_credito','album_one','album_two','album_three','album_four','album_five', 'album_six','conteudo','video','video_descricao','estado']
		widgets = {
			'titulo'          : forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'maxlength': 1000, 'placeholder': 'Titulo da noticias', 'required': True}),
			'chamada'         : forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'maxlength': 1000, 'placeholder': 'Chamada da noticias', 'required': True}),
			'estado'          : forms.Select(attrs={'class': 'form-control', 'type': 'select', 'required': True}),
			'data_publicacao' : forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'dd/mm/aaaa', 'required': True}),
			'img_noticia'     : forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'maxlength': 1000, 'placeholder': 'Imagem da noticias', 'required': True}),
			'img_credito'     : forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'maxlength': 1000, 'placeholder': 'Credito da imagem'}),
			'conteudo'        : forms.Textarea(attrs={'id': 'conteudo-noticia', 'class': 'form-control', 'maxlength': 10000, 'style': 'width: 100%;height: 600px;', 'required': True}),
			'video'           : forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'maxlength': 1000, 'placeholder': 'Link do video do YouTube'}),
			'video_descricao' : forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'maxlength': 1000, 'placeholder': 'Descricao do video'}),
			'album_one'       : forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'maxlength': 1000, 'placeholder': 'Imagem do album'}),
			'album_two'       : forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'maxlength': 1000, 'placeholder': 'Imagem do album'}),
			'album_three'     : forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'maxlength': 1000, 'placeholder': 'Imagem do album'}),
			'album_four'      : forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'maxlength': 1000, 'placeholder': 'Imagem do album'}),
			'album_five'      : forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'maxlength': 1000, 'placeholder': 'Imagem do album'}),
			'album_six'       : forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'maxlength': 1000, 'placeholder': 'Imagem do album'}),
		}


class MetaProjeto(ModelForm):

	class Meta:
		model = MetasGerais
		fields = ['unidade_demonstrativa', 'unidade_multiplicadora', 'dia_campo', 'produtores_capacitados', 'atecs_treinados']
		widgets = {
			'unidade_demonstrativa':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Unidade Demonstrativa', 'required': True}),
			'unidade_multiplicadora': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Unidade Multiplicadora', 'required': True}),
			'dia_campo':              forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Dia de Campo', 'required': True}),
			'produtores_capacitados': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Produtores', 'required': True}),
			'atecs_treinados':        forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Atec', 'required': True}),
		}


class MetasPAform(ModelForm):
	class Meta:
		model = MetasPA
		fields = ['unidade_demonstrativa', 'unidade_multiplicadora', 'dia_campo', 'produtores_capacitados', 'atecs_treinados']
		widgets = {
			'unidade_demonstrativa':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Unidade Demonstrativa', 'required': True}),
			'unidade_multiplicadora': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Unidade Multiplicadora', 'required': True}),
			'dia_campo':              forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Dia de Campo', 'required': True}),
			'produtores_capacitados': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Produtores', 'required': True}),
			'atecs_treinados':        forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Atec', 'required': True}),
		}

class MetasMTform(ModelForm):
	class Meta:
		model = MetasMT
		fields = ['unidade_demonstrativa', 'unidade_multiplicadora', 'dia_campo', 'produtores_capacitados', 'atecs_treinados']
		widgets = {
			'unidade_demonstrativa':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Unidade Demonstrativa', 'required': True}),
			'unidade_multiplicadora': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Unidade Multiplicadora', 'required': True}),
			'dia_campo':              forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Dia de Campo', 'required': True}),
			'produtores_capacitados': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Produtores', 'required': True}),
			'atecs_treinados':        forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Atec', 'required': True}),
		}


class MetasROform(ModelForm):
	class Meta:
		model = MetasRO
		fields = ['unidade_demonstrativa', 'unidade_multiplicadora', 'dia_campo', 'produtores_capacitados', 'atecs_treinados']
		widgets = {
			'unidade_demonstrativa':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Unidade Demonstrativa', 'required': True}),
			'unidade_multiplicadora': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Unidade Multiplicadora', 'required': True}),
			'dia_campo':              forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Dia de Campo', 'required': True}),
			'produtores_capacitados': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Produtores', 'required': True}),
			'atecs_treinados':        forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Atec', 'required': True}),
		}

class MetasBAform(ModelForm):
	class Meta:
		model = MetasBA
		fields = ['unidade_demonstrativa', 'unidade_multiplicadora', 'dia_campo', 'produtores_capacitados', 'atecs_treinados']
		widgets = {
			'unidade_demonstrativa':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Unidade Demonstrativa', 'required': True}),
			'unidade_multiplicadora': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Unidade Multiplicadora', 'required': True}),
			'dia_campo':              forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Dia de Campo', 'required': True}),
			'produtores_capacitados': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Produtores', 'required': True}),
			'atecs_treinados':        forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Atec', 'required': True}),
		}

class MetasMGform(ModelForm):
	class Meta:
		model = MetasMG
		fields = ['unidade_demonstrativa', 'unidade_multiplicadora', 'dia_campo', 'produtores_capacitados', 'atecs_treinados']
		widgets = {
			'unidade_demonstrativa':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Unidade Demonstrativa', 'required': True}),
			'unidade_multiplicadora': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Unidade Multiplicadora', 'required': True}),
			'dia_campo':              forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Dia de Campo', 'required': True}),
			'produtores_capacitados': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Produtores', 'required': True}),
			'atecs_treinados':        forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Atec', 'required': True}),
		}


class MetasPRform(ModelForm):
	class Meta:
		model = MetasPR
		fields = ['unidade_demonstrativa', 'unidade_multiplicadora', 'dia_campo', 'produtores_capacitados', 'atecs_treinados']
		widgets = {
			'unidade_demonstrativa':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Unidade Demonstrativa', 'required': True}),
			'unidade_multiplicadora': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Unidade Multiplicadora', 'required': True}),
			'dia_campo':              forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Dia de Campo', 'required': True}),
			'produtores_capacitados': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Produtores', 'required': True}),
			'atecs_treinados':        forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Atec', 'required': True}),
		}


class MetasRSform(ModelForm):
	class Meta:
		model = MetasRS
		fields = ['unidade_demonstrativa', 'unidade_multiplicadora', 'dia_campo', 'produtores_capacitados', 'atecs_treinados']
		widgets = {
			'unidade_demonstrativa':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Unidade Demonstrativa', 'required': True}),
			'unidade_multiplicadora': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Unidade Multiplicadora', 'required': True}),
			'dia_campo':              forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Dia de Campo', 'required': True}),
			'produtores_capacitados': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Produtores', 'required': True}),
			'atecs_treinados':        forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade Atec', 'required': True}),
		}



class newsletterForm(forms.ModelForm):

	class Meta:
		model = newsletter
		fields = ['nome_user','email_user']
		widgets = {
			'nome_user'  : forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Nome Completo', 'required': True}),
			'email_user' : forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'E-mail', 'required': True}),
		}


class depoimentoForm(ModelForm):
	class Meta:
		model = Depoimentos
		fields = ['titulo',
			'descricao',
			'embed_link',
			'link_img']
		widgets = {
			'titulo' 		: forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'maxlength': 1000, 'placeholder': 'Titulo do depoimento', 'required': True}),
			'descricao'		: forms.Textarea(attrs={'class': 'form-control', 'maxlength': 10000, 'style': 'width: 100%;height: 300px;'}),
			'embed_link'	: forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'maxlength': 1000, 'placeholder': 'Embed do depoimento', 'required': True}),
			'link_img'		: forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'maxlength': 1000, 'placeholder': 'Link da imagem', 'required': True}),
		}
