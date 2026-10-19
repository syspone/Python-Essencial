"""Garante que todas as aulas rodam do começo ao fim sem erro."""

import runpy

import pytest

from python_essencial.config import DIR_AULAS
from python_essencial.main import executar_aula, listar_aulas

AULAS = listar_aulas()


def test_existem_aulas():
    assert AULAS, f"Nenhuma aula encontrada em {DIR_AULAS}"


@pytest.mark.parametrize("aula", AULAS, ids=lambda caminho: caminho.stem)
def test_aula_roda_sem_erro(aula, capsys):
    runpy.run_path(str(aula), run_name="__main__")
    assert capsys.readouterr().out, "A aula deveria imprimir alguma coisa"


def test_aula_inexistente_gera_erro():
    with pytest.raises(ValueError):
        executar_aula(len(AULAS) + 1)
