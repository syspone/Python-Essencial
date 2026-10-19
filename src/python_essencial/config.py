"""Configurações do projeto, lidas do arquivo .env com python-dotenv."""

import os
from pathlib import Path

from dotenv import load_dotenv

# Raiz do projeto (a pasta que contém o pyproject.toml)
DIR_RAIZ = Path(__file__).resolve().parents[2]

load_dotenv(DIR_RAIZ / ".env")

DIR_AULAS = DIR_RAIZ / "aulas"
DIR_DADOS = DIR_RAIZ / "data"

AMBIENTE = os.getenv("AMBIENTE", "desenvolvimento")
NIVEL_LOG = os.getenv("NIVEL_LOG", "INFO")
