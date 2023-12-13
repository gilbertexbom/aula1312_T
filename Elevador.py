# classe Elevador
class Elevador(object):
    # Método construtor
    def __init__(self, andarAtual, portaAberta, peso):
        self.andarAtual = andarAtual
        self.portaAberta = portaAberta
        self.peso = peso

    # Encapsulamento
    def setAndarAtual(self, andarAtual):
        self.andarAtual = andarAtual

    def getAndarAtual(self):
        return self.andarAtual

    def setPortaAberta(self, portaAberta):
        self.portaAberta = portaAberta

    def getPortaAberta(self):
        return self.portaAberta

    def setPeso(self, peso):
        self.peso = peso

    def getPeso(self):
        return self.peso

    def __str__(self):
        return(
            '\n Andar Atual............' + str(self.getAndarAtual()) +
            '\n Peso...................{:.2f}'.format(self.getPeso()) +
            str('\n\t\t\t -- Porta Aberta -- ' if self.getPortaAberta() else '\n\t\t\t -- Porta Fechada -- ')
        )

