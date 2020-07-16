# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
""" Tutorial Um - respondendo dúvidas do SuperPython.

.. codeauthor:: Paulo Assumpcao <paulo.assump@gmail.com.br>

- Como associar um evento a uma imagem
- Como combinar cenas em salas diferentes
- Como capturar o teclado

Sem Classes neste modulo:

Changelog
---------
.. versionadded::    20.07
        Adiciona o gerenciador de chamadas http via bottle.

"""
from bottle import default_app, route, static_file
from main import Main

@route('/')
def hello_world():
    return 'Tutorial Dois - aprendendo Git e Bottle'

@route('/oi')
def oi_mundo():
    return 'Tutorial Dois - ensaiando uma nova rota'

@route('/vs')
def vs_mundo():
    return 'Tutorial Dois - Versão do sistema: {}'.format(Main().get_versao())

@route('/doc/<filename:re:.*\.html>')
def doc_mundo(filename):
    return static_file(filename, root='/home/PauloAssumpcao/dev/Delta/docs/build/html', mimetype='text/html')

@route('/doc/<filename:re:.*\.css>')
def css_mundo(filename):
    return static_file(filename, root='/home/PauloAssumpcao/dev/Delta/docs/build/html/', mimetype='text/css')

application = default_app()