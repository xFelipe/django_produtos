from django.db import models
from stdimage.models import StdImageField

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)   
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    active = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Product(Base):
    name = models.CharField('Nome', max_length=100)
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    stock = models.IntegerField('Estoque')
    image = StdImageField('Imagem', upload_to='uploads/produtos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Selug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.name


def produto_pre_save(signal, instance: Product, sender, **kwargs):
    instance.slug = slugify(instance.name)

signals.pre_save.connect(produto_pre_save, sender=Product)
