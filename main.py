import spotipy
import requests
import sys
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np
import random
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import json
import time
import sys
import urllib
from sklearn.preprocessing import MultiLabelBinarizer

class SpotifyDataGetter():
    def __init__(self) -> None:
        self.start()

    def start(self):
        client_id = "client_id"
        client_secret = "client_secret"
        client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        artists_dict = self.get_br_artists(self.get_artist_list())
        artist_df = pd.DataFrame.from_dict(artists_dict, orient='index')

        artist_df.to_csv('csv/artists.csv', index=False)

    def get_br_artists(self, artist_list) -> list:
        br_artists_dict = {}
        
        for artist_name in artist_list:
            results = self.sp.search(q=f"artist:{artist_name}", type='artist', limit=1)
            artists = results['artists']['items']
    
            if artists:
                artist = artists[0]
                br_artists_dict[artist_name] = {
                    #"id": artist['id'],
                    "name": artist['name'],
                    "popularity": artist['popularity'],
                    "genres": artist['genres'],
                    "followers": artist['followers']['total'],
                }

        print(br_artists_dict)

        return br_artists_dict

    def get_artist_list(self) -> list:
        return [
            # Old School
            "Carmen Miranda",
            "João Gilberto",
            "Elis Regina",
            "Caetano Veloso",
            "Gilberto Gil",
            "Gal Costa",
            "Chico Buarque",
            "Maria Bethânia",
            "Tom Jobim",
            "Vinicius de Moraes",
            "Milton Nascimento",
            "Eliseth Cardoso",
            "Nara Leão",
            "Cartola",
            "Dorival Caymmi",
            "Adoniran Barbosa",
            "Ary Barroso",
            "Francisco Alves",
            "Lupicínio Rodrigues",
            "Dona Ivone Lara",
            
            # New School
            "Anitta",
            "Luan Santana",
            "Marília Mendonça",
            "Pabllo Vittar",
            "Emicida",
            "Alok",
            "Ludmilla",
            "Wesley Safadão",
            "Gusttavo Lima",
            "Iza",
            "Vitor Kley",
            "Gloria Groove",
            "Léo Santana",
            "Thiaguinho",
            "Jão",
            "Tiago Iorc",
            "Duda Beat",
            "BaianaSystem",
            "Liniker",
            "Karol Conká",
            
            # Old School
            "Roberto Carlos",
            "Raul Seixas",
            "Cazuza",
            "Rita Lee",
            "Zé Ramalho",
            "Legião Urbana",
            "Os Mutantes",
            "Roupa Nova",
            "Paralamas do Sucesso",
            "Titãs",
            "Engenheiros do Hawaii",
            "Kid Abelha",
            "Beto Guedes",
            "Rita Lee",
            "Zé Ramalho",
            "RPM",
            "Ultraje a Rigor",
            "Capital Inicial",
            "Blitz",
            "João Bosco",
            
            # New School
            "Silva",
            "Pitty",
            "Criolo",
            "Clarice Falcão",
            "Rincon Sapiência",
            "Tropkillaz",
            "Papatinho",
            "Baco Exu do Blues",
            "Lellê",
            "Agnes Nunes",
            "Rico Dalasam",
            "Mc Tha",
            "Hot e Oreia",
            "BK'",
            "Djonga",
            "Froid",
            "Cynthia Luz",
            "Mãeana",
            "Josyara",
            "MC Carol",
        ]

if __name__ == '__main__':
    spd = SpotifyDataGetter()