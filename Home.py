import streamlit as st

st.set_page_config(
    page_title="Eleições - Brasil 2022",
    page_icon="👋",
)

st.write("# Eleições - Brasil 2022 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Um relatório sem autoria que circula pela internet aponta que existe uma diferença significatica de votos para determinado candidato nos modelos de urna anteriores a 2020.
    O objetivo do trabalho é averiguar se essa diferença existe ou não e apresentar essa comparação de forma conveniente para que a informação fique clara.
    
    - Site do TSE com os dados: https://dadosabertos.tse.jus.br/dataset/resultados-2022-boletim-de-urna
    - Modelo de Urna: https://cdn.tse.jus.br/estatistica/sead/odsele/modelo_urna/modelourna_numerointerno.zip
    - Relatório de inconsistências: https://ia904707.us.archive.org/13/items/brazil-was-stolen/BrazilWasStolen.pdf
    - Vídeo de apresentação do relatório: https://odysee.com/@desmentindoestado:7/-BrazilWasStolen:7
    """
)