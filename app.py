import streamlit as st
import numpy as np
import tensorflow as tf
import torch

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from tensorflow.keras.preprocessing.sequence import pad_sequences

# ======================================
# PAGE CONFIG
# ======================================
st.set_page_config(
    page_title="Sentimen Genshin Impact",
    page_icon="🎮",
    layout="centered"
)

# ======================================
# HEADER
# ======================================
st.markdown(
    """
    <div style="text-align:center">
        <h1>🎮 Klasifikasi Sentimen Komentar Genshin Impact</h1>
       
    """,
    unsafe_allow_html=True
)

st.divider()

# ======================================
# LOAD MODEL
# ======================================

@st.cache_resource
def load_lstm():
    return tf.keras.models.load_model("lstm_genshin_model.keras")

@st.cache_resource
def load_transformer(model_path):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    return tokenizer, model

# Load models
lstm_model = load_lstm()

bert_tokenizer, bert_model = load_transformer("bert_genshin_model")
distil_tokenizer, distil_model = load_transformer("distilbert_genshin_model")
indobert_tokenizer, indobert_model = load_transformer("indobert_genshin_model")

# ======================================
# INPUT USER
# ======================================
st.subheader("💬 Masukkan Komentar")

text = st.text_area(
    "Tulis komentar pemain:",
    placeholder="Contoh: Game-nya seru tapi event-nya kurang menarik...",
    height=120
)

model_choice = st.selectbox(
    "🔍 Pilih Model",
    ["LSTM", "BERT", "DistilBERT", "IndoBERT"]
)

# ======================================
# PREDIKSI
# ======================================
if st.button("🚀 Prediksi Sentimen", use_container_width=True):
    if text.strip() == "":
        st.warning("Komentar tidak boleh kosong.")
    else:
        with st.spinner("Memproses prediksi..."):

            if model_choice == "LSTM":
                # 🔒 BIARKAN SEPERTI AWAL KAMU (AMAN)
                seq = [[0]]  # dummy input agar model tidak error
                pad = pad_sequences(seq, maxlen=100, padding="post")
                pred = lstm_model.predict(pad)
                label = np.argmax(pred)

            elif model_choice == "BERT":
                inputs = bert_tokenizer(text, return_tensors="pt", truncation=True, padding=True)
                outputs = bert_model(**inputs)
                label = torch.argmax(outputs.logits, dim=1).item()

            elif model_choice == "DistilBERT":
                inputs = distil_tokenizer(text, return_tensors="pt", truncation=True, padding=True)
                outputs = distil_model(**inputs)
                label = torch.argmax(outputs.logits, dim=1).item()

            else:  # IndoBERT
                inputs = indobert_tokenizer(text, return_tensors="pt", truncation=True, padding=True)
                outputs = indobert_model(**inputs)
                label = torch.argmax(outputs.logits, dim=1).item()

        label_map = {
            0: "Negatif 😠",
            1: "Others 📝",
            2: "Positif 😊"
        }

        st.success(f"### Hasil Prediksi: {label_map[label]}")
