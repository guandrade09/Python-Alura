# Curso: Python Aplicando Orientação a Objetos

from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Restaurante'.ljust(15)} | {'Categoria'.ljust(15)} | {'Avaliação'.ljust(15)} | {'Status'.ljust(15)}')
        print(f'{'-'*len(f'{'Restaurante'.ljust(15)} | {'Categoria'.ljust(15)} | {'Avaliação'.ljust(15)} | {'Status'.ljust(15)}')}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(15)} | {restaurante.categoria.ljust(15)} | {str(restaurante.media_avaliacoes).ljust(15)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '✔' if self._ativo else '✖'
    
    def status(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 <=  nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma = sum(avaliacao.nota for avaliacao in self._avaliacao)
        qtde = len(self._avaliacao)
        media = round(soma/qtde, 1)
        return media