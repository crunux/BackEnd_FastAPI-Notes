import os

#Database
ENGINE_DATABASE = os.getenv("ENGINE_DATABASE")
USER_DATABASE = os.getenv("USER_DATABASE")
PASSWORD_DATABASE = os.getenv("PASSWORD_DATABASE")
HOST_DATABASE = os.getenv("HOST_DATABASE")
PORT_DATABASE = os.getenv("PORT_DATABASE")
NAME_DATABASE = os.getenv("NAME_DATABASE")

#Security
SECRET_KEY = "dc6e082640dbde65b3db9e082c69c1939118df36b4aac1cbdd5f76980ab66ef0"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30