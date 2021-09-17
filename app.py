import streamlit as st
import pandas as pd
import requests
import io
import matplotlib.pyplot as plt
import imageio
import PIL
import urllib
from urllib.request import urlopen
import base64
from PIL import Image
import requests
from io import BytesIO
import pickle

st.set_page_config(layout="wide")

def getImg(appid):
    index = games[games['appid'] == appid].index[0]
    res = requests.get(games['header_image'][index])
    img = Image.open(BytesIO(res.content))
    return img


def recommend(game):
    index = games[games['name'] == game].index[0]
    distances = sorted(list(enumerate(cosine_sim1[index])), reverse=True, key=lambda x: x[1])

    recommended_games_names = []
    recommended_games_posters = []

    for i in distances[1:11]:
        #print(games['name'].iloc[i[0]])            #+ '\t ' + games['header_image'].iloc[i[0]])
        app_id1 = games.iloc[i[0]].appid
        recommended_games_names.append(games['name'].iloc[i[0]])
        recommended_games_posters.append(getImg(app_id1))
    return recommended_games_names, recommended_games_posters

games_list = pickle.load(open('.pickle/gamesDataDict3.pkl','rb'))
games = pd.DataFrame(games_list)

cosine_sim1 = pickle.load(open('.pickle/cosineSim2.pkl','rb'))

#gpu_list = pickle.load(open('gpuDict.pkl','rb'))
#gpu = pd.DataFrame(gpu_list)

#cpu_list = pickle.load(open('cpuDict.pkl','rb'))
#cpu = pd.DataFrame(cpu_list)

st.title('Game Recommender')

gameOption = st.selectbox(
'Please choose a video game',
(games['name'].values))

#gpuOption = st.selectbox(
#'Please choose a GPU',
#(gpu['Architecture'].values))

#cpuOption = st.selectbox(
#'Please choose a CPU',
#(cpu['Product_Collection'].values))

if st.button('Choose Game'):
    recommended_games_names, recommended_games_posters = recommend(gameOption)
    st.header(recommended_games_names[0])
    st.image(recommended_games_posters[0])
    st.header(recommended_games_names[1])
    st.image(recommended_games_posters[1])
    st.header(recommended_games_names[2])
    st.image(recommended_games_posters[2])
    st.header(recommended_games_names[3])
    st.image(recommended_games_posters[3])
    st.header(recommended_games_names[4])
    st.image(recommended_games_posters[4])
    st.header(recommended_games_names[5])
    st.image(recommended_games_posters[5])
    st.header(recommended_games_names[6])
    st.image(recommended_games_posters[6])
    st.header(recommended_games_names[7])
    st.image(recommended_games_posters[7])
    st.header(recommended_games_names[8])
    st.image(recommended_games_posters[8])
    st.header(recommended_games_names[9])
    st.image(recommended_games_posters[9])
