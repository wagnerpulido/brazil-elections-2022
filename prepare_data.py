import numpy as np
import pandas as pd
import os.path
import wget
import zipfile
from util import *

def get_file_name(turno, estado):
    if turno == '1t':
        return f'bweb_1t_{estado}_051020221321'
    else:
        return f'bweb_2t_{estado}_311020221535'

def call_data(item):
    zip_file_name = item + '.zip'
    csv_file_path = 'data/' + item + '.csv'
    if not os.path.exists(csv_file_path):
        wget.download(f'{root_host}{zip_file_name}')
    if not os.path.exists(csv_file_path):
        with zipfile.ZipFile(f'{zip_file_name}', 'r') as zip_ref:
            zip_ref.extractall('data')
    if os.path.exists(zip_file_name):
        os.remove(zip_file_name)

def read_df(file_name, cargo):
    iter_csv = pd.read_csv('data/' + file_name + ".csv", sep=';', encoding='latin-1', iterator=True, chunksize=10000)
    dataframe = pd.concat([chunk[chunk["DS_CARGO_PERGUNTA"] == cargo] for chunk in iter_csv])
    dataframe = dataframe.drop(columns=drop_col)
    return dataframe

def read_cidades(file_name):
    iter_csv = pd.read_csv('data/' + file_name + ".csv", sep=';', encoding='latin-1', iterator=True, chunksize=10000)
    dataframe = pd.concat([chunk[chunk["DS_CARGO_PERGUNTA"] == 'Presidente'] for chunk in iter_csv])
    dataframe = dataframe.drop(columns=drop_not_cidade)
    cidades = dataframe['NM_MUNICIPIO'].unique().tolist()
    return cidades


# create a list of our conditions
def add_modelo_urna(df):
    conditions = [
        (df['NR_URNA_EFETIVADA'] <= 1220500),
        (df['NR_URNA_EFETIVADA'] >= 1220501) & (df['NR_URNA_EFETIVADA'] <= 1345500),
        (df['NR_URNA_EFETIVADA'] >= 1368501) & (df['NR_URNA_EFETIVADA'] <= 1370500),
        (df['NR_URNA_EFETIVADA'] >= 1600000) & (df['NR_URNA_EFETIVADA'] <= 1650000),
        (df['NR_URNA_EFETIVADA'] >= 1650001) & (df['NR_URNA_EFETIVADA'] <= 1701000),
        (df['NR_URNA_EFETIVADA'] >= 1750000) & (df['NR_URNA_EFETIVADA'] <= 1950000),
        (df['NR_URNA_EFETIVADA'] >= 2000000) & (df['NR_URNA_EFETIVADA'] <= 2250000)
    ]

    # create a list of the values we want to assign for each condition
    values = ['2009', '2010', '2011', '2011', '2013', '2015', '2020']

    # create a new column and use np.select to assign values to it using our lists as arguments
    df['DS_MODELO_URNA'] = np.select(conditions, values)

    # display updated DataFrame
    df.head()


def add_is2020(df):
    df['IS_2020'] = np.where(df['DS_MODELO_URNA'] == '2020', '2020', 'OUTRAS')

def drop_capitais(df):
    df = df[~df['NM_MUNICIPIO'].isin(capitais)]
    return df
