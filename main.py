#from core.interpreter import interpretar
from core.models import Ideia

titulo = input("Título: ")

descricao = input("Descrição: ")

ideia = Ideia(titulo, descricao)

resultado = ideia.interpretar()

print(f"--- Avaliação --- \n")
print(resultado)