from albibong.classes.object_into.harvestables_info import HarvestablesInfo
from albibong.classes.object_into.mob_info import MobInfo

import unittest

class TestResources(unittest.TestCase):
    def test_get_mob_id(self):
        testing_id = 383
        testing_name = "MOB_RABBIT"
        
        mobInfo = MobInfo.get_mob_id(testing_id)
        self.assertIsNotNone(mobInfo)

        mobData = MobInfo.deserialize(mobInfo, HarvestablesInfo)
        self.assertIsNotNone(mobData)

        self.assertEqual(mobData["unique_name"], testing_name)
        self.assertEqual(mobData["tier"], '1')
        self.assertEqual(mobData["type"], None)
        self.assertEqual(mobData["harvestable_type"], None)
        self.assertEqual(mobData["rarity"], 0)
        self.assertEqual(mobData["mob_name"], None)

    def test_get_mob2_id(self):
        testing_id = 517
        testing_name = "T4_MOB_CRITTER_FIBER_SWAMP_GREEN"
        
        mobInfo = MobInfo.get_mob_id(testing_id)
        self.assertIsNotNone(mobInfo)

        mobData = MobInfo.deserialize(mobInfo, HarvestablesInfo)
        self.assertIsNotNone(mobData)

        self.assertEqual(mobData["unique_name"], testing_name)
        self.assertEqual(mobData["tier"], '4')
        self.assertEqual(mobData["type"], "HARVESTABLE")
        self.assertEqual(mobData["harvestable_type"], "FIBER")
        self.assertEqual(mobData["rarity"], 0)
        self.assertEqual(mobData["mob_name"], None)

    def test_get_mob_by_name(self):
        test_data = [
            [407, "T1_MOB_HIDE_SWAMP_TOAD"],
            [383, "MOB_RABBIT"],
            [409, "T3_MOB_HIDE_SWAMP_GIANTTOAD"],
            [410, "T3_MOB_DYNAMIC_HIDE_SWAMP_GIANTTOAD"],
            [515, "T3_MOB_CRITTER_FIBER_SWAMP_GREEN"],
            [517, "T4_MOB_CRITTER_FIBER_SWAMP_GREEN"]
        ]
        
        for testing_id, testing_name in test_data:
            with self.subTest(testing_name=testing_name):
                try:
                    index, mob = MobInfo.get_mob_by_name(testing_name)
                    self.assertIsNotNone(mob)
                    self.assertEqual(mob["@uniquename"], testing_name)
                    self.assertEqual(index, testing_id)
                except Exception as e:
                    self.fail(f"Test failed for {testing_name} with exception: {e}")

if __name__ == '__main__':
    unittest.main()
