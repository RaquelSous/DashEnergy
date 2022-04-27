# Bibliotecas
import xlrd
import plotly.graph_objects as go
import plotly.graph_objs as go
import plotly.express as px
import plotly.offline as py
import pandas as pd
import dash
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_core_components as dcc
import re
from plotly.subplots import make_subplots


# Acessa o  arquivo
df = xlrd.open_workbook('202.xls')
tabela = df.sheet_by_name('Tabela 2.14')


coluna = []
dados = []
x = '2012'
for i in range(8):
    for x in range(2):
        j = x + 1
        coluna = tabela.col_values(j)
        dados.append(coluna[10:15])
#print(dados)

# Relação com o ano 2012

h = 0
m = 0
tabela = [[1 for x in range(2)]for x in range(5)]
for q in range(5):
    for l in range(1):
        tabela[h][0] = dados[0][q]
        tabela[h][1] = dados[x][q]
        h += 1
        m += 1
print(tabela)

anos = []
for dado in tabela:
    anos.append(dado[1])
valor = []
for dado in tabela:
    valor.append(dado[0])

barra = go.Bar(x=anos,
               y=valor,
               orientation='h',
               name='Tarifa Média [R$/MWh]',
               marker={'color': '#2178bb'})

config = go.Layout(title='Tarifa Média - 2012',
                   yaxis={'title': 'Regiões'},
                   xaxis={'title': 'Dados anuais'})
trace = [barra]
fig1 = go.Figure(data=trace, layout=config)

fig1.show()

# -------------------------------------------------------------------------- 2013
#Acessa o arquivo
df = xlrd.open_workbook('202.xls')
tabela = df.sheet_by_name('Tabela 2.14')

# 2013
coluna = []
dados = []
x = '2013'
for i in range(8):
    for x in range(3):
        j = x + 1
        coluna = tabela.col_values(j)
        dados.append(coluna[10:15])
#print(dados)

# Relação com o ano 2013

h = 0
m = 0
tabela = [[1 for x in range(2)]for x in range(5)]
for q in range(5):
    for l in range(1):
        tabela[h][0] = dados[0][q]
        tabela[h][1] = dados[x][q]
        h += 1
        m += 1
print(tabela)

anos = []
for dado in tabela:
    anos.append(dado[1])
valor = []
for dado in tabela:
    valor.append(dado[0])

barra = go.Bar(x=anos,
               y=valor,
               orientation='h',
               name='Tarifa Média [R$/MWh]',
               marker={'color': '#2178bb'})

config = go.Layout(title='Tarifa Média - 2013',
                   yaxis={'title': 'Regiões'},
                   xaxis={'title': 'Dados anuais'})
trace = [barra]
fig2 = go.Figure(data=trace, layout=config)

fig2.show()

# ------------------------------------------------------ 2014
df = xlrd.open_workbook('202.xls')
tabela = df.sheet_by_name('Tabela 2.14')

coluna = []
dados = []
x = '2014'
for i in range(8):
    for x in range(4):
        j = x + 1
        coluna = tabela.col_values(j)
        dados.append(coluna[10:15])
#print(dados)

# Relação com o ano 2014

h = 0
m = 0
tabela = [[1 for x in range(2)]for x in range(5)]
for q in range(5):
    for l in range(1):
        tabela[h][0] = dados[0][q]
        tabela[h][1] = dados[x][q]
        h += 1
        m += 1
print(tabela)

anos = []
for dado in tabela:
    anos.append(dado[1])
valor = []
for dado in tabela:
    valor.append(dado[0])

barra = go.Bar(x=anos,
               y=valor,
               orientation='h',
               name='Tarifa Média [R$/MWh]',
               marker={'color': '#2178bb'})

config = go.Layout(title='Tarifa Média - 2014',
                   yaxis={'title': 'Regiões'},
                   xaxis={'title': 'Dados anuais'})
trace = [barra]
fig3 = go.Figure(data=trace, layout=config)

fig3.show()

# ------------------------------------------------------ 2015
df = xlrd.open_workbook('202.xls')
tabela = df.sheet_by_name('Tabela 2.14')

coluna = []
dados = []
x = '2015'
for i in range(8):
    for x in range(5):
        j = x + 1
        coluna = tabela.col_values(j)
        dados.append(coluna[10:15])
#print(dados)

# Relação com o ano 2015

h = 0
m = 0
tabela = [[1 for x in range(2)]for x in range(5)]
for q in range(5):
    for l in range(1):
        tabela[h][0] = dados[0][q]
        tabela[h][1] = dados[x][q]
        h += 1
        m += 1
print(tabela)

anos = []
for dado in tabela:
    anos.append(dado[1])
valor = []
for dado in tabela:
    valor.append(dado[0])

barra = go.Bar(x=anos,
               y=valor,
               orientation='h',
               name='Tarifa Média [R$/MWh]',
               marker={'color': '#2178bb'})

config = go.Layout(title='Tarifa Média - 2015',
                   yaxis={'title': 'Regiões'},
                   xaxis={'title': 'Dados anuais'})
trace = [barra]
fig4 = go.Figure(data=trace, layout=config)

fig4.show()

# ----------------------------------------------------- 2016
df = xlrd.open_workbook('202.xls')
tabela = df.sheet_by_name('Tabela 2.14')

coluna = []
dados = []
x = '2016'
for i in range(8):
    for x in range(6):
        j = x + 1
        coluna = tabela.col_values(j)
        dados.append(coluna[10:15])
#print(dados)

# Relação com o ano 2016

h = 0
m = 0
tabela = [[1 for x in range(2)]for x in range(5)]
for q in range(5):
    for l in range(1):
        tabela[h][0] = dados[0][q]
        tabela[h][1] = dados[x][q]
        h += 1
        m += 1
print(tabela)

anos = []
for dado in tabela:
    anos.append(dado[1])
valor = []
for dado in tabela:
    valor.append(dado[0])

barra = go.Bar(x=anos,
               y=valor,
               orientation='h',
               name='Tarifa Média [R$/MWh]',
               marker={'color': '#2178bb'})

config = go.Layout(title='Tarifa Média - 2016',
                   yaxis={'title': 'Regiões'},
                   xaxis={'title': 'Dados anuais'})
trace = [barra]
fig5 = go.Figure(data=trace, layout=config)

fig5.show()

# ----------------------------------------------------- 2017
df = xlrd.open_workbook('202.xls')
tabela = df.sheet_by_name('Tabela 2.14')

coluna = []
dados = []
x = '2017'
for i in range(8):
    for x in range(7):
        j = x + 1
        coluna = tabela.col_values(j)
        dados.append(coluna[10:15])
#print(dados)

# Relação com o ano 2017

h = 0
m = 0
tabela = [[1 for x in range(2)]for x in range(5)]
for q in range(5):
    for l in range(1):
        tabela[h][0] = dados[0][q]
        tabela[h][1] = dados[x][q]
        h += 1
        m += 1
print(tabela)

anos = []
for dado in tabela:
    anos.append(dado[1])
valor = []
for dado in tabela:
    valor.append(dado[0])

barra = go.Bar(x=anos,
               y=valor,
               orientation='h',
               name='Tarifa Média [R$/MWh]',
               marker={'color': '#2178bb'})

config = go.Layout(title='Tarifa Média - 2017',
                   yaxis={'title': 'Regiões'},
                   xaxis={'title': 'Dados anuais'})
trace = [barra]
fig6 = go.Figure(data=trace, layout=config)

fig6.show()

# -------------------------------------------------------- 2018
df = xlrd.open_workbook('202.xls')
tabela = df.sheet_by_name('Tabela 2.14')

coluna = []
dados = []
x = '2018'
for i in range(8):
    for x in range(8):
        j = x + 1
        coluna = tabela.col_values(j)
        dados.append(coluna[10:15])
#print(dados)

# Relação com o ano 2018

h = 0
m = 0
tabela = [[1 for x in range(2)]for x in range(5)]
for q in range(5):
    for l in range(1):
        tabela[h][0] = dados[0][q]
        tabela[h][1] = dados[x][q]
        h += 1
        m += 1
print(tabela)

anos = []
for dado in tabela:
    anos.append(dado[1])
valor = []
for dado in tabela:
    valor.append(dado[0])

barra = go.Bar(x=anos,
               y=valor,
               orientation='h',
               name='Tarifa Média [R$/MWh]',
               marker={'color': '#2178bb'})

config = go.Layout(title='Tarifa Média - 2018',
                   yaxis={'title': 'Regiões'},
                   xaxis={'title': 'Dados anuais'})
trace = [barra]
fig7 = go.Figure(data=trace, layout=config)

fig7.show()

# --------------------------------------------------Dashboard
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Tarifa Média por Região [R$/MWh]', style={'text-align': 'center'}),
    html.Hr(),
    html.Div([
        dcc.Dropdown(id='demo-dropdown',
                    options=[
                        {'label': '2012', 'value': '2012'},
                        {'label': '2013', 'value': '2013'},
                        {'label': '2014', 'value': '2014'},
                        {'label': '2015', 'value': '2015'},
                        {'label': '2016', 'value': '2016'},
                        {'label': '2017', 'value': '2017'},
                        {'label': '2018', 'value': '2018'},
                    ],
                     value='2012'),
    ], style={'color': 'blue', 'width': '40%'}),
    dcc.Graph(id='fig1')
], style={'background': '#e8ecf4', 'color': 'white'})

@app.callback(
    dash.dependencies.Output('fig1', 'figure'),
    [dash.dependencies.Input('demo-dropdown', 'value')]
)
def grafico(x):
    if x == '2012':
        return fig1
    if x == '2013':
        return fig2
    if x == '2014':
        return fig3
    if x == '2015':
        return fig4
    if x == '2016':
        return fig5
    if x == '2017':
        return fig6
    if x == '2018':
        return fig7


if __name__== '__main__':
    app.run_server()

