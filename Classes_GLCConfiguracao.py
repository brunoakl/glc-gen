

class ConfiguracaoGLC(object):
    def __init__(self):
        self.vGramaticaAtual = []
        self.vSimboloAtual = []
        
    def ConfiguracaoPadrao(self):
      self.vSimboloAtual = ['S','NP','NP','VP','Det','N','V','Adv']
      self.vGramaticaAtual = ['NP VP', 'Det N | Det N', 'eu | ele | ela | joe | tu | nós | vós | eles', 
                              'V NP | VP', 'a | o | os | as| meu | dele | deles | dela | daquele | daqueles | destes', 
                              'elefante | gato | jeans | terno | palitó | caderno | garrafa | chapéu | mesa | prato ', 
                              'V | V Adv | chutou | seguido | tomada | bateu | lançou | matou | alimentou | escapuliu | corre | pula | dorme | come | bebe',
                              'rápido | devagar | silenciosamente | felizmente | bruptamente | dramaticamente | justamente '
                             ]
    
    
    def ConfiguracaoNova(self, pSimbolos, pGramatica):
      self.vGramaticaAtual = pGramatica
      self.vSimboloAtual = pSimbolos 

    def PegarGramatica(self):
      return self.vGramaticaAtual

    def PegarSimbolo(self):
      return self.vSimboloAtual
