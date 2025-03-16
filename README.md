# ¿Qué hay en tu plato?

Una aplicación de análisis nutricional impulsada por inteligencia artificial que te permite identificar alimentos en imágenes, calcular información nutricional y detectar el estado de los alimentos.

## Características

- **Identificación de alimentos** en imágenes con alta precisión
- **Cálculo de información nutricional** (calorías, proteínas, carbohidratos, grasas)
- **Detección del estado de los alimentos** para garantizar seguridad alimentaria
- **Recomendaciones personalizadas** para mejorar hábitos alimenticios
- **Visualización de datos** a través de gráficos interactivos
- **Exportación y guardado** de análisis para seguimiento

## Requisitos

- Python 3.9+
- Streamlit
- OpenCV
- Llama Index
- Google Gemini API
- Otras dependencias listadas en `requirements.txt`

## Configuración

1. Clona este repositorio
2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```
3. Crea un archivo `.env` basado en `.env.example` y añade tu API key de Google Gemini
4. Ejecuta la aplicación:
   ```
   streamlit run app.py
   ```

## Despliegue en Streamlit Cloud

1. Haz un fork de este repositorio a tu cuenta de GitHub
2. Ve a [Streamlit Cloud](https://streamlit.io/cloud)
3. Inicia sesión con tu cuenta de GitHub
4. Haz clic en "New app"
5. Selecciona tu repositorio, la rama (generalmente "main") y la ruta al archivo principal (app.py)
6. En la sección "Advanced settings", añade tu API key de Google como secreto:
   - Nombre: `GOOGLE_API_KEY`
   - Valor: Tu API key de Google Gemini
7. Haz clic en "Deploy"

## Solución de problemas comunes

### Error: ModuleNotFoundError

Si recibes errores de módulos no encontrados, asegúrate de que todas las dependencias estén correctamente instaladas:
```
pip install -r requirements.txt
```

### Error: API Key no válida

Verifica que has configurado correctamente la API key de Google Gemini en el archivo `.env` o como secreto en Streamlit Cloud.

### Error: Memoria insuficiente

La aplicación puede requerir bastante memoria para procesar imágenes y ejecutar modelos de IA. Si experimentas problemas de memoria en Streamlit Cloud, considera optimizar el código o usar una plataforma con más recursos.

## Licencia

Este proyecto está licenciado bajo [Licencia MIT](LICENSE).

## Autor

Desarrollado por Juan David Rivera 