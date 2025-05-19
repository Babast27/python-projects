import streamlit as st
from config import STREAMLIT_LAYOUT, PROJECTS

# importe tes classes
from modules.crypto   import CryptoAnalyzer
from modules.garch    import GarchModel
from modules.spot     import SpotPlotter
from modules.future   import FuturePlotter
from modules.portfolio import PortfolioTracker

st.set_page_config(layout=STREAMLIT_LAYOUT, page_title="Mes Projets Python")
st.sidebar.title("Mes projets Python")

# liste dynamique des choix
choice = st.sidebar.radio("Choisis un projet :", list(PROJECTS.keys()))

factory = {
    "Analyse crypto": CryptoAnalyzer,
    "GARCH":          GarchModel,
    "Spot Data":      SpotPlotter,
    "Future Data":    FuturePlotter,
    "Portefeuille":   PortfolioTracker
}

proj_class = factory.get(choice)
if proj_class:
    proj = proj_class()
    proj.run()
else:
    st.error(f"Projet « {choice} » non trouvé.")
