# -*- coding: utf-8 -*-
# @Time    : 2021/8/13 4:51
# @Author  : pixb
# @Email   : tpxsky@163.com
# @File    : t_game_state.py
# @Software: PyCharm
# @Description:
from hearthstone.enums import GameTag, State

from hslog import LogParser
from hslog.export import EntityTreeExporter
from model.t_my_state import t_my_state
from model.t_oppo_state import t_oppo_state


HEARTHSTONE_POWER_LOG_PATH = "C:/game/Hearthstone/Logs/Power.log"

class t_game_state:
    def __init__(self):
        self.parser = LogParser()
        self.parse = None
        self.game = None
        self.game_entity_id = 0
        self.player_id_map_dict = {}
        self.my_name = ""
        self.oppo_name = ""
        self.my_player_id = 0
        self.oppo_player_id = 0
        self.entity_dict = {}
        self.current_update_id = 0
        self.my_hero = None
        self.my_state = t_my_state()
        self.oppo_state = t_oppo_state()
        self.init()

    def __str__(self):
        res = \
            f"""t_game_state:
    game_entity_id: {self.game_entity_id}
    my_name: {self.my_name}
    oppo_name: {self.oppo_name}
    my_player_id: {self.my_player_id}
    oppo_player_id: {self.oppo_player_id}
    current_update_id: {self.current_update_id}
    entity_keys: {[list(self.entity_dict.keys())]}

"""
        return res

    def init(self):
        with open(HEARTHSTONE_POWER_LOG_PATH, "r", encoding="utf8") as f:
            self.parser.read(f)
        packet_tree = self.parser.games[0]
        exporter = EntityTreeExporter(packet_tree, player_manager=self.parser.player_manager)
        self.game = exporter.export()
        # my hero



    @property
    def is_end(self):
        return self.game.tags.get(GameTag.STATE) == State.COMPLETE
