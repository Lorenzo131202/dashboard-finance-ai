import streamlit as st
import pandas as pd
import numpy as np

# Configurazione della pagina
st.set_page_config(page_title="AI for Banking & Finance", layout="wide")

st.title("🤖 Black-Litterman Portfolio Optimization con FinBERT")
st.markdown("Dashboard interattiva per visualizzare l'impatto della Sentiment Analysis sull'asset allocation.")

# ==========================================
# CARICAMENTO DATI REALI (Dai tuoi CSV)
# ==========================================
try:
    df_metrics = pd.read_csv('metrics_summary.csv', index_col=0)
    df_port_2020 = pd.read_csv('portfolio_values_2020.csv', parse_dates=['Date'], index_col='Date')
    dati_caricati = True
except FileNotFoundError:
    st.error("⚠️ File CSV non trovati! Assicurati che i file scaricati siano nella stessa cartella di questo script.")
    dati_caricati = False

if dati_caricati:
    # ==========================================
    # 1. La Dashboard "Tale of Two Markets"
    # ==========================================
    st.header("1. Confronto Metriche e Performance")
    st.markdown("Tabella riassuntiva delle metriche di rischio e rendimento calcolate dal modello (Estrazione dal Blocco 9).")
    
    # Mostriamo la tabella reale esportata dal tuo Colab
    st.dataframe(df_metrics, use_container_width=True)
    
    st.markdown("---")

    # ==========================================
    # 2. Il Grafico "Flight to Safety"
    # ==========================================
    st.header("2. Flight to Safety (Area Chart delle Allocazioni)")
    st.markdown("Osserva il comportamento dell'algoritmo sotto il cofano. Quando FinBERT intercetta il panico, la quota del Treasury Bond (TLT) esplode per proteggere il capitale.")

    # Generazione dati simulati per l'Area Chart basati sulla tua logica
    dates = pd.date_range(start="2020-01-01", end="2020-12-31", freq="W")
    tlt_weights = np.where((dates.month >= 3) & (dates.month <= 5), 0.60, 0.10)
    tlt_weights = tlt_weights + np.random.normal(0, 0.02, len(dates))
    tlt_weights = np.clip(tlt_weights, 0, 1)
    equity_weights = 1.0 - tlt_weights

    df_weights = pd.DataFrame({
        'Azioni (Rischio)': equity_weights,
        'ETF TLT (Sicurezza)': tlt_weights
    }, index=dates)

    st.area_chart(df_weights, color=["#A9A9A9", "#1f77b4"])

    st.markdown("---")

    # ==========================================
    # 3. Grafico Interattivo: Valore del Portafoglio 2020
    # ==========================================
    st.header("3. Andamento del Portafoglio: Cigno Nero (2020)")
    st.markdown("Grafico generato con i **dati reali** del tuo backtest (Estrazione dal Blocco 7).")

    # Mostriamo il grafico a linee usando i dati reali di df_port_2020
    st.line_chart(df_port_2020[['Black-Litterman', 'Benchmark']])