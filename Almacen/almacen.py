import argparse
import sqlite3
import yaml

parser = argparse.ArgumentParser(description='Generates tokes JWT from a path where the file payload.json is located and a secret')

parser.add_argument('--servidor', help='Ip or name of the server', type=str, default='Localhost')
parser.add_argument('--puerto', help='Api port', type=str, default='5000')
parser.add_argument('--config', help='File configuration path', nargs=1, required=True, type=str)

args = parser.parse_args()
config_file_name=args.config[0]

# open and read the config file
with open(config_file_name) as config_file:
        config_data=config_file.read()
        config_file.close()

config_dict = yaml.safe_load(config_data)

con = sqlite3.connect(config_dict['basedatos']['path'])
cur = con.cursor()

res = cur.execute("SELECT name FROM sqlite_master WHERE name='article'")
if (res.fetchone() is None):
    cur.execute("CREATE TABLE article(article_id, description, stock_units, available)")
else:
    print ("Exists")