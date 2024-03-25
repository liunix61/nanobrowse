from nanorpc.client import NanoRpcTyped, NodeVersion
from nanorpc.client_nanoto import NanoToRpcTyped
from os import getenv

RPC_URL = getenv("RPC_URL")
AUTH_USERNAME = getenv("AUTH_USERNAME")
AUTH_PASSWORD = getenv("AUTH_PASSWORD")
NANO_TO_AUTH_KEY = getenv("NANO_TO_AUTH_KEY")  # optinal


def get_nanorpc_client(rpc_url=None, auth_username=None, auth_password=None):
    # Set the environment variables if they don't exist and parameters are provided
    rpc_url = rpc_url or RPC_URL
    auth_username = auth_username or AUTH_USERNAME
    auth_password = auth_password or AUTH_PASSWORD

    # Initialize and return the NanoRpc client
    return NanoRpcTyped(url=rpc_url,
                        username=auth_username,
                        password=auth_password,
                        wrap_json=True)


def get_nanoto_client():
    return NanoToRpcTyped(NANO_TO_AUTH_KEY, app_name="nanobrowse.com", app_email="iq.cc@pm.me")


# Create a single instance of NanoRpc client
nanorpc: NanoRpcTyped = get_nanorpc_client()
nanoto: NanoToRpcTyped = get_nanoto_client()
