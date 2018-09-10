from client.conf import settings
from . import client_01



def run():
    if settings.MODE == "Agent":
        cli = client_01.Agent()
    elif settings.MODE == "SSH":

        cli = client_01.SSH()
        print("ssh")
    elif settings.MODE == "Salt":
        cli = client_01.Salt()
    else:
        raise Exception("")

    cli.process()