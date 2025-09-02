from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    ativo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="produtos")
    fornecedores = models.ManyToManyField(Fornecedor, related_name="produtos")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class CupomDesconto(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    desconto_percentual = models.IntegerField()  # Ex: 10 = 10%
    ativo = models.BooleanField(default=True)
    validade = models.DateField()

    def __str__(self):
        return f"{self.codigo} ({self.desconto_percentual}%)"


class Pedido(models.Model):
    STATUS_CHOICES = [
        ("PENDENTE", "Pendente"),
        ("PAGO", "Pago"),
        ("ENVIADO", "Enviado"),
        ("CONCLUIDO", "Concluído"),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="pedidos")
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDENTE")
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cupom = models.ForeignKey(CupomDesconto, on_delete=models.SET_NULL, blank=True, null=True, related_name="pedidos")

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.nome}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="itens_pedido")
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} (Pedido #{self.pedido.id})"


class AvaliacaoProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="avaliacoes")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="avaliacoes")
    nota = models.IntegerField()  # Ex: 1 a 5
    comentario = models.TextField(blank=True, null=True)
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.produto.nome} - {self.nota}⭐ por {self.cliente.nome}"
