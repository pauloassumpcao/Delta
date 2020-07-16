# -*- coding: utf-8 -*-
# Delta.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Tutorial Dois - Brincando de git.

.. codeauthor:: Paulo Assumpção <paulo.assump@gmail.com>

 - Como criar um repositório no github
 - Como clonar usando o comando git
 - Como comitar usando o comando git

- Classes nesse módulo:
    :py:class:Main Exemplo de classe qualquer



Changelog
---------
.. versionadded::    20.07
        Documentação do tutorial

"""

class Main:
    """Classe exemplo

        :param versao: versão desse exemplo
    """
    def __init__(self, versao):
        print("classe exemplo, versao {}".format(versao))


if __name__ == "__name__":
    Main(1)