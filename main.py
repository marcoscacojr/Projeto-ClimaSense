import streamlit as st
import folium
from streamlit_folium import st_folium, folium_static

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
st.button("Atualizar Notícias")

# Seção de notícias
st.subheader("Notícias Recentes")

# Notícias relacionadas aos eventos
st.markdown("""
- **Queimadas no interior de São Paulo**: Aumentam o número de focos de incêndio no interior de SP, principalmente em Ribeirão Preto.
- **Queda Brusca da Temparatura no Centro-Oeste**: Correntes de alta pressão vão resfriar a semana no Centro-Oeste.
- **Enchentes na capital paulista**: Com as fortes chuvas ao longo do dia, as principais vias da cidade de São Paulo estão completamente alagadas.
""")

# Simulação de alertas
st.subheader("Alertas Atuais")
st.info("Alerta: Enchente eminente na sua região!")
st.warning("Alerta: Qualidade do ar muito baixa!")
st.error("Alerta: Foco de incêndio iniciado na sua região!")
