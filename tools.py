import pandas as pd
import plotly.graph_objects as go
import numpy as np


def classificacao(dataset, tag, col):

    df = pd.DataFrame(
        dataset[col].value_counts()).reset_index()
    df.rename(columns={'index': 'CLASSIFICACAO_'+tag,
              col: 'TOTAL'}, inplace=True)
    df['porcentagem'] = (df['TOTAL'] / df['TOTAL'].sum()) * 100

    return df


def classificacao_sexo(df, tag, col):

    df_r = pd.DataFrame(df.groupby(by=[col, 'SEXO'])[col].count()).rename(
        columns={col: 'TOTAL'}).reset_index()
    df_r.rename(columns={col: 'CLASSIFICACAO_'+tag}, inplace=True)
    return df_r


def grafico_barra(df, x_col, y_col, name_g, layout):
    colors = ['lightslategray', 'red', 'blue',
              'green', 'yellowgreen', 'yellow']
    f = go.Figure(data=[
        go.Bar(name=name_g,
               x=df[x_col],
               y=df[y_col],
               marker_color=colors)
    ])

    f.update_layout(**layout)

    f.update_layout(barmode='group')

    return f


def grafico_barrar_sexo(df, tag, layout):

    f = go.Figure(data=[
        go.Bar(name='Masculino',
               x=df.query('SEXO == "M"').sort_values(
                   by='TOTAL', ascending=False)[tag],
               y=df.query('SEXO == "M"').sort_values(by='TOTAL', ascending=False)['TOTAL']),
        go.Bar(name='Feminino',
               x=df.query('SEXO == "F"').sort_values(
                   by='TOTAL', ascending=False)[tag],
               y=df.query('SEXO == "F"').sort_values(by='TOTAL', ascending=False)['TOTAL'])
    ])

    f.update_layout(**layout)

    f.update_layout(barmode='group')

    return f


def unique_bairros(df):
    bairro = list(df['BAIRRO'].unique())
    bairro.remove(np.nan)
    return bairro


def agrupamento_bairro(df, bairro: str, col: str):
    estatura = pd.DataFrame(df.groupby(by=['BAIRRO', 'SEXO', col])[
                            col].count()).rename(columns={col: 'TOTAL'}).reset_index()

    for i in estatura['BAIRRO'].unique():
        mask = estatura['BAIRRO'] == i
        estatura.loc[mask, 'PORCENTAGEM_BAIRRO'] = estatura[estatura['BAIRRO']
                                                            == i]['TOTAL'] / estatura[estatura['BAIRRO'] == i]['TOTAL'].sum()

    return estatura[estatura['BAIRRO'] == bairro]


def col_count(df, col):
    c_df = pd.DataFrame(df[col].value_counts()).reset_index()
    c_df.rename(columns={'index': 'CLASSIFICACAO', col: 'TOTAL'}, inplace=True)
    c_df['PORCENTAGEM'] = c_df['TOTAL'] / c_df['TOTAL'].sum()
    return c_df
