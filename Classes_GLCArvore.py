import re
import nltk
nltk.download('punkt')
import io
import sys

class Arvore(object):
    def __init__(self):
        self.Fgramatica = ""
        self.FTextoConvertido =""
        self.FSaida = ""

    def ConverterGramatica(self, pTexto):
        vRegraDeProducao = re.compile(r"\[([^\]]+)\]\s*=\s*(.+)")
        vTexto = ""
        for vMatch in vRegraDeProducao.finditer(pTexto):
            vDireita, vEsquerda = vMatch.groups()
            vEsquerda = re.sub(r"\s*\|\s*", " | ", vEsquerda)
            vEsquerda = re.sub(r"\b([a-zéúíóáàìãç]+)\b", lambda m: f"'{m.group(1)}'", vEsquerda)
            vEsquerda = re.sub(r"\[([^\]]+)\]", lambda m: f"{m.group(1)}", vEsquerda)
            if "|" in vEsquerda:
                vTexto += f"{vDireita.strip()} -> {vEsquerda.strip()}\n"
            else:
                vTexto += f"{vDireita.strip()} -> {vEsquerda.strip()}\n"
        return vTexto

    def IniciarGramatica(self, vGramaticas, vSimbolos):
        vTexto1 = ""
        for vPosicao in range(len(vSimbolos)):
            vTexto1 += "[" + vSimbolos[vPosicao] + "] = [" + vGramaticas[vPosicao] + "]\n"
        self.Fgramatica = vTexto1
        self.FTextoConvertido = self.ConverterGramatica(self.Fgramatica)

    def CriaArvore(self, pSentenca, pGramaticas, pSimbolos):
        self.IniciarGramatica(pGramaticas, pSimbolos)
        vtexto = nltk.CFG.fromstring(self.FTextoConvertido)
        parser = nltk.ChartParser(vtexto)
        tokens = nltk.word_tokenize(pSentenca)
        VTexto_io = io.StringIO()
        sys.stdout = VTexto_io
        for tree in parser.parse(tokens):
            tree.pretty_print()
            break
        sys.stdout = sys.__stdout__
        vArvoreTexto = VTexto_io.getvalue()
        VTexto_io.close()
        return vArvoreTexto
