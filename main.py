import streamlit as st
import auxiliar as aux

st.set_page_config(
    page_title="Flower Clasification"
)

if 'images' not in st.session_state:
    st.session_state['images'] = list()
    st.session_state['model'] = None


if not st.session_state['images']:
    st.session_state['model'] = aux.load_model()

    uploades_files = st.file_uploader("Sube una Imagen",  type = ['png', 'jpg', 'jpeg'], accept_multiple_files=True)
    if st.button("Analizar Imagenes"):
        placeholder = st.empty()
        with placeholder.container():
            st.write("Convirtiendo las Imágenes")
            my_bar = st.progress(0)
            for i, uploaded_file in enumerate(uploades_files):
                # To read file as bytes:
                bytes_data = uploaded_file.getvalue()
                name = uploaded_file.name
                st.session_state['images'].append(aux.decode_image(bytes_data, name))
                percent_complete = (i+1)/len(uploades_files)
                my_bar.progress(percent_complete)
        
        placeholder.empty()
        st.experimental_rerun()
else:
    if st.button("Reiniciar"):
        st.session_state['images'] = list()
        st.experimental_rerun()
    for path in st.session_state['images']:
        image, y_pred = aux.predict(path)
        st.image(image)
        st.dataframe(y_pred)
        st.bar_chart(y_pred.transpose())
