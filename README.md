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

