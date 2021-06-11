import pandas as pd
import plotly.graph_objects as go


def classificacao(dataset, tag, col):

    df = pd.DataFrame(
        dataset[col].value_counts()).reset_index()
    df.rename(columns={'index': 'class_'+tag,
              col: 'total'}, inplace=True)
    df['porcentagem'] = (df['total'] / df['total'].sum()) * 100
    return df


def classificacao_sexo(df, tag, col):

    df_r = pd.DataFrame(df.groupby(by=[col, 'SEXO'])[col].count()).rename(
        columns={col: 'total'}).reset_index()
    df_r.rename(columns={'SEXO': 'sexo',
                col: 'class_'+tag}, inplace=True)
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
               x=df.query('sexo == "M"').sort_values(
                   by='total', ascending=False)['class_'+tag],
               y=df.query('sexo == "M"').sort_values(by='total', ascending=False)['total']),
        go.Bar(name='Feminino',
               x=df.query('sexo == "F"').sort_values(
                   by='total', ascending=False)['class_'+tag],
               y=df.query('sexo == "F"').sort_values(by='total', ascending=False)['total'])
    ])

    f.update_layout(**layout)

    f.update_layout(barmode='group')

    return f
