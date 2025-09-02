from django.contrib import admin
from .models import (
    Categoria,
    Produto,
    Fornecedor,
    Cliente,
    Pedido,
    ItemPedido,
    CupomDesconto,
    AvaliacaoProduto,
)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "preco", "estoque", "ativo", "criado_em")
    list_filter = ("ativo", "categoria", "fornecedores")
    search_fields = ("nome", "descricao")

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "telefone", "data_cadastro")
    list_filter = ("data_cadastro",)
    search_fields = ("nome", "email")

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "status", "data_pedido", "total", "cupom")
    list_filter = ("status", "data_pedido")
    search_fields = ("id", "cliente__nome", "cliente__email")

@admin.register(AvaliacaoProduto)
class AvaliacaoProdutoAdmin(admin.ModelAdmin):
    list_display = ("produto", "cliente", "nota", "data_avaliacao")
    list_filter = ("nota", "data_avaliacao")
    search_fields = ("produto__nome", "cliente__nome")

admin.site.register(Categoria)
admin.site.register(Fornecedor)
admin.site.register(ItemPedido)
admin.site.register(CupomDesconto)