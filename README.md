# Python-Essencial

Aulas e exercícios do curso de Python, organizados no padrão de um projeto profissional.

## Estrutura

```
Python-Essencial/
├── aulas/                    # uma aula por arquivo (aula01_..., aula02_...)
├── src/python_essencial/     # código do projeto
│   ├── config.py             # lê as configurações do .env
│   └── main.py               # menu para listar e rodar as aulas
├── tests/                    # testes automatizados (pytest)
├── data/                     # dados locais (fora do git)
├── notebooks/                # notebooks Jupyter
├── .env.example              # modelo das variáveis de ambiente
├── requirements.txt          # dependências do projeto
├── requirements-dev.txt      # dependências de desenvolvimento
└── pyproject.toml            # metadados e configuração do pytest e do ruff
```

## Instalação

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pip install -e .
cp .env.example .env
```

## Como usar

Rodar uma aula direto:

```bash
python aulas/aula04_variaveis.py
```

Ou pelo menu, que lista todas as aulas:

```bash
python -m python_essencial
```

## Qualidade do código

```bash
pytest          # roda os testes
ruff check .    # verifica o estilo do código
ruff format .   # formata o código
```

## Aulas

| Nº | Arquivo | Assunto |
|----|---------|---------|
| 01 | `aula01_comentarios.py` | Comentários e docstrings |
| 02 | `aula02_docstring_funcoes.py` | Docstrings em funções |
| 03 | `aula03_operadores_matematicos.py` | Operadores matemáticos |
| 04 | `aula04_variaveis.py` | Variáveis e tipos |

## Nova aula

Crie o arquivo seguindo a numeração (ex.: `aulas/aula05_listas.py`) com o mesmo cabeçalho
das outras aulas. Ele aparece sozinho no menu e nos testes.
