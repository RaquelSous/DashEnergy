#importa as bibliotecas
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)

#gráfico norte
df0 = pd.read_csv('geracao_ano.csv')
linha = go.Scatter(x = df0['ano'],
                   y = df0['norte'],
                    mode = 'lines',
                    name = 'Geracao [GWh]',
                    line = {'color': '#38aecc'})

df1 = pd.read_csv('consumo_ano.csv')
barra = go.Bar(x = df1['ano'],
                   y = df1['norte'],
                   name = 'Consumo [GWh]',
                   marker = {'color': '#183446'})

config = go.Layout( title ='Consumo Vs Geração [GWh]', 
                                yaxis={'title':'Geração/Consumo [GWh]'},
                                xaxis={'title':''})
trace = [linha, barra]
fig = go.Figure(data=trace, layout=config)

py.iplot(fig)

#grafico nordeste
df0 = pd.read_csv('geracao_ano.csv')
linha = go.Scatter(x = df0['ano'],
                   y = df0['nordeste'],
                    mode = 'lines',
                    name = 'Geracao [GWh]',
                    line = {'color': '#38aecc'})

df1 = pd.read_csv('consumo_ano.csv')
barra = go.Bar(x = df1['ano'],
                   y = df1['nordeste'],
                   name = 'Consumo [GWh]',
                   marker = {'color': '#183446'})

config = go.Layout( title ='Consumo Vs Geração [GWh]', 
                                yaxis={'title':'Geração/Consumo [GWh]'},
                                xaxis={'title':''})
trace = [linha, barra]
fig = go.Figure(data=trace, layout=config)

py.iplot(fig)

#grafico centro oeste
df0 = pd.read_csv('geracao_ano.csv')
linha = go.Scatter(x = df0['ano'],
                   y = df0['centro_oeste'],
                    mode = 'lines',
                    name = 'Geracao [GWh]',
                    line = {'color': '#38aecc'})

df1 = pd.read_csv('consumo_ano.csv')
barra = go.Bar(x = df1['ano'],
                   y = df1['centro_oeste'],
                   name = 'Consumo [GWh]',
                   marker = {'color': '#183446'})

config = go.Layout( title ='Consumo Vs Geração [GWh]', 
                                yaxis={'title':'Geração/Consumo [GWh]'},
                                xaxis={'title':''})
trace = [linha, barra]
fig = go.Figure(data=trace, layout=config)

py.iplot(fig)

#grafico sul
df0 = pd.read_csv('geracao_ano.csv')
linha = go.Scatter(x = df0['ano'],
                   y = df0['sul'],
                    mode = 'lines',
                    name = 'Geracao [GWh]',
                    line = {'color': '#38aecc'})

df1 = pd.read_csv('consumo_ano.csv')
barra = go.Bar(x = df1['ano'],
                   y = df1['sul'],
                   name = 'Consumo [GWh]',
                   marker = {'color': '#183446'})

config = go.Layout( title ='Consumo Vs Geração [GWh]', 
                                yaxis={'title':'Geração/Consumo [GWh]'},
                                xaxis={'title':''})
trace = [linha, barra]
fig = go.Figure(data=trace, layout=config)

py.iplot(fig)

#grafico sudeste
df0 = pd.read_csv('geracao_ano.csv')
linha = go.Scatter(x = df0['ano'],
                   y = df0['sudeste'],
                    mode = 'lines',
                    name = 'Geracao [GWh]',
                    line = {'color': '#38aecc'})

df1 = pd.read_csv('consumo_ano.csv')
barra = go.Bar(x = df1['ano'],
                   y = df1['sudeste'],
                   name = 'Consumo [GWh]',
                   marker = {'color': '#183446'})

config = go.Layout( title ='Consumo Vs Geração [GWh]', 
                                yaxis={'title':'Geração/Consumo [GWh]'},
                                xaxis={'title':''})
trace = [linha, barra]
fig = go.Figure(data=trace, layout=config)

py.iplot(fig)
