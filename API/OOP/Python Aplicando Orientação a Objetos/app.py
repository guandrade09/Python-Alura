from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')

restaurante_praca.receber_avaliacao('Gu', 10)
restaurante_praca.receber_avaliacao('May', 3)

restaurante_praca.status()

def main():
    Restaurante.listar_restaurantes()
    pass

if __name__ == '__main__':
    main()