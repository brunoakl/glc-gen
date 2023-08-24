import sys
import tkinter as tk
from tkinter import ttk, messagebox
import random
import Classes_GLCConfiguracao
import Classes_GeraGLC
import Classes_GLCArvore
import Forms_GLCConfiguracao

class InterfaceGerarGLC():
  def __init__(self):
    self.frmPrincipal = tk.Tk()
    self.FLargura = 800
    self.FAltura = 600
    self.frmBotoes = tk.Frame(self.frmPrincipal)
    self.ckxPassoAPasso = tk.Checkbutton(self.frmPrincipal)
    self.ckxArvore = tk.Checkbutton(self.frmPrincipal)
    self.FCheckbox = tk.BooleanVar()
    self.FCheckbox2 = tk.BooleanVar()
    self.FPassoaPasso = bool
    self.FArvore = bool
    self.lblLinhas = tk.Label(self.frmPrincipal)
    self.FLinha_selecionada = tk.IntVar() 
    self.cmbLinhas = ttk.Combobox(self.frmPrincipal, textvariable=self.FLinha_selecionada)
    self.mmoGerarGLC = tk.Text(self.frmPrincipal)
    self.btnGerar = tk.Button(self.frmBotoes)
    self.btnConfiguracao = tk.Button(self.frmBotoes)
    self.lblInformacao = tk.Label(self.frmPrincipal)    
    self.FGLCArvore = Classes_GLCArvore.Arvore()
    self.FTextosGLC = Classes_GLCConfiguracao.ConfiguracaoGLC()
    self.FConfiguracao = Forms_GLCConfiguracao
    self.FJanelaConfig = None
    self.FLinha = 0
    self.FUltimoMarcado = 0
  
  def PegarLinhas(self):
    if not self.FLinha_selecionada.get():
       messagebox.showinfo(title="Atenção!", message="Quantidade de Linhas não escolhida!", icon=messagebox.INFO)      
    else:
      self.FLinha = self.FLinha_selecionada.get()
  
  def Alternar(self):
    if self.FCheckbox.get() and self.FCheckbox2.get():
      if self.FUltimoMarcado == 1:
        self.ckxPassoAPasso.deselect()
      elif self.FUltimoMarcado ==2:
        self.ckxArvore.deselect()

    if self.FCheckbox.get():
      self.FUltimoMarcado = 1
    if self.FCheckbox2.get():
      self.FUltimoMarcado = 2


  def PegarEscolha(self):
    self.FPassoaPasso = self.FCheckbox.get()
    self.FArvore = self.FCheckbox2.get()

  def GerarGLCEmMemo(self):
    try:
      self.PegarLinhas()
      self.PegarEscolha()
      self.mmoGerarGLC.config(state="normal")
      self.mmoGerarGLC.delete('1.0', tk.END)
      vGramaticas = self.FTextosGLC.PegarGramatica()
      vSimbolos = self.FTextosGLC.PegarSimbolo()   
      vGeraGLC = Classes_GeraGLC.GerarGLC()
      for vCampo in range(len(vSimbolos)):
        vGeraGLC.AdicionarGramatica(vSimbolos[vCampo], vGramaticas[vCampo])
      
      for vInteiro in range(self.FLinha):
        vTexto = vGeraGLC.GerarRandomicamente(vSimbolos[0], self.FPassoaPasso)
        if self.FArvore:
          self.mmoGerarGLC.insert(tk.END, vTexto + '\n\n') 
          vTexto = self.FGLCArvore.CriaArvore(vTexto, vGramaticas, vSimbolos)
          self.mmoGerarGLC.insert(tk.END, vTexto + '\n\n') 
        else:
          self.mmoGerarGLC.insert(tk.END, vTexto + "\n")   
      self.mmoGerarGLC.config(state="disabled") 
    except Exception:
      messagebox.showinfo(title="Atenção!", message="Alguma Coisa deu Errado, verifique a configuração!", 
                          icon=messagebox.INFO) 
      self.AbrirConfiguracao()

  def AbrirConfiguracao(self):
    if not self.FConfiguracao.vJanelaAberta:
      self.FJanelaConfig = self.FConfiguracao.InterfaceConfiguracaoGLC()
      self.FJanelaConfig.AbrirJanela(self.FTextosGLC)
      self.FTextosGLC = self.FJanelaConfig.DevolverConfiguracao()
    else:
      self.FJanelaConfig.FocarJanela()

  def FecharJanela(self):
    FConfiguracao = Forms_GLCConfiguracao
    FJanelaConfig = FConfiguracao.InterfaceConfiguracaoGLC()
    FJanelaConfig.FecharJanela
    self.frmPrincipal.destroy()
    sys.exit()

  def CriarJanela(self):
    self.FTextosGLC.ConfiguracaoPadrao()
    vLarguraTela = self.frmPrincipal.winfo_screenwidth()
    vAlturaTela = self.frmPrincipal.winfo_screenheight()
    vX = (vLarguraTela/2) - (self.FLargura/2)
    vY = (vAlturaTela/2) - (self.FAltura/2)
    self.frmPrincipal.geometry('%dx%d+%d+%d' % (self.FLargura, self.FAltura, vX, vY))
    self.frmPrincipal.title("Gerador de GLC")
    self.frmPrincipal.protocol("WM_DELETE_WINDOW", self.FecharJanela)
    self.ckxPassoAPasso.config(text='Visualizar Passo a Passo', variable=self.FCheckbox, 
                               offvalue=False, onvalue= True, command=self.Alternar)
    self.ckxPassoAPasso.place(x=8, y=4, height=17, anchor= "nw")
    self.ckxArvore.bind()
    self.ckxArvore.config(text='Visualizar Arvore Der.', variable=self.FCheckbox2, 
                          offvalue=False, onvalue= True, command=self.Alternar)
    self.ckxArvore.place(x=8, y=19)
    self.lblLinhas.config(text="Quantidade de linhas:")
    self.lblLinhas.place(x=600, y=3)
    options = [str(i) for i in range(1, 100)]
    self.cmbLinhas['values'] = options
    self.cmbLinhas.place(x=600, y=20)
    self.mmoGerarGLC.config(wrap='word', state='disabled')
    self.mmoGerarGLC.pack(padx=10, pady=45, fill='both', expand=True)
    self.frmBotoes.pack(padx=10, pady=5)
    self.lblInformacao.pack(side="top", pady=5)
    self.lblInformacao.config(text="[Ctrl + A] -> Ativar Arvore   [Ctrl + P] -> Ativar Passos   " +
                                   "[Ctrl + G] -> Gerar Textos    [Ctrl + D] -> Abrir Configuração", anchor='s')
    self.btnGerar.config(text="Gerar textos", command= self.GerarGLCEmMemo)
    self.btnGerar.pack(side='left', padx=5)
    self.btnConfiguracao.config(text="Adicionar Gramatica", command= self.AbrirConfiguracao)
    self.btnConfiguracao.pack(side='right', padx=5)
    self.frmPrincipal.bind_all("<Control-a>", lambda event: self.ckxArvore.invoke())
    self.frmPrincipal.bind_all("<Control-p>", lambda event: self.ckxPassoAPasso.invoke())
    self.frmPrincipal.bind_all("<Control-g>", lambda event: self.btnGerar.invoke())
    self.frmPrincipal.bind_all("<Control-d>", lambda event: self.btnConfiguracao.invoke())
    self.frmPrincipal.mainloop()

vJanela = InterfaceGerarGLC()
vJanela.CriarJanela()