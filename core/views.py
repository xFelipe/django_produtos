from django.shortcuts import render
from .forms import ContactForm, ProductModelForm
from django.contrib import messages
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
            # form = ContactForm()
        else:
            messages.error(request, "Formulário inválido")
    context = {
        'form': form
    }
    return render(request, 'core/contact.html', context)

def product(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, "Produto salvo com sucesso!")
            # form = ProductModelForm()
        else:
            messages.error(request, "Erro ao salvar produto")
    else:
        form = ProductModelForm()

    return render(request, 'core/product.html', context={
        'form': form
    })
