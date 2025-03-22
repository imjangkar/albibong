import unittest
from albibong.classes.radar import Radar

class TestRadar(unittest.TestCase):
    def setUp(self):
        self.radar = Radar()

    def test_simple(self):
        self.assertEqual(1 + 1, 2)

    def test_add_solo_dungeon(self):
        id = 1
        location = [1, 2]
        name = "T5_PROTAL_SOLO"
        enchant = 1
        parameters = {0: 275023, 1: [60.0, -310.0], 2: 90.0, 3: 'T5_PROTAL_SOLO', 5: 'SWAMP_RED_RANDOM_EXIT_10x10_PORTAL_SOLO_B_CORRUPT', 6: 44, 7: True, 8: 0, 11: True, 14: 0, 16: -1, 17: 1, 19: 0, 252: 319}

        self.radar.add_dungeon(id, location, name, enchant, parameters)
        self.assertEqual(self.radar.dungeon_list[0]["id"], id)

    def test_add_solo_dungeon(self):
        id = 1
        location = [1, 2]
        name = "T5_MORGANA"
        enchant = 1
        parameters = {0: 275023, 1: [60.0, -310.0], 2: 90.0, 3: 'T5_PROTAL_SOLO', 5: 'SWAMP_RED_RANDOM_EXIT_10x10_PORTAL_SOLO_B_CORRUPT', 6: 44, 7: True, 8: 0, 11: True, 14: 0, 16: -1, 17: 1, 19: 0, 252: 319}

        self.radar.add_dungeon(id, location, name, enchant, parameters)
        self.assertEqual(self.radar.dungeon_list[id]["id"], id)


    def test_add_corrupted_dungeon(self):
        id = 1
        location = [1, 2]
        name = "CORRUPTED_SOLO_NONLETHAL"
        enchant = 1
        parameters = {0: 275023, 1: [60.0, -310.0], 2: 90.0, 3: 'CORRUPTED_SOLO_NONLETHAL', 5: 'SWAMP_RED_RANDOM_EXIT_10x10_PORTAL_SOLO_B_CORRUPT', 6: 44, 7: True, 8: 0, 11: True, 14: 0, 16: -1, 17: 1, 19: 0, 252: 319}
       


        self.radar.add_dungeon(id, location, name, enchant, parameters)
        self.assertEqual(self.radar.dungeon_list[id]["id"], id)

    def test_add_hellgate_dungeon(self):
        id = 1
        location = [1, 2]
        name = "HELLGATE_2V2_NON_LETHAL" 
        enchant = 1
        parameters = {0: 275023, 1: [60.0, -310.0], 2: 90.0, 3: 'CORRUPTED_SOLO_NONLETHAL', 5: 'SWAMP_RED_RANDOM_EXIT_10x10_PORTAL_SOLO_B_CORRUPT', 6: 44, 7: True, 8: 0, 11: True, 14: 0, 16: -1, 17: 1, 19: 0, 252: 319}
       


        self.radar.add_dungeon(id, location, name, enchant, parameters)
        self.assertEqual(self.radar.dungeon_list[id]["id"], id)

    def test_add_other_dungeon(self):
        id = 1
        location = [1, 2]
        name = "UNKNOW" 
        enchant = 1
        parameters = {0: 275023, 1: [60.0, -310.0], 2: 90.0, 3: 'CORRUPTED_SOLO_NONLETHAL', 5: 'SWAMP_RED_RANDOM_EXIT_10x10_PORTAL_SOLO_B_CORRUPT', 6: 44, 7: True, 8: 0, 11: True, 14: 0, 16: -1, 17: 1, 19: 0, 252: 319}
       


        self.radar.add_dungeon(id, location, name, enchant, parameters)
        self.assertEqual(self.radar.dungeon_list[id]["id"], id)

if __name__ == '__main__':
    unittest.main()
