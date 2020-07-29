# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
""" Tutorial Um - respondendo dúvidas do SuperPython.

.. codeauthor:: Paulo Assumpcao <paulo.assump@gmail.com.br>

- Rotas para o memorygame
- Rota para Oi mundo
- Rota para a versão do sistema
- Rota para o PyMundo
- Rota para o doc_mundo
- Rota para o css_mundo

Sem Classes neste modulo:

Changelog
---------
.. versionadded::    20.07
        Adiciona o gerenciador de chamadas http via bottle.

"""
from bottle import default_app, route, static_file
from main import Main

@route('/')
def memory_game():
    return static_file('index.html', root='/home/PauloAssumpcao/dev/Delta/src/', mimetype='text/html')

@route('/oi')
def oi_mundo():
    return 'Tutorial Dois - ensaiando uma nova rota'

@route('/vs')
def vs_mundo():
    return 'Tutorial Dois - Versão do sistema: {}'.format(Main().get_versao())

@route('/<filename:re:.*\.py>')
def py_mundo(filename):
    return static_file(filename, root='/home/PauloAssumpcao/dev/Delta/src', mimetype='text/python')


@route('/<filename:re:.*\.html>')
def doc_mundo(filename):
    return static_file(filename, root='/home/PauloAssumpcao/dev/Delta/docs/build/html', mimetype='text/html')

@route('/doc/<filename:re:.*\.css>')
def css_mundo(filename):
    return static_file(filename, root='/home/PauloAssumpcao/dev/Delta/docs/build/html/', mimetype='text/css')

application = default_app()
