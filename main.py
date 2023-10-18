from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import os


# Criando a janela e estabelecendo parâmetros
janela = Tk()
janela.title('App do Tempo')
janela.geometry('900x500')
janela.resizable(False, False)


chave_api = os.getenv('chave')


# Funcao do botao


def pegar_previsao():
    try:
        cidade = campo_texto.get()
        geolocador = Nominatim(user_agent='geoapiExercised')
        localizacao = geolocador.geocode(cidade)
        obj = TimezoneFinder()
        resultado = obj.timezone_at(lng=localizacao.longitude, lat=localizacao.latitude)

        home = pytz.timezone(resultado)
        hora_local = datetime.now(home)
        hora_atual = hora_local.strftime('%I:%M %p')
        relogio.config(text=hora_atual)
        nome.config(text=f' Atualmente em {cidade}')

        # API da previsão

        api = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&lang=pt&units=metric&appid={chave_api}'
        dados_json = requests.get(api).json()
        condicao = dados_json['weather'][0]['description']
        condicao.strip('{}')
        descricao = dados_json['weather'][0]['description']
        temperatura = int(dados_json['main']['temp'])
        pressao = dados_json['main']['pressure']
        umidade = dados_json['main']['humidity']
        vento = dados_json['wind']['speed']

        t.config(text=(temperatura,'º'))
        c.config(text=f'{condicao} | SENSAÇÂO DE {temperatura}º')
        w.config(text=f'{vento} m/s')
        h.config(text=f'{umidade} %')
        d.config(text=descricao)
        p.config(text=f'{pressao} hPa')

    except Exception as e:
        messagebox.showerror('App de Previsão', 'Cidade Inválida')


# Caixa de pesquisa

imagem_pesquisa = PhotoImage(file='Copy of search.png')
minha_imagem = Label(image=imagem_pesquisa)
minha_imagem.place(x=20,y=20)

campo_texto = tk.Entry(janela,justify='center', width=17,font=('poppins',25,'bold'), bg='#404040', border=0, fg='white')
campo_texto.place(x=50,y=40)
campo_texto.focus()

icone_pesquisa = PhotoImage(file='Copy of search_icon.png')
meu_icone = Button(janela,image=icone_pesquisa, borderwidth=0,cursor='hand2',bg='#404040', command=pegar_previsao)
meu_icone.place(x=400,y=34)


# Logo

imagem_logo = PhotoImage(file='Copy of logo.png')
logo = Label(image=imagem_logo)
logo.place(x=150,y=120)


# Caixa de baixo

imagem_caixa = PhotoImage(file='Copy of box.png')
minha_imagem_caixa = Label(image=imagem_caixa)
minha_imagem_caixa.pack(padx=5,pady=5,side='bottom')


# Hora

nome = Label(janela,font=('arial',14,'bold'))
nome.place(x=30,y=100)

relogio = Label(janela,font=('Helvetica',20))
relogio.place(x=30,y=130)


# Labels

label1 = Label(janela,text='Vento', font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')
label1.place(x=120,y=400)

label2 = Label(janela,text='Umidade', font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')
label2.place(x=250,y=400)

label3 = Label(janela,text='Descrição', font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')
label3.place(x=430,y=400)

label4 = Label(janela,text='Pressão atmosférica ', font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')
label4.place(x=600,y=400)

t = Label(font=('arial', 70, 'bold'),fg='#ee666d')
t.place(x=400,y=150)

c = Label(font=('arial',15,'bold'))
c.place(x=400,y=250)


w = Label(text='...',font=('arial',18,'bold'),bg='#1ab5ef')
w.place(x=120,y=430)

h = Label(text='...',font=('arial',18,'bold'),bg='#1ab5ef')
h.place(x=280,y=430)

d = Label(text='...',font=('arial',18,'bold'),bg='#1ab5ef')
d.place(x=420,y=430)

p = Label(text='...',font=('arial',18,'bold'),bg='#1ab5ef')
p.place(x=660,y=430)


janela.mainloop()


