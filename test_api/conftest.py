import requests
import pytest
import os
from dotenv import load_dotenv


@pytest.fixture(autouse=True, scope='session')
def load_env(autouse=True):
    load_dotenv()


@pytest.fixture(autouse=True)
def session():
    print(f'create session')
    session = requests.session()
    yield session



