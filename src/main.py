# -*- coding: utf-8 -*-
# Delta.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Tutorial Dois - Brincando de git.

.. codeauthor:: Paulo Assumpcao <paulo.assump@gmail.com.br>

- Como criar um repositório no github
- Como clonar usando o comando git
- Como comitar usando o comando git

Classes neste modulo:
    :py:class:`Main` Exemplo de classe qualquer.

Changelog
---------
.. versionadded::    20.07
        Documentação do tutorial.

"""

class Main:
    """Classe exemplo

        :param versao: versão desse exemplo
    """
    def __init__(self, versao="20.07"):
        self.versao = versao
        #print("classe exemplo, versao {}".format(versao))

    def get_versao(self):
        """Retorna a versao do sistema

            :return: A versao do sistema
        """
        return self.versao


if __name__ == "__main__":
    print(Main().get_versao())