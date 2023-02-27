from ftpretty import ftpretty
from decouple import config

host = config('FTP_HOST')
user = config('FTP_USER')
passwd = config('FTP_PWD')


def connect_FTP():
    return ftpretty(host, user, passwd)


def get_file_from_FTP(filename: str, dest_path: str):
    connect_FTP().get(f'/{filename}', f'{dest_path}/{filename}')


def send_file_to_FTP(filename: str, dep_path: str):
    connect_FTP().put(f'{dep_path}/{filename}', f'/{filename}')

