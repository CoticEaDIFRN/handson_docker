from django.db.models import Model, CharField

class Pedido(Model):
    cliente_cpf = CharField('CPF', max_length=11)
    descricao = CharField('Descrição', max_length=255)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return "%s (%s) %s" % (self.id, self.cliente_cpf, self.descricao)
