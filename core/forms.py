from django.core.mail.message import EmailMessage
from django import forms
from .models import Product


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    subject = forms.CharField(label='Assunto', max_length=120)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {subject}\nMensagem: {message}'

        mail = EmailMessage(
            subject="E-mail enviado pelo sistema Django",
            body=conteudo,
            from_email="contato@domain.com",
            to=['contato@domain.com'],
            headers={'reply-to': email},
        )
        mail.send()


class ProductModelForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'image']