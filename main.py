from core.models import Ideia

ideia = Ideia( 
    "Construir o Rick",
    "Criar um assistente pessoal capaz de transformar ideias em ações."
)

print(f'Ideia: {ideia.titulo}')
print(f'Descrição: {ideia.descricao}')
print(f'Status: {ideia.status}')