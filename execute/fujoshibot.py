import json
from requests_oauthlib import OAuth1Session
from GenerateText import GenerateText

consumer_key = 'KpAEO0WxnGyHgWsGEf1OlMTZE'
consumer_secret = 'VobwNObT810beusoqNxwI6vXIvWPxt8xEzudwGQAJnwRSJx4PO'
access_token = '941478586103488512-5MCh5qDEpJWkBBlKmnfOsratilTPcai'
access_token_secret = 'IvkcXXsR249IRYhbpWxwL0W5jWNCjyFF6Nbfht0bik66M'

def markovbot():
    #keysfile = open('keys.json')
    #keys = json.load(keysfile)
    oath = create_oath_session()

    generator = GenerateText(1)

    tweetmarkovstring(oath, generator)

def create_oath_session():
    oath = OAuth1Session(
    consumer_key, consumer_secret, access_token, access_token_secret
    #oath_key_dict['consumer_key'],
    #oath_key_dict['consumer_secret'],
    #oath_key_dict['access_token'],
    #oath_key_dict['access_token_secret']
    )
    return oath

def tweetmarkovstring(oath, generator):
    url = 'https://api.twitter.com/1.1/statuses/update.json'
    markovstring = generator.generate()
    print(markovstring)
    params = {'status': markovstring}
    req = oath.post(url, params)

    if req.status_code == 200:
        print('tweet succeed!')
    else:
        print('tweet failed')


if __name__ == '__main__':
    markovbot()