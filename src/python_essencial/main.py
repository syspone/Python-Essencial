"""Menu para listar e executar as aulas do curso.

Uso:
    python -m python_essencial          # lista as aulas e pergunta qual rodar
    python -m python_essencial 4        # roda direto a aula 4
"""

import runpy
import sys
from pathlib import Path

from python_essencial.config import DIR_AULAS


def listar_aulas() -> list[Path]:
    """Retorna os arquivos de aula em ordem (aula01, aula02, ...)."""
    return sorted(DIR_AULAS.glob("aula*.py"))


def executar_aula(numero: int) -> None:
    """Executa a aula pelo número, como se fosse rodada direto no terminal."""
    aulas = listar_aulas()
    if not 1 <= numero <= len(aulas):
        raise ValueError(f"Aula {numero} não existe. Escolha de 1 a {len(aulas)}.")
    runpy.run_path(str(aulas[numero - 1]), run_name="__main__")


def main() -> None:
    aulas = listar_aulas()

    if len(sys.argv) > 1:
        escolha = sys.argv[1]
    else:
        print("Aulas disponíveis:")
        for indice, aula in enumerate(aulas, start=1):
            print(f"  {indice}. {aula.stem}")
        escolha = input("Qual aula deseja rodar? ")

    try:
        executar_aula(int(escolha))
    except ValueError as erro:
        print(f"Opção inválida: {erro}")
        sys.exit(1)


if __name__ == "__main__":
    main()
