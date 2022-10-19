fastApi backend to query data from twitter and google trends

It needs an .env file on this folder with twitter settings
https://python-twitter.readthedocs.io/en/latest/getting_started.html



### running locally ###
git clone https://github.com/dgranuzzo/twitter-google-trends-bk
cd twitter-google-trends-bk
pip install -r requirements.txt
cd app
python main.py


### running with Docker ###
git clone https://github.com/dgranuzzo/twitter-google-trends-bk
cd twitter-google-trends-bk
docker build -t trends .
docker run trends

