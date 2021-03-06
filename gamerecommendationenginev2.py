# -*- coding: utf-8 -*-
"""GameRecommendationEngineV2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZiuEaaB3gL1M-o3ThN00nc0t5ZGP3t-N
"""

import numpy as np
import pandas as pd
import ast
import pickle

games = pd.read_csv('steam.csv')
#games = games.astype(np.float32)

games.head(3)

games.shape

games[['appid', 'name', 'developer', 'publisher', 'steamspy_tags']]

features = ['appid', 'name', 'developer', 'publisher', 'steamspy_tags']

def clean_data(x):
  if isinstance(x, list):
    return [str.lower(i.replace(" ", " ")) for i in x]
  else:
      if isinstance(x, str):
        return str.lower(x.replace(" ", " "))
      else:
        return ''

for feature in features:
  games[feature] = games[feature].apply(clean_data)

def get_important_features(data):
  important_features = []
  for i in range(0, data.shape[0]):
    important_features.append(data['name'][i]+' '+data['developer'][i]+' '+data['publisher'][i]+' '+' '+data['steamspy_tags'][i])

  return important_features

games['important_features'] = get_important_features(games)

games.head(3)

games.drop(columns=['developer', 'publisher', 'steamspy_tags'])

from sklearn.feature_extraction.text import CountVectorizer

count = CountVectorizer(stop_words='english')
count_matrix1 = count.fit_transform(games['important_features'])

from sklearn.metrics.pairwise import cosine_similarity
cosine_sim1 = cosine_similarity(count_matrix1)

games[games['name'] == 'counter-strike'].index[0]

#games = games.reset_index()
#indices = pd.Series(games.index, index=games['name']).drop_duplicates()

games.head(3)

def recommend(game):    #cosine_sim=cosine_sim1
  #indx = indices[game]
  #simScore = list(enumerate(cosine_sim1[indx]))
  #simScore = sorted(simScore, key=lambda x: x[1], reverse=True)
  #simScore = simScore[1:11]
  #game_indx = [i[0] for i in simScore]
  #return games['name'].iloc[game_indx]
  index = games[games['name'] == game].index[0]
  distances = sorted(list(enumerate(cosine_sim1[index])), reverse=True, key=lambda x: x[1])
  for i in distances[1:11]:
    print(games['name'].iloc[i[0]])
    print(games['developer'].iloc[i[0]])

recommend('grand theft auto iv')       #, cosine_sim1)

pickle.dump(games,open('gamesData2.pkl', 'wb'))

pickle.dump(cosine_sim1,open('cosineSim.pkl', 'wb'), protocol=4)

pickle.dump(games.to_dict(),open('gamesDataDict2.pkl', 'wb'))