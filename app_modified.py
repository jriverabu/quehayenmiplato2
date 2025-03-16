import streamlit as st
import cv2
import numpy as np
import tempfile
from llama_index.llms.gemini import Gemini
from llama_index.core.llms import ChatMessage, ImageBlock, MessageRole, TextBlock
import re
import os
import base64
from PIL import Image
import io
import pandas as pd
import json
from datetime import datetime
import uuid
import altair as alt
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Set up Google API Key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("No se encontró la API key de Google. Por favor, configura la variable de entorno GOOGLE_API_KEY.")
    st.stop()

os.environ["GOOGLE_API_KEY"] = api_key

# Initialize the Gemini model
gemini_pro = Gemini(model_name="models/gemini-1.5-flash")

# Custom CSS
def local_css(file_name):
    try:
        with open(file_name, "r") as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"Archivo CSS no encontrado: {file_name}")

def set_page_config():
    st.set_page_config(
        page_title="¿Qué hay en tu plato?",
        page_icon="🥩",
        layout="wide",
        initial_sidebar_state="expanded",
    )

def main():
    set_page_config()
    
    # Intentar cargar CSS si existe
    try:
        local_css("style.css")
    except Exception as e:
        st.warning(f"No se pudo cargar el archivo CSS: {str(e)}")

    # Intentar cargar logo si existe
    logo_path = "logo.png"
    if os.path.exists(logo_path):
        st.sidebar.image(logo_path, use_container_width=True)
    else:
        st.sidebar.title("¿Qué hay en tu plato?")
        
    st.sidebar.markdown("Powered by Juan David Rivera")

    menu = ["Herramienta", "Sobre el Proyecto", "Investigaciones"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if choice == "Herramienta":
        home_page()
    elif choice == "Sobre el Proyecto":
        about_page()
    elif choice == "Investigaciones":
        contact_page()

# El resto del código permanece igual...
# Aquí deberías copiar el resto de las funciones de tu app.py original

# Ejemplo de las funciones principales (deberías completar con tu código original)
def home_page():
    st.title("¿Qué hay en tu plato?")
    st.markdown("Upload an image or use your camera to detect objects in real-time!")
    
    # Aquí va el resto de tu código de home_page()...

def about_page():
    st.title("Sobre ¿Qué hay en tu plato?")
    # Aquí va el resto de tu código de about_page()...

def contact_page():
    st.title("Investigaciones y Recursos")
    # Aquí va el resto de tu código de contact_page()...

if __name__ == "__main__":
    main() 