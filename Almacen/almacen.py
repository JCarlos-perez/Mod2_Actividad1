'''
La aplicación recibirá como argumentos opcionales:
a.--servidor: IP o nombre del servidor donde se inicia la aplicación.Opcional. Por defecto localhost.
b.--puerto: puerto donde se expondrá el API. Opcional. Por defecto 5000.
c.--config: ruta y nombre del fichero de configuración de la aplicación.Obligatorio.
'''
import argparse
import sqlite3
import yaml
import os

def check_port(p_port):
    '''
    Check if p_port is an actually valid port

    parav value: port to be checked
    '''
    i_port = int(p_port)
    if not(1 <= i_port <= 65535):
        raise argparse.ArgumentTypeError(p_port + " no es un puerto válido [1-65535]")
    return p_port

def check_file(p_file):
    '''
    Chequea if the file is an actually valid file and it exists in the OS

    :param value: name of the file to be checked
    '''
    if not os.path.isfile(p_file):
        raise argparse.ArgumentTypeError("El fichero " + p_file + " no existe.")
    return p_file

def return_config (p_config_file_name):
    '''
    Returns a dictionary with the info of a file given than the format is YAML

    :param value: name of the file to be read
    '''
    with open(p_config_file_name) as config_file:
        configdict = yaml.safe_load(config_file)
        config_file.close()
    return configdict

def connect_db (p_database_file):
    '''
    Returns a valid cursor to the database located in the given file

    :param value: name of the database file
    '''
    con = sqlite3.connect(p_database_file)
    cur = con.cursor()

    res = cur.execute("SELECT name FROM sqlite_master WHERE name='article'")
    if (res.fetchone() is None):
        cur.execute("CREATE TABLE article(article_id, description, stock_units, available)")

    return cur

parser = argparse.ArgumentParser(description='Generates tokes JWT from a path where the file payload.json is located and a secret')

parser.add_argument('--servidor', help='Ip or name of the server', type=str, default='Localhost')
parser.add_argument('--puerto', help='Api port', type=check_port, default='5000')
parser.add_argument('--config', help='File configuration path', nargs=1, required=True, type=check_file)

args = parser.parse_args()
config_file_name = args.config[0]
servidor = args.servidor
puerto = args.puerto

# open and read the config file
config_dict = return_config(config_file_name)

#Connect to a database
cursor = connect_db (config_dict["basedatos"]["path"])