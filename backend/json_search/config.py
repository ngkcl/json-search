# As the makefile calls the scripts we assume poject directory is ./src relative to makefile
PROJECT_PATH = "./json_search/"
ROOT = "./"

INDEX_DIRNAME = "indexdir"
INDEX_DIR = ROOT + INDEX_DIRNAME

DATA_FILE_NAME = "stores.json"
DATA_FILE = PROJECT_PATH + DATA_FILE_NAME

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5000