from tkinter import *
from tkinter import scrolledtext
from time import sleep
from PIL import ImageTk, Image

class GraficoInterativo:
  rodando = True
  def __init__(self, janela):
    # Gera a janela 
    self.janela = janela
    janela.title("Número de Casos no Brasil")
    janela.geometry("1200x1000")
    janela.iconphoto(False, PhotoImage(file='icones/virus.png'))

    # Gera titulo da janela
    self.titulo = Label(janela, text="Número de casos de Covid-19 no Brasil", 
                        font =('Verdana', 20), )
    self.titulo.grid(row=0, column=1, pady=10,columnspan=2)   

    # Cria scale
    self.v = DoubleVar() 
    self.scale = Scale(variable = self.v, from_ = 0, to = 272, orient = HORIZONTAL, length=400, width=15, showvalue=0, command=self.printar_imagem)  
    self.scale.grid(row=2,column=1, columnspan=2, pady=(10,0))

    # Primeiros gráficos na janela
  
    dia_inicial_grande = Image.open("mapas/0.png")
    dia_inicial_pequeno = dia_inicial_grande.resize((600, 450), Image.ANTIALIAS)
    dia_inicial = ImageTk.PhotoImage(dia_inicial_pequeno)

    self.imagem1 = Label(self.janela, image=dia_inicial)
    self.imagem1.image = dia_inicial
    self.imagem1.grid(row=1, column=0, columnspan=2, padx=(20,10), pady=(15,0))

    dia_inicial_grande = Image.open("graficos/0.png")
    dia_inicial_pequeno = dia_inicial_grande.resize((800, 500), Image.ANTIALIAS)
    dia_inicial = ImageTk.PhotoImage(dia_inicial_pequeno)
    
    self.imagem2 = Label(self.janela, image=dia_inicial)
    self.imagem2.image = dia_inicial
    self.imagem2.grid(row=1, column=2, columnspan=2, padx=(0,10), pady=(15,0))

    # Cria botão

    pad_y = 0
    pad_x = 0
    self.botao_iniciar = Button(text="Iniciar",command=self.avancar)
    self.botao_iniciar.grid(row=3,column=1,pady=pad_y, padx=(pad_x,0))

    self.botao_parar = Button(text="Parar",command=self.parar, state=DISABLED)
    self.botao_parar.grid(row=3,column=2, pady=10, padx=(0,pad_x))

   
  def printar_imagem(self, event):

    index = int(self.v.get())
    dia_inicial_grande = Image.open(f"mapas/{index}.png")
    dia_inicial_pequeno = dia_inicial_grande.resize((600, 450), Image.ANTIALIAS)
    dia_inicial = ImageTk.PhotoImage(dia_inicial_pequeno)

    self.imagem1 = Label(self.janela, image=dia_inicial)
    self.imagem1.image = dia_inicial
    self.imagem1.grid(row=1, column=0, columnspan=2, padx=(20,10), pady=(15,0))

    dia_inicial_grande = Image.open(f"graficos/{index}.png")
    dia_inicial_pequeno = dia_inicial_grande.resize((800, 500), Image.ANTIALIAS)
    dia_inicial = ImageTk.PhotoImage(dia_inicial_pequeno)
    
    self.imagem2 = Label(self.janela, image=dia_inicial)
    self.imagem2.image = dia_inicial
    self.imagem2.grid(row=1, column=2, columnspan=2, padx=(0,10), pady=(15,0))
    print(f"imagem {index}.png")

  def avancar(self):
    ''' Avança a escala automaticamente quando o botão é pressionado'''

    dias = 7
    if self.v.get() == 272:
      self.parar()
    if self.rodando:
      self.janela.after(400, self.avancar)
      self.botao_iniciar.config(state=DISABLED)
      self.botao_parar.config(state=NORMAL)
    else:
      dias = 0
    self.scale.set(self.v.get() + dias)
    self.rodando = True
    
  def parar(self) :
    self.rodando = False
    self.botao_iniciar.config(state=NORMAL)
    self.botao_parar.config(state=DISABLED)
    
# Iniciando programa

raiz = Tk()

interface = GraficoInterativo(raiz)

raiz.mainloop()    