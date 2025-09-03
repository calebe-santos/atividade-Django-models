O objetivo do projeto era criar, do zero, a estrutura de dados e o painel de gerenciamento para uma aplicação web. O tema escolhido foi uma plataforma de 
e-commerce.

O desenvolvimento seguiu quatro etapas principais:
1. Modelagem de Dados
Foram criados oito models no arquivo models.py para representar as entidades de um e-commerce: Produto, Categoria, Fornecedor, Cliente, Pedido, ItemPedido,
AvaliacaoProduto e CupomDesconto. A relação entre eles foi feita de forma lógica e coerente, utilizando:

ForeignKey: Para relacionamentos de um para muitos, como um Produto que pertence a uma Categoria.

ManyToManyField: Para relacionamentos de muitos para muitos, como um Pedido que pode ter vários CupomDesconto.
Cada model também recebeu o método 

__str__ para garantir uma representação clara no painel de administração.

2. Configuração do Painel de Administração
O painel de administração padrão do Django foi substituído por um tema customizado, o 

Django Jazzmin. Para isso, o pacote foi instalado e configurado no arquivo 

settings.py do projeto.

3. Customização Avançada do Admin
Todos os oito models criados foram registrados no painel de administração para ficarem visíveis. Além disso, 

quatro models foram customizados com uma classe ModelAdmin para melhorar a experiência de gerenciamento. Nesses models, foram usados os seguintes recursos:

list_display: Para escolher quais colunas exibir na listagem de dados.

list_filter: Para criar filtros interativos por campos importantes, como categoria ou status.

search_fields: Para adicionar uma barra de busca que permite pesquisar por campos específicos.

4. Configuração e Visualização
Após a configuração, foram executadas as migrações para criar as tabelas no banco de dados. O projeto foi visualizado através de um servidor de desenvolvimento que rodou
em uma porta alternativa para evitar conflitos. A URL para acessar o painel de administração foi configurada no arquivo urls.py do projeto.
