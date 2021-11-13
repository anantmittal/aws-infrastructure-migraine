import ruamel.yaml


# Path is relative to server_flask
COUCHDB_CLIENT_CONFIG_PATH = "../secrets/client/couchdb_client_config.yaml"


class Config:

    def __init__(self):
        with open(COUCHDB_CLIENT_CONFIG_PATH) as file_couchdb_client_config:
            couchdb_client_config = ruamel.yaml.safe_load(file_couchdb_client_config)

        self.DB_BASEURL = couchdb_client_config["baseurl"]
        self.DB_ADMIN_USER = couchdb_client_config["admin"]["user"]
        self.DB_ADMIN_PASSWORD = couchdb_client_config["admin"]["password"]
