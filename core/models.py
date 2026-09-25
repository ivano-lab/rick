
class Ideia:
    def __init__(self, titulo, descricao, status="em_avaliacao"):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status

    def interpretar(self):
        resultado = (
            f'Título: {self.titulo}\n'
            f'Descrição: {self.descricao}\n'
            f'Status: {self.status}\n'
            )

        return resultado

class Projeto:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.status = "aprovado"

