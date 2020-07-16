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
        Adicionar o gerenciador de chamadas http via bottle
"""

# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route

@route('/')
def hello_world():
    return 'Tutorial Dois - aprendendo Git e Bottle'

@route('/oi')
def oi_mundo():
    return 'Tutorial Dois - ensaiando uma nova rota'

application = default_app()

