import streamlit as st
import folium
from streamlit_folium import st_folium, folium_static
import random

def exibir_noticias():
    # Função para exibir notícias aleatórias

    noticias = [
        "Queimadas no interior de São Paulo: Aumentam o número de focos de incêndio no interior de SP, principalmente em Ribeirão Preto.",
        "Queda Brusca da Temperatura no Centro-Oeste: Correntes de alta pressão vão resfriar a semana no Centro-Oeste.",
        "Enchentes na capital paulista: Com as fortes chuvas ao longo do dia, as principais vias da cidade de São Paulo estão completamente alagadas.",
        "Tempestade de areia no Nordeste: Ventos fortes estão formando grandes tempestades de areia na região nordeste do Brasil.",
        "Seca prolongada no Sul: A falta de chuvas agrava a seca em várias cidades do Sul, afetando a agricultura local.",
        "Deslizamentos de terra no Rio de Janeiro: Fortes chuvas causaram deslizamentos de terra em áreas de encosta, deixando dezenas de desabrigados.",
        "Nevasca atinge o Sul do Brasil: Regiões serranas do Rio Grande do Sul estão enfrentando uma nevasca incomum para a época do ano",
        "Tornado em área rural do Paraná: Um tornado foi registrado em áreas rurais do Paraná, causando destruição em fazendas",
        "Ondas de calor no Norte: O aumento das temperaturas está elevando os índices de calor em várias cidades da região Norte.",
        "Tsunami em área costeira do Espírito Santo: Ondas gigantes atingiram a costa do Espírito Santo, causando destruição em algumas áreas.",
        "Inundações no Pantanal: O excesso de chuvas na região do Pantanal está causando grandes inundações, afetando a fauna e flora locais.",
        "Ciclone no litoral catarinense: Um ciclone extratropical está provocando fortes ventos e ressacas no litoral de Santa Catarina."
    ]

    noticias_aleatorias = random.sample(noticias, 3)  # Seleciona 3 notícias aleatórias
    st.subheader("Notícias Atualizadas")
    for noticia in noticias_aleatorias:
        st.markdown(f"- {noticia}")
    
# Título da página
st.title("ClimaSense - Monitoramento Climático")

# Mapa com eventos climáticos
st.subheader("Mapa de Eventos Climáticos")

# Inicia o mapa
mapa = folium.Map(location=[-15.7801, -47.9292], zoom_start=4)

# Adiciona marcadores para eventos (exemplo de ícones para eventos climáticos)
folium.Marker(
    [-21.1694, -47.8111],
    popup="Incêndio Florestal",
    icon=folium.Icon(color="red", icon="fire"),
).add_to(mapa)

folium.Marker(
    [-23.5505, -46.6333], popup="Enchente", icon=folium.Icon(color="blue", icon="tint")
).add_to(mapa)

folium.Marker(
    [-15.7975, -47.8919],
    popup="Queda Brusca da Temperatura",
    icon=folium.Icon(color="lightblue", icon="temperature-arrow-down", prefix="fa"),
).add_to(mapa)

folium.Marker(
    [-22.8935, -42.4683],
    popup="Variação Brusca da Maré Alta",
    icon=folium.Icon(color="darkblue", icon="house-flood-water", prefix="fa"),
).add_to(mapa)

# Exibe o mapa no Streamlit
st_data = folium_static(mapa, width=700, height=400)

# Botão de Tempo Real
if st.button("Atualizar Notícias"):
    exibir_noticias()


# Simulação de alertas
st.subheader("Alertas Atuais")
st.info("Alerta: Enchente eminente na sua região!")
st.warning("Alerta: Qualidade do ar muito baixa!")
st.error("Alerta: Foco de incêndio iniciado na sua região!")
