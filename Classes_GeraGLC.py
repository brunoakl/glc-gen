import random
import collections
from collections import defaultdict


class GerarGLC(object):
    def __init__(self):
        self.vGramatica = defaultdict(list)

    def AdicionarGramatica(self, pNaoTerminal, pRegraNegocio):
        vGramaticas = pRegraNegocio.split('|')
        for vGramatica in vGramaticas:
            self.vGramatica[pNaoTerminal].append(tuple(vGramatica.split()))

    def GerarRandomicamente(self, pSimbolo, pPassoaPasso):
        vTexto = ''
        if pPassoaPasso == True:
            vTextoTodo = ''
            vTextoTodo += pSimbolo + '->'
        vGramaticaAleatoria = random.choice(self.vGramatica[pSimbolo])
        for vSimbolo in vGramaticaAleatoria:
            if vSimbolo in self.vGramatica:
                if pPassoaPasso == True:
                    vTextoTodo += vSimbolo + '->'
                vTexto += self.GerarRandomicamente(vSimbolo, pPassoaPasso)
            else:
                vTexto += vSimbolo + ' '
                if pPassoaPasso == True:
                    vTexto += '\n'
        if pPassoaPasso == True:
            return vTextoTodo + vTexto
        else:
            return vTexto


