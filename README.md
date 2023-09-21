## Spotify Data Getter

Very simple python program to generate datasets from spotify API

1) Vá em [Spotify For Developers](https://developer.spotify.com) e realize login

2) No [Dashboard](https://developer.spotify.com/dashboard), crie um app e siga os passos. Depois de criar o app entre em settings e copie o clientID e clientSecret

3) Entre no repositório  
$ cd spotify-data-getter

4) Instale os pacotes necessários
$ pip install -r requirements

5) Dentro do main.py, manualmente cole o client_id e o client_secret na função start() da classe

6) Executar! O resultado estará na pasta csv.