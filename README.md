# Telelgram bot(pet project✨)
## Bot for exchange rates

## Features

- The bot takes in currency code that you want to sell and buy.
- The bot takes in amount of currency that you want to sell. 
- As a resutl the bot returns you amount of currency that you want to buy, according current rates. 


## Installation


#### Install and run localy:

```sh
git clone
# clone this repo

cd <PATH>
# move to project root directory

pip3 install -r requirements.txt 
# install requirements

export TOKEN=<your bot token> 
# to start the bot, you need to pass token to the environment

python3 run main.py

```

#### Install and run with Docker:

```sh
git clone
# clone this repo

cd <PATH>
# move to project root directory

docker build -t <REPOSITORY>:<TAG> . 
# build docker image for this bot pass REPOSITORY and TAG for comfortable run

docker run -e TOKEN_BOT_EXCHANGE=<your bot token> <REPOSITORY>:<TAG>
# create and run your docker Container with bot passing your bot token to environment 
```

 





  

