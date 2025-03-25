# stj_process_client/__init__.py
from .consultar import STJClient
from .extrair import create_dataframes

__all__ = ['STJClient', 'create_dataframes']
