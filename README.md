# Flower Classification

Para una muestra de la funcionalidad, pueden entrar [acá](http://34.134.234.159:9030).

Para desplegar este archivo localmente, son necesarias las siguientes librerías:
* streamlit==1.14.0
* tensorflow==2.10.0
* opencv-python==4.6.0.66

Si quiere ejecutar su archivo localmente, lo puede hacer a través del siguiente comando:

```
streamlit run main.py
```

Para desplegar el contenedor, lo puede ejectutar con los siguientes comandos:

```
docker build -t medical .
docker run -it 9030:9030 --name med_app medical
```
