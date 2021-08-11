from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from desafio_fullstack.core.forms import EstadoForm, CidadeForm
from desafio_fullstack.core.models import Estado, Cidade


def estados_list(request):
    if request.method == 'GET':
        estados = Estado.objects.all()
        context = dict(estados=estados)
        return render(request, 'core/estado_list.html', context)
    else:
        pesquisa = request.POST.get('pesquisa', '')
        estados = Estado.objects.filter(Q(Q(sigla__icontains=pesquisa) | Q(nome__icontains=pesquisa)))
        context = dict(estados=estados, pesquisa=pesquisa)
        return render(request, 'core/estado_list.html', context)


def estados_create(request):
    if request.method == 'GET':
        form = EstadoForm()
        context = dict(form=form)
        return render(request, 'core/estado_form.html', context)
    else:
        form = EstadoForm(request.POST)
        if not form.is_valid():
            context = dict(form=form)
            return render(request, 'core/estado_form.html', context)
        form.save()
        mensagem = 'Estado cadastrado com sucesso.'
        messages.add_message(request, messages.SUCCESS, mensagem, extra_tags='alert alert-success')
        return redirect(reverse('core:estados_list'))


def estados_update(request, estado_pk):
    estado = get_object_or_404(Estado, id=estado_pk)

    if request.method == 'GET':
        form = EstadoForm(instance=estado)
        context = dict(form=form)
        return render(request, 'core/estado_form.html', context)
    else:
        form = EstadoForm(request.POST, instance=estado)
        if not form.is_valid():
            context = dict(form=form)
            return render(request, 'core/estado_form.html', context)
        form.save()
        mensagem = 'Estado alterado com sucesso.'
        messages.add_message(request, messages.SUCCESS, mensagem, extra_tags='alert alert-success')
        return redirect(reverse('core:estados_list'))


def estados_delete(request, estado_pk):
    estado = get_object_or_404(Estado, id=estado_pk)

    if request.method == 'GET':
        context = dict(estado=estado)
        return render(request, 'core/estado_confirm_delete.html', context)
    else:
        estado.delete()
        mensagem = 'Estado excluído com sucesso.'
        messages.add_message(request, messages.SUCCESS, mensagem, extra_tags='alert alert-success')
        return redirect(reverse('core:estados_list'))


def cidades_list(request):
    if request.method == 'GET':
        cidades = Cidade.objects.all()
        context = dict(cidades=cidades)
        return render(request, 'core/cidade_list.html', context)
    else:
        pesquisa = request.POST.get('pesquisa', '')
        cidades = Cidade.objects.filter(nome__icontains=pesquisa)
        context = dict(cidades=cidades, pesquisa=pesquisa)
        return render(request, 'core/cidade_list.html', context)


def cidades_create(request):
    if request.method == 'GET':
        form = CidadeForm()
        context = dict(form=form)
        return render(request, 'core/cidade_form.html', context)
    else:
        form = CidadeForm(request.POST)
        if not form.is_valid():
            context = dict(form=form)
            return render(request, 'core/cidade_form.html', context)
        form.save()
        mensagem = 'cidade cadastrado com sucesso.'
        messages.add_message(request, messages.SUCCESS, mensagem, extra_tags='alert alert-success')
        return redirect(reverse('core:cidades_list'))


def cidades_update(request, cidade_pk):
    cidade = get_object_or_404(Cidade, id=cidade_pk)

    if request.method == 'GET':
        form = CidadeForm(instance=cidade)
        context = dict(form=form)
        return render(request, 'core/cidade_form.html', context)
    else:
        form = CidadeForm(request.POST, instance=cidade)
        if not form.is_valid():
            context = dict(form=form)
            return render(request, 'core/cidade_form.html', context)
        form.save()
        mensagem = 'Cidade alterada com sucesso.'
        messages.add_message(request, messages.SUCCESS, mensagem, extra_tags='alert alert-success')
        return redirect(reverse('core:cidades_list'))


def cidades_delete(request, cidade_pk):
    cidade = get_object_or_404(Cidade, id=cidade_pk)

    if request.method == 'GET':
        context = dict(cidade=cidade)
        return render(request, 'core/cidade_confirm_delete.html', context)
    else:
        cidade.delete()
        mensagem = 'Cidade excluída com sucesso.'
        messages.add_message(request, messages.SUCCESS, mensagem, extra_tags='alert alert-success')
        return redirect(reverse('core:cidades_list'))


def home_view(request):
    return render(request, 'core/home.html')


# Parte de login e logout
def login_view(request):
    if request.method == 'GET':
        return _login_view_get(request)
    else:
        return _login_view_post(request)


def _login_view_get(request):
    return render(request, 'core/login.html')


def _login_view_post(request):
    username = request.POST.get('username', '')
    senha = request.POST.get('senha', '')
    user = authenticate(username=username, password=senha)
    if user is None:
        mensagem = 'Usuário e/ou senha inválidos'
        messages.add_message(request, messages.ERROR, mensagem)
        return render(request, 'core/login.html', status=403)
    login(request, user)
    next_url = request.GET.get('next', '/')
    return redirect(next_url)


def logout_view(request):
    logout(request)
    return redirect(reverse('core:home'))
