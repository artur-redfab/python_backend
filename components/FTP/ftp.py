from ftpretty import ftpretty

host = "192.168.156.70"
user = "kond"
passwd = "xtJobZ2a"

path = 'C:/Users/kond/Desktop/Programming'


def connect_FTP():
    return ftpretty(host, user, passwd)


def get_file_from_FTP(filename: str, dest_path: str):
    connect_FTP().get(f'/{filename}', f'{dest_path}/{filename}')


def set_file_to_FTP(filename: str, dep_path: str):
    connect_FTP().put(f'{dep_path}/{filename}', f'/{filename}')

