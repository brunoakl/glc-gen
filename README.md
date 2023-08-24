###Gerador de Gramática Livre de Contexto(GLC) com interface gráfica.
###Autores(RA): Bruno Machado Ferreira, Ernani Neto, Fábio Gomes e Ryan Henrique Nantes


Testado em:
- Ubuntu 22.04LTS
- Conda 23.1.0
- Python 3.10.9

Divisão de trabalhos:
-Ryan: Interfaces principal e de configuração, revisão de erros, RegEx;
-Ernani: Gramática, aleatoriedade das frases geradas e gravação do screencast;
-Bruno: Escrita do memorial, pesquisa relativa à árvore de derivação e solução de problemas com dependêncas;
-Fábio: pesquisas gerais, auxílio no desenvolvimento de porções do algoritmo;

Preparando para instalar dependências no Conda:
- $ conda create -n LFA
- $ conda activate LFA
- $ conda install python

Para iniciar, abra um terminal na pasta do Gerador e execute o comando:
- $ python Forms_GLCPrincipal.py
Isso abrirá o menu inicial do Gerador, onde há botões para configurar/importar a gramática,
escolher quantas linhas serão geradas e outro para gerar os textos aleatórios. Caso um número de 
linhas não seja escolhido, o programa exibirá um aviso.

Descrição:
O gerador é capaz de gerar, de forma aleatória, frases de forma livre de contexto, podendo gerar a 
quantidade de frases de acordo com a numeração selecionada no combobox, é possível importar uma
gramática que siga o padrão da que está implementada inicialmente e exibida no campo de configuração,
assim como também é possível de se criar sua própria gramática, além de ter implementado o botão de
retroceder, que permite com que as últimas linhas inseridas sejam apagadas unitariamente, assim como
realizar uma limpeza total, além da funcionalidade de poder retornar á gramática padrão utilizada no 
gerador.

Observações importantes: 
- A gramatica importada deve ser no formato .txt, além de seguir a formatação padrão do arquivo 
'teste.txt' que serve de exemplo;
- Ultilizamos como base o código e gramática apresentados no site:
"https://eli.thegreenplace.net/2010/01/28/generating-random-sentences-from-a-context-free-grammar",
que foi fornecido no classroom;
- Também utizamos como auxílio partes do algoritmo geradas por I.A através do ChatGPT-3;
- Algumas janelas de avisos do gerador podem não aparecer sobrepondo as demais janelas, e 
aparecerem mais ao fundo;
- Fechar a janela principal fechará todo o gerador. 



