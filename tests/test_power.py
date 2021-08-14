# -*- coding: utf-8 -*-
# @Time    : 2021/8/12 6:51
# @Author  : pixb
# @Email   : tpxsky@163.com
# @File    : test_power.py
# @Software: PyCharm
# @Description:
from hearthstone.entities import Player, Game, Card
from hearthstone.enums import Zone

from hslog.export import EntityTreeExporter, CompositeExporter
from hslog.parser import *
from model.t_game_state import t_game_state

HEARTHSTONE_POWER_LOG_PATH = "C:/game/Hearthstone/Logs/Power.log"

def print_player(player:Player):
    print("\t player_id:{}\n".format(player.player_id))
    print("\t account_hi:{}\n".format(player.account_hi))
    print("\t account_lo:{}\n".format(player.account_lo))
    print("\t name:{}\n".format(player.name))
    print("\t names:{}\n".format(player.names))
    print("\t initial_deck:\n")
    for desk in player.initial_deck:
        print("\t\t desk:{}".format(desk))
    print("\t known_starting_deck_list:\n")
    for startdesk in player.known_starting_deck_list:
        print("\t\t desk:{}".format(startdesk))
    print("\t entities:\n")
    for et in player.entities:
        print("\t\t et:{}".format(et))
        if et.zone == Zone.HAND:
            print_card(et)

    print("------------------------ RESOURCES:{}\n".format(player.tags.get(GameTag.RESOURCES)))

    print("\t hero:{}\n".format(player.hero))
    print("\t heros:\n")
    for hero in player.heroes:
        print("\t\t et:{}".format(hero))
    print("\t starting_hero{}:\n".format(player.starting_hero))
    print("\t is_ai:{}:\n".format(player.is_ai))
    print("\t in_zone:\n")
    for zoneEt in player.in_zone(player.zone):
        print("\t\t in zone[{}]:{}".format(Zone.DECK, zoneEt))

    print("\t tags:\n")
    for tag in player.tags:
        print("\t\t tag: {}\n".format(tag))
    print("\t state:{}\n".format(player.tags.get(GameTag.PLAYSTATE)))
    print("player PLAYSTATE:{}".format(player.tags.get(GameTag.PLAYSTATE)))
    print("player CURRENT_PLAYER {}".format(player.tags.get(GameTag.CURRENT_PLAYER)))

def print_card(card:Card):
    print("==================Card============================\n")
    print("card: {}\n".format(card))
    print("\tcard TAG_LAST_KNOWN_COST_IN_HAND:{}".format(card.tags.get(GameTag.TAG_LAST_KNOWN_COST_IN_HAND)))
    print("\tcard zone pos:{}".format(card.tags.get(GameTag.ZONE_POSITION)))



def print_game(game:Game):
    print("\n ====================Game=====================\n")
    print("game id:{}".format(game.id))
    print("game.state:{}".format(game.initial_state))
    print("game tag state:{}".format(game.tags.get(GameTag.STATE)))
    print("game NUM_TURNS_IN_PLAY:{}".format(game.tags.get(GameTag.NUM_TURNS_IN_PLAY)))



def test_power():
    parser = LogParser()
    with open(HEARTHSTONE_POWER_LOG_PATH, "r", encoding="utf8") as f:
        parser.read(f)

    packet_tree = parser.games[0]
    exporter = EntityTreeExporter(packet_tree, player_manager=parser.player_manager)
    game = exporter.export()

    # parser.flush()
    # packet_tree = parser.games[0]
    # game = packet_tree.export().game
    print_game(game.game)

    # composite_exporter = CompositeExporter(packet_tree, [exporter])
    # for et in game.game.entities:
    #     print("et:\n"
    #           "\t type:{}\n"
    #           "\t zone:{}\n"
    #           "\t id:{}\n"
    #           .format(et.type, et.zone, et.id))

    # line = "TAG_CHANGE Entity=%s tag=ZONE value=HAND" % (entity_format)
    # packet = parser.handle_power(None, "TAG_CHANGE", None)

    print("test Power.log  player1 name:{}\n".format(game.game.players[0].name,),)
    player1 = game.game.players[0]
    print_player(player1)
    print("test Power.log  player2 name:{}\n".format(game.game.players[1].name,),)
    print("")

def test_game_state():
    parser = LogParser()
    with open(HEARTHSTONE_POWER_LOG_PATH, "r", encoding="utf8") as f:
        parser.read(f)

    packet_tree = parser.games[0]
    exporter = EntityTreeExporter(packet_tree, player_manager=parser.player_manager)
    game = exporter.export()
    player1 = game.game.players[0]
    player2 = game.game.players[1]

    game_state = t_game_state()
    game_state.game_entity_id = game.game.id
    game_state.my_name = player1.name
    game_state.oppo_name = player2.name
    game_state.my_player_id = player1.id
    game_state.oppo_player_id = player2.id



    print("==" * 20)
    print(game_state)



if __name__ == "__main__":
    test_power()

