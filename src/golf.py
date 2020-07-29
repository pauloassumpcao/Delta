# -*- coding: utf-8 -*-
# Delta.golf.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Jogo da Memória.

.. codeauthor:: Paulo Assumpção <paulo.assump@gmail.com>

Classes neste modulo:
    :py:class:`Card` Classe responsável pelo comportamento e rederização das cartas.
    :py:class:`Game2x5` Classe responsável pela jogabilidade.

Changelog
---------
.. versionadded::    20.07
        Grid 2x5 de cartões do jogo da memória
        shuffle das cartas
        bind do click sobre o botão
        regra do jogo

"""

from vitollino.main import Cena, Elemento, Texto, STYLE
# em vez de sleep temos que usar o timer do navegador
# https://www.brython.info/static_doc/en/timer.html
from browser import timer
import random
import time

__version__ = "20.07"
__author__ = "Paulo Assumpção"

IMG_CARD_FACE_DOWN = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_verso.png?disp=inline"
IMG_CARD_1 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_pycharm.png?disp=inline"
IMG_CARD_2 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_Linux.png?disp=inline"
IMG_CARD_3 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_Gitlab.png?disp=inline"
IMG_CARD_4 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_github.png?disp=inline"
IMG_CARD_5 = "http://activufrj.nce.ufrj.br/file/ProgOO/Card_Activ.png?disp=inline"

IMG_WIDTH = 150
IMG_HEIGHT = 150

class Card():
    """
        Classe responsável pela renderização das faces das cartas
        
        :param name: nome da carta
        :param image: imagem da carta quando viarada para cima
        :param position: posição da carta na Cena
        :param cena: a cena onde a carta será renderizada
        :param rule: o método que contém as regras do jogo
    """      
    def __init__(self, name, image, position, cena, rule):
        self.rule = rule
        self.name = name
        self.cena = cena
        self.image = image
        self.faceDown = True
        self.position = position
        self.pos_x = 50 + self.position[0] * IMG_WIDTH
        self.pos_y = 50 + self.position[1] * IMG_HEIGHT
        self.card = Elemento(IMG_CARD_FACE_DOWN, tit=self.name, x=self.pos_x, y=self.pos_y, width=IMG_WIDTH, height=IMG_HEIGHT, cena=self.cena)
        self.card.elt.bind("click", self.turnUp)

    def turnUp(self, env=None):
        """
            Renderiza a carta com a face para cima e altera o comportamento do clique da carta
       
        """
        self.card = Elemento(self.image, tit=self.name, x=self.pos_x, y=self.pos_y, width=IMG_WIDTH, height=IMG_HEIGHT, cena=self.cena)
        self.faceDown = False
        self.card.elt.bind("click", self.turnDown)
        self.rule(self)

    def turnDown(self, env=None):
        """
            Renderiza a carta com a face para baixo e altera o comportamento do clique da carta
       
        """
        self.card = Elemento(IMG_CARD_FACE_DOWN, tit=self.name, x=self.pos_x, y=self.pos_y, width=IMG_WIDTH, height=IMG_HEIGHT, cena=self.cena)
        self.faceDown = True
        self.card.elt.bind("click", self.turnUp)


class Game2x5:
    """
        Classe principal do jogo da memória, responsável pelas regras do jogo e da jogabilidade
       
    """
    # referência para o Elemento
    previous_selected_card = None
    list_objects = None

    cena = Cena()

    def vai(self):
        """
            Inicia o jogo.
            
        """
        self.create_2x5_cards()

    def create_2x5_cards(self):
        """
            Cria uma matriz contendo 10 cartas distribuidas em 2 linhas e 5 colunas
            
        """       
        
        # Exemplo de matrix do jogo
        #    matrix 2x5:
        #    1A 1B 2A 2B 3A
        #    3B 4A 4B 5A 5B
        
        list_cards = self.shuffle_cards()
        # aqui, list_objects tem que ser atributo de instância da classe Game2x5
        # pois ele vai ser usado no método verifyingGameOver():
        # rule também não pode ser estático pois vai usar o método verifyingGameOver()
        self.list_objects = [
            Card("PyCharm", IMG_CARD_1, list_cards[0], Game2x5.cena, self.rule),
            Card("PyCharm", IMG_CARD_1, list_cards[1], Game2x5.cena, self.rule),
            Card("Linux", IMG_CARD_2, list_cards[2], Game2x5.cena, self.rule),
            Card("Linux", IMG_CARD_2, list_cards[3], Game2x5.cena, self.rule),
            Card("GitLab", IMG_CARD_3, list_cards[4], Game2x5.cena, self.rule),
            Card("GitLab", IMG_CARD_3, list_cards[5], Game2x5.cena, self.rule),
            Card("GitHub", IMG_CARD_4, list_cards[6], Game2x5.cena, self.rule),
            Card("GitHub", IMG_CARD_4, list_cards[7], Game2x5.cena, self.rule),
            Card("Activ", IMG_CARD_5, list_cards[8], Game2x5.cena, self.rule),
            Card("Activ", IMG_CARD_5, list_cards[9], Game2x5.cena, self.rule)]
        Game2x5.cena.vai()


    # @staticmethod
    def rule(self, selected_card):
        """
            Regra do jogo da memória.
            Verifica se as cartas são iguais, se sim mantem elas para cima,
            caso contrário, virar para baixo
            :param selected_card: a carta que foi selecionada
            
        """

        # abortar se o clique ocorrer sobre a mesma carta
        if Game2x5.previous_selected_card == selected_card:
            return

        # tem um par selecionado?
        if Game2x5.previous_selected_card is None:
            # primeira carta selecionada
            Game2x5.previous_selected_card = selected_card
            # desabilita o clique sobre carta virada
            Game2x5.previous_selected_card.card.elt.unbind("click")
            return

        # Não acertou
        if Game2x5.previous_selected_card.name != selected_card.name:
            # reabilita a ação o clique e vira a carta 1 para baixo
            Game2x5.previous_selected_card.card.elt.bind("click", Game2x5.previous_selected_card.turnUp)
            Game2x5.previous_selected_card.turnDown()

            # reabilita a ação do clique e vira a carta 2 para baixo
            selected_card.card.elt.bind("click", selected_card.turnUp)
            def turn(*_):
                selected_card.turnDown()
                Game2x5.previous_selected_card = None
            # uma maneira de esperar é usar o foi do texto
            # ele é chamado quando se fecha o texto clicando o <x>
            Texto(Game2x5.cena, "Opa!", "Errou!!!", foi=turn).vai()

            # Aqui tem q esperar pelo menos 3 segundos, como fazer? (sleep, não funciona)
            # outra é usar o set_timeout do timer
            # timer.set_timeout(turn, 3000)
        # acertou
        else:
            # desabilita o clique sobre as cartas acertadas
            Game2x5.previous_selected_card = None
            # aqui não pode ser verifyingGameOver estatico
            self.verifyingGameOver()
            selected_card.card.elt.unbind("click")
            Texto(Game2x5.cena, "Acertou!!!").vai()

    # @staticmethod
    def verifyingGameOver(self):
        """
            Verifica se o jogo chegou ao fim
            
        """
        # object é palavra reservada, use _object
        for _object in self.list_objects:
            if _object.faceDown == True:
                return

        def proximo_jogo(*_):
            from delta.india import Game2x3
            Game2x3().vai()
        # usa o foi do texto para chamar o próximo jogo.
        Texto(Game2x5.cena, "GameOver!!!", foi=proximo_jogo).vai()
        # proxima sala


    def shuffle_cards(self):
        """
            Embaralha as cartas
            
        """
        list_cards =  [(0,0), (1,0), (2,0), (3,0), (4,0), (0,1), (1,1), (2,1), (3,1), (4,1)]
        random.shuffle(list_cards)
        return list_cards


if __name__ == "__main__":
    Game2x5().vai()
