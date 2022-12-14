states_center = {
	'AC': [-8.77, -70.55],
	'AL': [-9.62, -36.82],
	'AM': [-3.47, -65.10],
	'AP': [1.41, -51.77],
	'BA': [-13.29, -41.71],
	'CE': [-5.20, -39.53],
	'DF': [-15.83, -47.86],
	'ES': [-19.19, -40.34],
	'GO': [-15.98, -49.86],
	'MA': [-5.42, -45.44],
	'MT': [-12.64, -55.42],
	'MS': [-20.51, -54.54],
	'MG': [-18.10, -44.38],
	'PA': [-3.79, -52.48],
	'PB': [-7.28, -36.72],
	'PR': [-24.89, -51.55],
	'PE': [-8.38, -37.86],
	'PI': [-6.60, -42.28],
	'RJ': [-22.25, -42.66],
	'RN': [-5.81, -36.59],
	'RO': [-10.83, -63.34],
	'RS': [-30.17, -53.50],
	'RR': [1.99, -61.33],
	'SC': [-27.45, -50.95],
	'SE': [-10.57, -37.45],
	'SP': [-22.19, -48.79],
	'TO': [-9.46, -48.26]
}

state_number = {#Região Norte
	'AC' : 12,
	'AM' : 13,
	'AP' : 16,
	'PA' : 15,
	'RO' : 11,
	'RR' : 14,
	'TO' : 17,
	#'Região Nordeste
	'AL' : 27,
	'BA' : 29,
	'CE' : 23,
	'MA' : 21,
	'PB' : 25,
	'PE' : 26,
	'PI' : 22,
	'RN' : 24,
	'SE' : 28,
	#Região Sudeste
	'ES' : 32,
	'MG' : 31,
	'RJ' : 33,
	'SP' : 35,
	#Região Sul
	'PR' : 41,
	'RS' : 43,
	'SC' : 42,
	#Região Centro-Oeste
	'DF' : 53,
	'GO' : 52,
	'MT' : 51,
	'MS' : 50
}


bus = [
'bweb_2t_AC_311020221535', 'bweb_2t_AL_311020221535', 'bweb_2t_AM_311020221535', 'bweb_2t_AP_311020221535',
'bweb_2t_BA_311020221535', 'bweb_2t_CE_311020221535', 'bweb_2t_DF_311020221535', 'bweb_2t_ES_311020221535',
'bweb_2t_GO_311020221535', 'bweb_2t_MA_311020221535', 'bweb_2t_MG_311020221535', 'bweb_2t_MS_311020221535',
'bweb_2t_MT_311020221535', 'bweb_2t_PA_311020221535', 'bweb_2t_PB_311020221535', 'bweb_2t_PE_311020221535',
'bweb_2t_PI_311020221535', 'bweb_2t_PR_311020221535', 'bweb_2t_RJ_311020221535', 'bweb_2t_RN_311020221535',
'bweb_2t_RO_311020221535', 'bweb_2t_RR_311020221535', 'bweb_2t_RS_311020221535', 'bweb_2t_SC_311020221535',
'bweb_2t_SE_311020221535', 'bweb_2t_SP_311020221535', 'bweb_2t_TO_311020221535', 'bweb_2t_ZZ_311020221535',
'bweb_1t_AC_051020221321', 'bweb_1t_AL_051020221321', 'bweb_1t_AM_051020221321', 'bweb_1t_AP_051020221321',
'bweb_1t_BA_051020221321', 'bweb_1t_CE_051020221321', 'bweb_1t_DF_051020221321', 'bweb_1t_ES_051020221321',
'bweb_1t_GO_051020221321', 'bweb_1t_MA_051020221321', 'bweb_1t_MG_051020221321', 'bweb_1t_MS_051020221321',
'bweb_1t_MT_051020221321', 'bweb_1t_PA_051020221321', 'bweb_1t_PB_051020221321', 'bweb_1t_PE_051020221321',
'bweb_1t_PI_051020221321', 'bweb_1t_PR_051020221321', 'bweb_1t_RJ_051020221321', 'bweb_1t_RN_051020221321',
'bweb_1t_RO_051020221321', 'bweb_1t_RR_051020221321', 'bweb_1t_RS_051020221321', 'bweb_1t_SC_051020221321',
'bweb_1t_SE_051020221321', 'bweb_1t_SP_051020221321', 'bweb_1t_TO_051020221321', 'bweb_1t_ZZ_051020221321'
]


drop_not_cidade = ['DT_GERACAO', 'HH_GERACAO', 'ANO_ELEICAO', 'CD_TIPO_ELEICAO',
       'NM_TIPO_ELEICAO', 'CD_PLEITO', 'DT_PLEITO', 'NR_TURNO', 'CD_ELEICAO',
       'DS_ELEICAO', 'SG_UF', 'CD_MUNICIPIO',
       'NR_LOCAL_VOTACAO', 'CD_CARGO_PERGUNTA',
       'NM_PARTIDO',
       'DT_BU_RECEBIDO', 'QT_APTOS', 'QT_COMPARECIMENTO', 'QT_ABSTENCOES',
       'CD_TIPO_URNA', 'DS_TIPO_URNA', 'CD_TIPO_VOTAVEL', 'DS_TIPO_VOTAVEL',
       'NR_VOTAVEL',
       'CD_CARGA_1_URNA_EFETIVADA', 'CD_CARGA_2_URNA_EFETIVADA',
       'CD_FLASHCARD_URNA_EFETIVADA', 'DT_CARGA_URNA_EFETIVADA',
       'DS_CARGO_PERGUNTA_SECAO', 'DS_AGREGADAS', 'DT_ABERTURA',
       'DT_ENCERRAMENTO', 'QT_ELEITORES_BIOMETRIA_NH', 'DT_EMISSAO_BU',
       'NR_JUNTA_APURADORA', 'NR_TURMA_APURADORA',
       'DS_CARGO_PERGUNTA', 'NR_URNA_EFETIVADA', 'QT_VOTOS', 'NR_PARTIDO', 'SG_PARTIDO', 'NM_VOTAVEL', 'NR_ZONA', 'NR_SECAO']


drop_col = ['DT_GERACAO', 'HH_GERACAO', 'ANO_ELEICAO', 'CD_TIPO_ELEICAO',
       'NM_TIPO_ELEICAO', 'CD_PLEITO', 'DT_PLEITO', 'NR_TURNO', 'CD_ELEICAO',
       'DS_ELEICAO', 'SG_UF',
       'NR_LOCAL_VOTACAO', 'CD_CARGO_PERGUNTA',
       'NM_PARTIDO',
       'DT_BU_RECEBIDO', 'QT_APTOS', 'QT_COMPARECIMENTO', 'QT_ABSTENCOES',
       'CD_TIPO_URNA', 'DS_TIPO_URNA', 'CD_TIPO_VOTAVEL', 'DS_TIPO_VOTAVEL',
       'NR_VOTAVEL',
       'CD_CARGA_1_URNA_EFETIVADA', 'CD_CARGA_2_URNA_EFETIVADA',
       'CD_FLASHCARD_URNA_EFETIVADA', 'DT_CARGA_URNA_EFETIVADA',
       'DS_CARGO_PERGUNTA_SECAO', 'DS_AGREGADAS', 'DT_ABERTURA',
       'DT_ENCERRAMENTO', 'QT_ELEITORES_BIOMETRIA_NH', 'DT_EMISSAO_BU',
       'NR_JUNTA_APURADORA', 'NR_TURMA_APURADORA']

partidos = ['PTB', 'PL', 'PT', 'PDT', 'MDB', '#NULO#', 'NOVO', 'UNIÃO', 'PSOL',
            'PP', 'PMN', 'PODE', 'PROS', 'PATRIOTA', 'REPUBLICANOS', 'PSD',  'PMB', 'DC',
            'REDE', 'PRTB', 'SOLIDARIEDADE', 'PSC', 'CIDADANIA', 'PV', 'PSB', 'PSDB', 'PC do B',
            'PCB', 'UP', 'PSTU', 'PCO', 'Nulo', 'Branco']

cores = ['#00bfff', '#120075', '#c4122d','#FE8E6D', '#00aa4f', '#3b484e','#F3701B', '#40ccff', '#FFEE57',
         '#0067A5', '#DD3333', '#31b44b','#f48c24', '#006400', '#002cc4','#FFA500', '#DD3333', '#0065cb',
         '#00C2BB', '#2cb53f', '#ff6600','#006f41', '#0080FF', '#DA251C','#ff0000', '#000000', '#c92127',
         '#9F030A', '#3b484e', '#FEFEFE', '#FEFEFE']

# ['CD_MUNICIPIO', 'NM_MUNICIPIO', 'DS_CARGO_PERGUNTA', 'NR_URNA_EFETIVADA', 'QT_VOTOS', 'NR_PARTIDO', 'SG_PARTIDO', 'NM_VOTAVEL', 'NR_ZONA', 'NR_SECAO']

root_host = "https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2022/buweb/"

capitais = ['RIO BRANCO','MACEIO','MACAPA','MANAUS','SALVADOR','FORTALEZA','VITORIA','GOIANIA','SAO LUIS','CUIABA',
'CAMPO GRANDE','BELO HORIZONTE','BELEM','JOAO PESSOA','CURITIBA','RECIFE','TERESINA','RIO DE JANEIRO','NATAL',
'PORTO ALEGRE','PORTO VELHO','BOA VISTA','FLORIANOPOLIS','SAO PAULO','ARACAJU','PALMAS']

cargos = ['Presidente', 'Governador', 'Senador', 'Deputado Federal', 'Deputado Estadual']

estados = ['AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO','ZZ']

colors = {
 '2020': 'blue',
 '2015': 'pink',
 '2013': 'darkred',
 '2011': 'orange',
 '2010': 'red',
 '2009': 'purple',
}