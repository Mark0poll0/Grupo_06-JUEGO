
# SOKOBAN |  GRUPO 06 | LEER SECCION DE COMO EJECUTAR - TRABAJO FINAL

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.6.1-green?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Status](https://img.shields.io/badge/Status-En_Desarrollo-orange?style=for-the-badge)
## 👥 Integrantes (Grupo 06)
* Quispe Gonzales Mark
* Illesca Vicente Alexander
* Junior Yanac Minaya

---


### 📦 Tecnologías y Librerías Utilizadas
* **Python 3.11+**: Lenguaje base para el desarrollo del proyecto.
* **Pygame**: Biblioteca para el manejo del motor 2D, renderizado gráfico por celdas y captura de eventos discretos de teclado.
* **Scikit-learn**: Framework encargado del entrenamiento, evaluación y persistencia (archivos .pkl) de los modelos de Machine Learning.
* **Pandas y NumPy**: Utilizados para la estructuración del dataset de movimientos y manipulación algebraica de las matrices del tablero.

---

## 🚀 Guía de Instalación y Ejecución

Sigue estos pasos detallados de manera secuencial para clonar, configurar el entorno virtual y ejecutar el proyecto en tu máquina local.

### 1. Clonar el Repositorio
Abre tu terminal GIT BASH  o consola de comandos y ejecuta el siguiente comando para clonar el proyecto:
```bash
git clone https://github.com/Mark0poll0/Grupo_06-JUEGO.git
```



### 2. Abrir el Proyecto en Visual Studio Code

### 3. Configurar y Activar el Entorno Virtual (venv)
Para aislar las dependencias del proyecto, crea y activa el entorno virtual ejecutando estos dos comandos secuenciales en la terminal de VS Code:

1. Crear el entorno en tu terminal de visual (Se hace solo la primera vez):
```bash
python -m venv .venv
```
2. Activar el entorno en la terminal clásica de visual studio :
```bash
.venv\Scripts\activate.bat
```

Nota: Sabrás que se activó correctamente porque verás el prefijo (.venv) al inicio de la línea de comandos.



### 4. Instalar los Requerimientos del Sistema
Con el entorno virtual activado, instala todas las dependencias necesarias EJECUTA EN TU TERMINAL:
```bash
pip install -r requirements.txt
```
### 5. Ejecución del Proyecto
Para inicializar el juego e interactuar con el mapa base, ejecuta el módulo principal desde la raíz del espacio de trabajo:
```bash
python -m src.main 
```
O PRESIONA F5 -  :v 


---

## 📝 Resumen del Proyecto
Sokoban IA Híbrido es un videojuego interactivo 2D Humano-Máquina desarrollado en Python. Combina búsquedas en grafos tradicionales con modelos predictivos clásicos de scikit-learn (sin redes profundas) para anticipar los movimientos del jugador y alterar el entorno dinámicamente.