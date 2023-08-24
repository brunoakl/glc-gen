import tkinter as tk
from tkinter import messagebox, filedialog as fd
import Classes_GLCConfiguracao
import re

vJanelaAberta = False

class InterfaceConfiguracaoGLC():
  def __init__(self):
    self.frmConfiguracaoGLC = tk.Tk()
    self.FLargura = 800 
    self.FAltura = 600
    self.frmComponentes = tk.Frame(self.frmConfiguracaoGLC)
    self.edtSimboloNaoTerminal = tk.Entry(self.frmComponentes)
    self.lblSeta = tk.Label(self.frmComponentes)
    self.edtNovaGramatica = tk.Entry(self.frmComponentes)
    self.mmoNovaConfiguracaoGLC = tk.Text(self.frmConfiguracaoGLC)
    self.frmConfiguracaoBotoes = tk.Frame(self.frmConfiguracaoGLC)
    self.lblInformacao = tk.Label(self.frmConfiguracaoBotoes) 
    self.btnAdicionarNovaGramatica = tk.Button(self.frmComponentes)
    self.btnAbrirGramatica = tk.Button(self.frmComponentes)
    self.btnImplementar = tk.Button(self.frmConfiguracaoBotoes)
    self.btnRetornaPadrao = tk.Button(self.frmConfiguracaoBotoes)
    self.btnRetroceder = tk.Button(self.frmConfiguracaoBotoes) 
    self.btnLimpar = tk.Button(self.frmConfiguracaoBotoes)
    self.FGramaticas = Classes_GLCConfiguracao.ConfiguracaoGLC()
    self.FLinha = 0 
    
  def DesativaBotoesSeMemoLimpo(self):
    if self.VerificaMemoLimpo():
      self.DesativarImplementarLimpar()

  def VerificaMemoLimpo(self):
    vResposta = True
    if self.FLinha != 0:
      vResposta = False
    return vResposta
  
  def LimparCampos(self):
    self.LimparEdit(self.edtSimboloNaoTerminal)
    self.LimparEdit(self.edtNovaGramatica)

  def LimparEdit(self, pEntry):
    pEntry.delete('0', 'end')

  def LimparMemo(self):
    self.mmoNovaConfiguracaoGLC.config(state='normal')
    self.mmoNovaConfiguracaoGLC.delete('1.0', 'end')
    self.FLinha = 0
    self.DesativarImplementarLimpar()
    self.DesativarRetroceder()
    self.mmoNovaConfiguracaoGLC.config(state='disabled')
    
  def RetirarEspacosInicioFim(self, pCampo):
    vTexto = pCampo.lstrip()
    return vTexto.rstrip()

  def PegarTexto(self, pEntry):
    return self.RetirarEspacosInicioFim(pEntry.get())

  def PegarTextoSemEspaco(self, pCampo):
    return pCampo.strip()

  def VerificaCampoVazio(self, pCampo):
    vResultado = True
    if not self.PegarTextoSemEspaco(pCampo):
      vResultado = False
    return vResultado
  
  def Retroceder(self):
    FLinha = str(self.FLinha) + '.0'
    self.mmoNovaConfiguracaoGLC.config(state='normal')
    self.mmoNovaConfiguracaoGLC.delete(FLinha, "end") 
    self.mmoNovaConfiguracaoGLC.insert(tk.END,"\n")
    self.FLinha = self.FLinha - 1
    if self.FLinha == 0:
      self.DesativarRetroceder()
    self.mmoNovaConfiguracaoGLC.config(state='disabled')
    self.DesativaBotoesSeMemoLimpo()
    
  def AtivarImplementarLimpar(self):
    self.btnImplementar.config(state="normal")
    self.btnLimpar.config(state='normal')

  def DesativarImplementarLimpar(self):
    self.btnImplementar.config(state="disabled")
    self.btnLimpar.config(state='disabled')

  def DesativarRetroceder(self):
    self.btnRetroceder.config(state="disabled")

  def AtivarRetroceder(self):
    self.btnRetroceder.config(state="normal")

  def AdicionarCampoEmMemo(self):
    self.mmoNovaConfiguracaoGLC.config(state='normal')
    vSimbolo = self.PegarTexto(self.edtSimboloNaoTerminal)
    vGramatica = self.PegarTexto(self.edtNovaGramatica)

    if (not self.VerificaCampoVazio(vSimbolo)) or (not self.VerificaCampoVazio(vGramatica)):
      messagebox.showinfo(title="Atenção!", message="Algum dos campos esta vazio!", icon=messagebox.INFO)
      self.FocarJanela()
    else:
      self.mmoNovaConfiguracaoGLC.insert(tk.END, vSimbolo + " ~ " + vGramatica + "\n")
      self.FLinha = self.FLinha + 1
      self.LimparCampos()
      self.edtSimboloNaoTerminal.focus_set()

    self.mmoNovaConfiguracaoGLC.config(state='disabled')
    self.FocarJanela()
    
    if not self.VerificaMemoLimpo():
      self.AtivarImplementarLimpar()

  def OperacaoSucesso(self):
     messagebox.showinfo(title="Atenção!", message="Implementado com sucesso!", icon=messagebox.INFO)
     self.FecharJanela()   

  def Implementar(self):
    if not self.Confirmar():
      self.FocarJanela()
    else:
      vGramatica = []
      vSimbolo = []
      vRegexSimbolo = re.compile('^([a-zA-Z]+) *~')
      vRegexGramatica = re.compile('~ *(.+)$')

      for vLinha in self.mmoNovaConfiguracaoGLC.get("1.0", tk.END).splitlines():
        if not vLinha:
          continue
        else:
          vMatchGramatica = vRegexGramatica.search(vLinha)
          vMatchSimbolo = vRegexSimbolo.search(vLinha)
          vSimbolo.append(vMatchSimbolo.group(1))
          vGramatica.append(vMatchGramatica.group(1))

      self.FGramaticas.ConfiguracaoNova(pGramatica= vGramatica, pSimbolos= vSimbolo)
      self.OperacaoSucesso()

  def PegarDadosArquivo(self, pNomeTxt):
    self.LimparMemo()
    with open(pNomeTxt, "r") as arquivo:
      for vlinha in arquivo:
        vResultado = re.search(
          '^([a-zA-Z]+) *~ *(.+)$',
          vlinha) 
        if vResultado:
          self.mmoNovaConfiguracaoGLC.config(state='normal')
          self.mmoNovaConfiguracaoGLC.insert(tk.END, vlinha)
    self.AtivarImplementarLimpar()
    
  def AbrirArquivo(self):
    Tipo_Arquivo = (('Arquivos Txt', '*.txt'),
                    ('Arquivos Txt', '*.txt'))
    
    NomeArquivo = fd.askopenfilename(
                                     title='Seleciona Gramatica',
                                     initialdir='/',
                                     filetypes=Tipo_Arquivo
                                    )
    if not NomeArquivo:
      messagebox.showinfo(title="Atenção!", message="Arquivo não escolhido!", icon=messagebox.INFO)
    else:
      self.PegarDadosArquivo(NomeArquivo)
    self.FocarJanela()
      
  
  def FecharJanela(self):
    global vJanelaAberta
    vJanelaAberta = False
    self.frmConfiguracaoGLC.destroy()
  
  def Confirmar(self):
    vResposta = messagebox.askquestion(title="Atenção!", 
                                        message="Deseja realmente Salvar? \nIsso ira sobreescrever a atual", 
                                        icon=messagebox.INFO)
    if vResposta == 'yes':
      return True
    else:
      return False
    
  def FocarJanela(self):
    self.frmConfiguracaoGLC.lift()
    self.frmConfiguracaoGLC.deiconify()
    self.edtSimboloNaoTerminal.focus_set()

  def CriarJanela(self):
    global vJanelaAberta
    vJanelaAberta = True
    vLarguraTela = self.frmConfiguracaoGLC.winfo_screenwidth()
    vAlturaTela = self.frmConfiguracaoGLC.winfo_screenheight()
    vX = (vLarguraTela/2) - (self.FLargura/2)
    vY = (vAlturaTela/2) - (self.FAltura/2)
    self.frmConfiguracaoGLC.geometry('%dx%d+%d+%d' % (self.FLargura, self.FAltura, vX, vY))
    self.frmConfiguracaoGLC.title("Configuração de GLC")   
    self.frmConfiguracaoGLC.protocol("WM_DELETE_WINDOW", self.FecharJanela)
    self.frmComponentes.pack(padx=10, pady=10)
    self.edtSimboloNaoTerminal.grid(row=0, column=1)
    self.edtSimboloNaoTerminal.config(width= 10, justify="center")
    self.lblSeta.config(text=" ~ ")
    self.lblSeta.grid(row=0, column=3)
    self.edtNovaGramatica.grid(row=0, column=5)
    self.edtNovaGramatica.config(justify="center")
    self.mmoNovaConfiguracaoGLC.pack(padx=10, pady=25, fill='both', expand=True)
    self.mmoNovaConfiguracaoGLC.config(state='disabled')
    self.frmConfiguracaoBotoes.pack(padx=5, pady=5)
    self.lblInformacao.pack(side="bottom", pady=1)
    self.lblInformacao.config(text="[F5] -> Retorna Padrão   [f8] -> Abre Gramatica   [Ctrl + A] -> Adicionar" +    
                                   "\n[Ctrl + I] -> Implementar   [Ctrl + L] -> Limpar Linhas     " +
                                   "[Ctrl + Z] -> Retroceder Linha"
                              , anchor='s')
    self.btnAdicionarNovaGramatica.config(text="Adicionar", command= self.AdicionarCampoEmMemo)
    self.btnAdicionarNovaGramatica.grid(row=0,column=9, padx=5)
    self.btnAbrirGramatica.config(text= "Importar Gramatica", command=self.AbrirArquivo)
    self.btnAbrirGramatica.grid(row=0,column=12)
    self.btnImplementar.config(text="Implementar Nova Configuração", state='disabled', command= self.Implementar)
    self.btnImplementar.pack(side='left', padx= 2, pady=5)  
    self.btnRetornaPadrao.config(text="Retornar Padrão", command= self.RetornarPadrao)
    self.btnRetornaPadrao.pack(side='left', padx= 2, pady=5) 
    self.btnLimpar.config(text="Limpar", command= self.LimparMemo)   
    self.btnLimpar.pack(side='right', padx= 2, pady=5)         
    self.btnRetroceder.config(text="Retroceder", state= 'normal', command= self.Retroceder)
    self.btnRetroceder.pack(side='right', padx= 2, pady=5)      
    self.frmConfiguracaoGLC.bind_all("<F8>", lambda event: self.btnAbrirGramatica.invoke())
    self.frmConfiguracaoGLC.bind_all("<Control-a>", lambda event: self.btnAdicionarNovaGramatica.invoke())
    self.frmConfiguracaoGLC.bind_all("<F5>", lambda event: self.btnRetornaPadrao.invoke())
    self.frmConfiguracaoGLC.bind_all("<Control-i>", lambda event: self.btnImplementar.invoke())
    self.frmConfiguracaoGLC.bind_all("<Control-l>", lambda event: self.btnLimpar.invoke())
    self.frmConfiguracaoGLC.bind_all("<Control-z>", lambda event: self.btnRetroceder.invoke())

  def RetornarPadrao(self):
    if not self.Confirmar():
      self.FocarJanela()
    else:
      self.FGramaticas.ConfiguracaoPadrao()
      self.PreencherMemo()
      self.OperacaoSucesso()

  def PreencherMemo(self):
    self.mmoNovaConfiguracaoGLC.config(state="normal")
    vGramaticas = self.FGramaticas.PegarGramatica()
    vSimbolos = self.FGramaticas.PegarSimbolo()   
    for vCampo in range(len(vSimbolos)):
      self.FLinha = self.FLinha + 1
      vtexto = vSimbolos[vCampo] + ' ~ ' +  vGramaticas[vCampo]
      self.mmoNovaConfiguracaoGLC.insert(tk.END, vtexto + "\n") 
    self.mmoNovaConfiguracaoGLC.config(state='disabled')

  def DevolverConfiguracao(self):
    return self.FGramaticas

  def AbrirJanela(self, pGramatica):
    self.FGramaticas = pGramatica
    self.CriarJanela()
    self.PreencherMemo()
    self.btnLimpar.config(state='normal')
    self.frmConfiguracaoGLC.mainloop()
