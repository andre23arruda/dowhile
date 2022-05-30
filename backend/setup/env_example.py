# RENAME THIS FILE TO env.py
import os, json, socket


def get_ip_address():
    '''Return IP adress'''
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def get_allowed_hosts():
    '''Create a list of aloowed hosts'''
    hosts = ['127.0.0.1', 'localhost', get_ip_address()]
    return hosts


os.environ['SECRET_KEY'] = 'your key'
os.environ['DEBUG'] = 'true'
os.environ['ALLOWED_HOSTS'] = json.dumps(get_allowed_hosts())
os.environ['LANGUAGE_CODE'] = 'pt-br'
os.environ['TIME_ZONE'] = 'America/Sao_Paulo'

os.environ['CLOUDINARY'] = '' # '' is False
os.environ['CLOUD_NAME'] = 'utils-cloudinary'
os.environ['API_KEY'] = 'your-key'
os.environ['API_SECRET'] = 'your-api-key'

os.environ['CORS_ALLOWED_ORIGINS'] = json.dumps([ f'http://{ host }:3000' for host in get_allowed_hosts() ])

os.environ['GITHUB_CLIENT_ID'] = 'CLIENT_ID'
os.environ['GITHUB_CLIENT_SECRET'] = 'CLIENT_SECRET'
