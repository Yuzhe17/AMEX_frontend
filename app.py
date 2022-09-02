from asyncore import read
import streamlit as st
from PIL import Image
from pandas import read_csv
import requests
import json

st.markdown("<h1 style='text-align: center; color: purple;'>Will your customer pay you BACK?!</h1>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; color: grey;'>Dear American Express managment, </h4>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: grey;'>Please only upload a CSV file in the following format: </h5>", unsafe_allow_html=True)


col1, col2, col3, col4, col5 = st.columns(5)

with col3:

    with open('template_csv/AMEX_user_template.csv') as f:
        if st.download_button('Example template', f, 'example_template.csv'):
            st.write('Thanks for downloading!')

st.write('\n\n-------------')

amex_foto = Image.open('team_imgs/amex.png')
st.image(amex_foto)

with st.form("my_form"):

    uploaded_csv_file = st.file_uploader("Upload a customer CSV File",
                                         type=['csv'],
                                        # accept_multiple_files=True
                                         )

    submitted = st.form_submit_button("Get prediction!")


if submitted:

    url_api = 'https://amex-api-results.herokuapp.com/predict'
    if uploaded_csv_file == None:
        st.markdown("<h5 style='text-align: center; color: red;'>Wrong submission, please upload CSV file in the right format</h5>", unsafe_allow_html=True)

    else:

        data = read_csv(uploaded_csv_file, index_col=0).fillna('').to_dict(orient='records')[0]
        params_user = {"data": json.dumps(data)}

        predictions = requests.get(url_api,
                                    params = params_user).json()


        st.markdown("<h3 style='text-align: center; color: black;'>Thank you for submitting</h3>", unsafe_allow_html=True)
        st.write('-------------')
        st.markdown("<h5 style='text-align: center; color: black;'>Customer with ID:</h5>", unsafe_allow_html=True)

        if predictions['output'] == 'defaulter':

            html_str_custID = f"<h6 style='text-align: center; color: grey;'>{predictions['customer_ID']}</h6>"
            st.markdown(html_str_custID, unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: center; color: black;'>Must be a ... </h5>", unsafe_allow_html=True)
            html_str_output = f"<h3 style='text-align: center; color: red;'>{predictions['output']}</h3>"
            st.markdown(html_str_output, unsafe_allow_html=True)
            st.markdown("<h6 style='text-align: center; color: black;'>With probability of:</h6>", unsafe_allow_html=True)
            html_str_proba = f"<h3 style='text-align: center; color: red;'>{predictions['probability']}</h3>"
            st.markdown(html_str_proba, unsafe_allow_html=True)


        else:
            html_str_custID = f"<h6 style='text-align: center; color: grey;'>{predictions['customer_ID']}</h6>"
            st.markdown(html_str_custID, unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: center; color: black;'>Must be a ... </h5>", unsafe_allow_html=True)
            html_str_output = f"<h5 style='text-align: center; color: green;'>{predictions['output']}</h5>"
            st.markdown(html_str_output, unsafe_allow_html=True)
            st.markdown("<h6 style='text-align: center; color: black;'>With probability of:</h6>", unsafe_allow_html=True)
            html_str_proba = f"<h3 style='text-align: center; color: green;'>{float(predictions['probability'])*100} %</h3>"
            st.markdown(html_str_proba, unsafe_allow_html=True)

        # p_2 = read_csv(uploaded_csv_file, index_col=0).fillna('').to_dict(orient='records')[0]['P_2']

        # if p_2 == 0.3671699213:
        #     st.markdown("<h6 style='text-align: center; color: grey;'>e5a854a3211e83db521500e8b70360fe9670af1df904017d84cf245c2ec1c68b</h6>", unsafe_allow_html=True)
        #     st.markdown("<h5 style='text-align: center; color: black;'>Must be a ... </h5>", unsafe_allow_html=True)
        #     st.markdown("<h5 style='text-align: center; color: green;'>payer</h5>", unsafe_allow_html=True)
        #     st.markdown("<h6 style='text-align: center; color: black;'>With probability of:</h6>", unsafe_allow_html=True)
        #     st.markdown("<h3 style='text-align: center; color: green;'>94.7 %</h3>", unsafe_allow_html=True)

        # elif p_2 == 0.5243904932:
        #     st.markdown("<h6 style='text-align: center; color: grey;'>6ba461c93869797c49b0f34c29274e50915466eda02a82fde4aa2c73c3924339</h6>", unsafe_allow_html=True)
        #     st.markdown("<h5 style='text-align: center; color: black;'>Must be a ... </h5>", unsafe_allow_html=True)
        #     st.markdown("<h5 style='text-align: center; color: red;'>defaulter</h5>", unsafe_allow_html=True)
        #     st.markdown("<h6 style='text-align: center; color: black;'>With probability of:</h6>", unsafe_allow_html=True)
        #     st.markdown("<h3 style='text-align: center; color: red;'>84.3 %</h3>", unsafe_allow_html=True)

        # else:
        #     st.markdown("<h5 style='text-align: center; color: red;'>Wrong submission, please upload CSV file in the right format</h5>", unsafe_allow_html=True)


st.write('-------------')

isis_img = Image.open('team_imgs/isis.jpeg')
slawa_img = Image.open('team_imgs/slawa.jpeg')
yuzhe_img = Image.open('team_imgs/yuzhe.jpeg')
sjoerd_img = Image.open('team_imgs/sjoerd.jpeg')
lewagon_img = Image.open('team_imgs/lewagon.png')

st.write('\n\n\n\nThis wonderful predictor is brought to you by:')


st.image([isis_img, slawa_img, yuzhe_img, sjoerd_img, lewagon_img],
         caption=['Isis!', 'Slawa!', 'Yuzhe!', 'Sjoerd!', 'Le Wagon!'], width=100)

st.write('-------------')

mlfoto = Image.open('team_imgs/MLfoto.webp')
st.image(mlfoto)
