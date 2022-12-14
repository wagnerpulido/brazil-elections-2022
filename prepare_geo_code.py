import pandas as pd

drops = [
# 'id_municipio_tse',
# 'id_municipio',
 'ano',
 'turno',
 'zona',
 'secao',
 'aptos',
 'comparecimento',
 'abstencoes',
 'votos_nominais',
 'votos_brancos',
 'votos_nulos',
 'votos_coligacao',
 'votos_nulos_apu_sep',
 'votos_pendentes',
 'proporcao_comparecimento',
 'proporcao_votos_nominais',
 'proporcao_votos_coligacao',
 'proporcao_votos_brancos',
 'proporcao_votos_nulos'
]

def get_code_ibge_tse(uf):
    iter_csv = pd.read_csv('data/detalhes_votacao_secao.csv', iterator=True, chunksize=10000)
    df = pd.concat([chunk[(chunk['ano'] == 2022) & (chunk['sigla_uf'] == uf)] for chunk in iter_csv])
    codes = df.groupby(['id_municipio_tse', 'id_municipio'], as_index=False).sum()
    codes = codes.astype({'id_municipio_tse': int})
    codes = codes.astype({'id_municipio': int})
    codes = codes.drop(columns=drops)
    return codes

def add_ibge_code(df, uf):
    codes = get_code_ibge_tse(uf)
    df_by_city = df.groupby(['NM_MUNICIPIO', 'CD_MUNICIPIO'], as_index=False).sum()
    df_by_city = df_by_city.merge(codes, left_on='CD_MUNICIPIO', right_on='id_municipio_tse')
    return df_by_city
