from django.shortcuts import render
from .forms import ContactForm, ProductModelForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import Product


def index(request):
    return render(request, 'core/index.html', context={
        'products': Product.objects.all()
    })

# Create your views here.
def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.send_mail()

            messages.success(request, "E-mail enviado com sucesso!")
            form = ContactForm() # Reset form
        else:
            messages.error(request, "Formulário inválido")

    return render(request, 'core/contact.html', context={
        'form': form
    })

def product(request):
    if not request.user.is_authenticated:
        return redirect('index')

    form = ProductModelForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

            messages.success(request, "Produto salvo com sucesso!")
            form = ProductModelForm() # Reset form
        else:
            messages.error(request, "Erro ao salvar produto")

    return render(request, 'core/product.html', context={
        'form': form
    })
