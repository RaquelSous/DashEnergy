import plotly.offline as py
import plotly.graph_objs as go
#py.init_notebook_mode(connected=True)

#Norte Geração
# abre o arquivo
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.4.csv")
# f.read lê todo o conteúdo do arquivo e retorna uma string
# .split("\n") divide essa string do conteudo em linhas
content = f.read().split("\n")
#lista vazia que armazena os anos
years = []
#for lê a oitava linha que contem os anos dentro do arquivo csv
#.split(",") separa elementos por vírgula da lista, começando pelo elemento 2 e excluindo os últimos 4
for y in content[8].split(",")[2:-4]:
    #insere na lista years cada elemento de y transformado de string para inteiro
    years.append (int(y))
#lista vazia que armazena energia de cada região
data = []
#for lê todas as linhas da lista
for l in content:
    #.split(",") separa por vírgula
    ls = l.split(",")
    #condiciona que se o elemento 1 da lista for igual à "Norte" prossigo
    if ls[1] == "Norte":
        #determina o começo e fim da lista, partindo do elemento 2 e excluindo os últimos 5
        dt = ls[2:-5]
        #lê cada elemento da lista filtrada
        for l in dt:
            #insere na lista data cada elemento l transformado de string para float
            data.append(float(l))
        
#variável que armazena informações do gráfico       
linha = go.Scatter(x = years, #anos do gráfico, eixo x
                   y = data, #energia do gráfico, eixo y
                   mode = 'lines', #modo do gráfico, tipo linhas
                   name = 'Geracao [GWh]', #nome das linhas, no caso geração
                   line = {'color': '#38aecc'}) #cor das linhas
#Norte Consumo
# abre o arquivo
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 3.1.csv")
# f.read lê todo o conteúdo do arquivo e retorna uma string
# .split("\n") divide essa string do conteudo em linhas
content = f.read().split("\n")
#insere na lista years cada elemento de y transformado de string para inteiro
years = []
#for lê a oitava linha que contem os anos dentro do arquivo csv
#.split(",") separa elementos por vírgula da lista, começando pelo elemento 2 e excluindo os últimos 4
for y in content[8].split(",")[2:-4]:
    #insere na lista years cada elemento de y transformado de string para inteiro
    years.append (int(y))
#lista vazia que armazena energia de cada região
data = []
#for lê todas as linhas da lista
for l in content:
    #.split(",") separa por vírgula
    ls = l.split(",")
    #condiciona que se o elemento 1 da lista for igual à "Norte" prossigo
    if ls[1] == "Norte":
        #determina o começo e fim da lista, partindo do elemento 2 e excluindo os últimos 5
        dt = ls[2:-5]
        #lê cada elemento da lista filtrada
        for l in dt:
            #insere na lista data cada elemento l transformado de string para float
            data.append(float(l))
#variável que armazena informações do gráfico
barra = go.Bar(x = years,#anos do gráfico, eixo x
                   y = data, #energia do gráfico, eixo y
                   name = 'Consumo [GWh]',#nome das barras, no caso geração
                   marker = {'color': '#183446'})#cor das barras


config = go.Layout( title ='Consumo Vs Geração [GWh]', #título do gráfico
                                yaxis={'title':'Geração/Consumo [GWh]'}, #título eixo y
                                xaxis={'title':''}) #título eixo x
trace = [linha, barra] #variável que armazena gráficos
fig = go.Figure(data=trace, layout=config) #transforma em fig os gráficos com o layout determinado

fig.show() #plot fig

#Nordeste Geração
# abre o arquivo
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.4.csv")
# f.read lê todo o conteúdo do arquivo e retorna uma string
# .split("\n") divide essa string do conteudo em linhas
content = f.read().split("\n")
#lista vazia que armazena os anos
years = []
#for lê a oitava linha que contem os anos dentro do arquivo csv
#.split(",") separa elementos por vírgula da lista, começando pelo elemento 2 e excluindo os últimos 4
for y in content[8].split(",")[2:-4]:
    #insere na lista years cada elemento de y transformado de string para inteiro
    years.append (int(y))
#lista vazia que armazena energia de cada região
data = []
#for lê todas as linhas da lista
for l in content:
    #.split(",") separa por vírgula
    ls = l.split(",")
    #condiciona que se o elemento 1 da lista for igual à "Nordeste" prossigo
    if ls[1] == "Nordeste":
        #determina o começo e fim da lista, partindo do elemento 2 e excluindo os últimos 5
        dt = ls[2:-5]
        #lê cada elemento da lista filtrada
        for l in dt:
            #insere na lista data cada elemento l transformado de string para float
            data.append(float(l))
        
#variável que armazena informações do gráfico       
linha = go.Scatter(x = years, #anos do gráfico, eixo x
                   y = data, #energia do gráfico, eixo y
                   mode = 'lines', #modo do gráfico, tipo linhas
                   name = 'Geracao [GWh]', #nome das linhas, no caso geração
                   line = {'color': '#38aecc'}) #cor das linhas

#Nordeste Consumo
# abre o arquivo
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 3.1.csv")
# f.read lê todo o conteúdo do arquivo e retorna uma string
# .split("\n") divide essa string do conteudo em linhas
content = f.read().split("\n")
#insere na lista years cada elemento de y transformado de string para inteiro
years = []
#for lê a oitava linha que contem os anos dentro do arquivo csv
#.split(",") separa elementos por vírgula da lista, começando pelo elemento 2 e excluindo os últimos 4
for y in content[8].split(",")[2:-4]:
    #insere na lista years cada elemento de y transformado de string para inteiro
    years.append (int(y))
#lista vazia que armazena energia de cada região
data = []
#for lê todas as linhas da lista
for l in content:
    #.split(",") separa por vírgula
    ls = l.split(",")
    #condiciona que se o elemento 1 da lista for igual à "Nordeste" prossigo
    if ls[1] == "Nordeste":
        #determina o começo e fim da lista, partindo do elemento 2 e excluindo os últimos 5
        dt = ls[2:-5]
        #lê cada elemento da lista filtrada
        for l in dt:
            #insere na lista data cada elemento l transformado de string para float
            data.append(float(l))
#variável que armazena informações do gráfico
barra = go.Bar(x = years,#anos do gráfico, eixo x
                   y = data, #energia do gráfico, eixo y
                   name = 'Consumo [GWh]',#nome das barras, no caso geração
                   marker = {'color': '#183446'})#cor das barras


config = go.Layout( title ='Consumo Vs Geração na Região Norte [GWh]', #título do gráfico
                                yaxis={'title':'Geração/Consumo [GWh]'}, #título eixo y
                                xaxis={'title':''}) #título eixo x
trace = [linha, barra] #variável que armazena gráficos
fig = go.Figure(data=trace, layout=config) #transforma em fig os gráficos com o layout determinado

fig.show() #plot fig

#Centro-Oeste Geração
# abre o arquivo
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.4.csv")
# f.read lê todo o conteúdo do arquivo e retorna uma string
# .split("\n") divide essa string do conteudo em linhas
content = f.read().split("\n")
#lista vazia que armazena os anos
years = []
#for lê a oitava linha que contem os anos dentro do arquivo csv
#.split(",") separa elementos por vírgula da lista, começando pelo elemento 2 e excluindo os últimos 4
for y in content[8].split(",")[2:-4]:
    #insere na lista years cada elemento de y transformado de string para inteiro
    years.append (int(y))
#lista vazia que armazena energia de cada região
data = []
#for lê todas as linhas da lista
for l in content:
    #.split(",") separa por vírgula
    ls = l.split(",")
    #condiciona que se o elemento 1 da lista for igual à "Centro-Oeste" prossigo
    if ls[1] == "Centro-Oeste":
        #determina o começo e fim da lista, partindo do elemento 2 e excluindo os últimos 5
        dt = ls[2:-5]
        #lê cada elemento da lista filtrada
        for l in dt:
            #insere na lista data cada elemento l transformado de string para float
            data.append(float(l))
        
#variável que armazena informações do gráfico       
linha = go.Scatter(x = years, #anos do gráfico, eixo x
                   y = data, #energia do gráfico, eixo y
                   mode = 'lines', #modo do gráfico, tipo linhas
                   name = 'Geracao [GWh]', #nome das linhas, no caso geração
                   line = {'color': '#38aecc'}) #cor das linhas

#Centro-Oeste Consumo
# abre o arquivo
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 3.1.csv")
# f.read lê todo o conteúdo do arquivo e retorna uma string
# .split("\n") divide essa string do conteudo em linhas
content = f.read().split("\n")
#insere na lista years cada elemento de y transformado de string para inteiro
years = []
#for lê a oitava linha que contem os anos dentro do arquivo csv
#.split(",") separa elementos por vírgula da lista, começando pelo elemento 2 e excluindo os últimos 4
for y in content[8].split(",")[2:-4]:
    #insere na lista years cada elemento de y transformado de string para inteiro
    years.append (int(y))
#lista vazia que armazena energia de cada região
data = []
#for lê todas as linhas da lista
for l in content:
    #.split(",") separa por vírgula
    ls = l.split(",")
    #condiciona que se o elemento 1 da lista for igual à "Centro-Oeste" prossigo
    if ls[1] == "Centro-Oeste":
        #determina o começo e fim da lista, partindo do elemento 2 e excluindo os últimos 5
        dt = ls[2:-5]
        #lê cada elemento da lista filtrada
        for l in dt:
            #insere na lista data cada elemento l transformado de string para float
            data.append(float(l))
#variável que armazena informações do gráfico
barra = go.Bar(x = years,#anos do gráfico, eixo x
                   y = data, #energia do gráfico, eixo y
                   name = 'Consumo [GWh]',#nome das barras, no caso geração
                   marker = {'color': '#183446'})#cor das barras


config = go.Layout( title ='Consumo Vs Geração na Região Nordeste [GWh]', #título do gráfico
                                yaxis={'title':'Geração/Consumo [GWh]'}, #título eixo y
                                xaxis={'title':''}) #título eixo x
trace = [linha, barra] #variável que armazena gráficos
fig = go.Figure(data=trace, layout=config) #transforma em fig os gráficos com o layout determinado

fig.show() #plot fig

#Sul Geração
# abre o arquivo
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.4.csv")
# f.read lê todo o conteúdo do arquivo e retorna uma string
# .split("\n") divide essa string do conteudo em linhas
content = f.read().split("\n")
#lista vazia que armazena os anos
years = []
#for lê a oitava linha que contem os anos dentro do arquivo csv
#.split(",") separa elementos por vírgula da lista, começando pelo elemento 2 e excluindo os últimos 4
for y in content[8].split(",")[2:-4]:
    #insere na lista years cada elemento de y transformado de string para inteiro
    years.append (int(y))
#lista vazia que armazena energia de cada região
data = []
#for lê todas as linhas da lista
for l in content:
    #.split(",") separa por vírgula
    ls = l.split(",")
    #condiciona que se o elemento 1 da lista for igual à "Sul" prossigo
    if ls[1] == "Sul":
        #determina o começo e fim da lista, partindo do elemento 2 e excluindo os últimos 5
        dt = ls[2:-5]
        #lê cada elemento da lista filtrada
        for l in dt:
            #insere na lista data cada elemento l transformado de string para float
            data.append(float(l))
        
#variável que armazena informações do gráfico       
linha = go.Scatter(x = years, #anos do gráfico, eixo x
                   y = data, #energia do gráfico, eixo y
                   mode = 'lines', #modo do gráfico, tipo linhas
                   name = 'Geracao [GWh]', #nome das linhas, no caso geração
                   line = {'color': '#38aecc'}) #cor das linhas

#Sul Consumo
# abre o arquivo
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 3.1.csv")
# f.read lê todo o conteúdo do arquivo e retorna uma string
# .split("\n") divide essa string do conteudo em linhas
content = f.read().split("\n")
#insere na lista years cada elemento de y transformado de string para inteiro
years = []
#for lê a oitava linha que contem os anos dentro do arquivo csv
#.split(",") separa elementos por vírgula da lista, começando pelo elemento 2 e excluindo os últimos 4
for y in content[8].split(",")[2:-4]:
    #insere na lista years cada elemento de y transformado de string para inteiro
    years.append (int(y))
#lista vazia que armazena energia de cada região
data = []
#for lê todas as linhas da lista
for l in content:
    #.split(",") separa por vírgula
    ls = l.split(",")
    #condiciona que se o elemento 1 da lista for igual à "Sul" prossigo
    if ls[1] == "Sul":
        #determina o começo e fim da lista, partindo do elemento 2 e excluindo os últimos 5
        dt = ls[2:-5]
        #lê cada elemento da lista filtrada
        for l in dt:
            #insere na lista data cada elemento l transformado de string para float
            data.append(float(l))
#variável que armazena informações do gráfico
barra = go.Bar(x = years,#anos do gráfico, eixo x
                   y = data, #energia do gráfico, eixo y
                   name = 'Consumo [GWh]',#nome das barras, no caso geração
                   marker = {'color': '#183446'})#cor das barras


config = go.Layout( title ='Consumo Vs Geração na Região Centro-Oeste [GWh]', #título do gráfico
                                yaxis={'title':'Geração/Consumo [GWh]'}, #título eixo y
                                xaxis={'title':''}) #título eixo x
trace = [linha, barra] #variável que armazena gráficos
fig = go.Figure(data=trace, layout=config) #transforma em fig os gráficos com o layout determinado

fig.show() #plot fig

#Sudeste Geração
# abre o arquivo
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 2.4.csv")
# f.read lê todo o conteúdo do arquivo e retorna uma string
# .split("\n") divide essa string do conteudo em linhas
content = f.read().split("\n")
#lista vazia que armazena os anos
years = []
#for lê a oitava linha que contem os anos dentro do arquivo csv
#.split(",") separa elementos por vírgula da lista, começando pelo elemento 2 e excluindo os últimos 4
for y in content[8].split(",")[2:-4]:
    #insere na lista years cada elemento de y transformado de string para inteiro
    years.append (int(y))
#lista vazia que armazena energia de cada região
data = []
#for lê todas as linhas da lista
for l in content:
    #.split(",") separa por vírgula
    ls = l.split(",")
    #condiciona que se o elemento 1 da lista for igual à "Sudeste" prossigo
    if ls[1] == "Sudeste":
        #determina o começo e fim da lista, partindo do elemento 2 e excluindo os últimos 5
        dt = ls[2:-5]
        #lê cada elemento da lista filtrada
        for l in dt:
            #insere na lista data cada elemento l transformado de string para float
            data.append(float(l))
        
#variável que armazena informações do gráfico       
linha = go.Scatter(x = years, #anos do gráfico, eixo x
                   y = data, #energia do gráfico, eixo y
                   mode = 'lines', #modo do gráfico, tipo linhas
                   name = 'Geracao [GWh]', #nome das linhas, no caso geração
                   line = {'color': '#38aecc'}) #cor das linhas

#Sudeste Consumo
# abre o arquivo
f = open("Anuário Estatístico de Energia Elétrica 2020 - Workbook.xlsx - Tabela 3.1.csv")
# f.read lê todo o conteúdo do arquivo e retorna uma string
# .split("\n") divide essa string do conteudo em linhas
content = f.read().split("\n")
#insere na lista years cada elemento de y transformado de string para inteiro
years = []
#for lê a oitava linha que contem os anos dentro do arquivo csv
#.split(",") separa elementos por vírgula da lista, começando pelo elemento 2 e excluindo os últimos 4
for y in content[8].split(",")[2:-4]:
    #insere na lista years cada elemento de y transformado de string para inteiro
    years.append (int(y))
#lista vazia que armazena energia de cada região
data = []
#for lê todas as linhas da lista
for l in content:
    #.split(",") separa por vírgula
    ls = l.split(",")
    #condiciona que se o elemento 1 da lista for igual à "Sudeste" prossigo
    if ls[1] == "Sudeste":
        #determina o começo e fim da lista, partindo do elemento 2 e excluindo os últimos 5
        dt = ls[2:-5]
        #lê cada elemento da lista filtrada
        for l in dt:
            #insere na lista data cada elemento l transformado de string para float
            data.append(float(l))
#variável que armazena informações do gráfico
barra = go.Bar(x = years,#anos do gráfico, eixo x
                   y = data, #energia do gráfico, eixo y
                   name = 'Consumo [GWh]',#nome das barras, no caso geração
                   marker = {'color': '#183446'})#cor das barras


config = go.Layout( title ='Consumo Vs Geração na Região Sudeste [GWh]', #título do gráfico
                                yaxis={'title':'Geração/Consumo [GWh]'}, #título eixo y
                                xaxis={'title':''}) #título eixo x
trace = [linha, barra] #variável que armazena gráficos
fig = go.Figure(data=trace, layout=config) #transforma em fig os gráficos com o layout determinado

fig.show() #plot fig
