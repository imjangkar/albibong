import json
import os

jonPath = os.path.join(
    os.path.dirname(__file__), "../../resources/ao-bin-dumps-json/mobs.json"
)

with open(jonPath) as json_file:
    mob_by_id = json.load(json_file)


class MobInfo:
    offset = 14
    @classmethod
    def get_mob_id(cls, code: int):
        try:
            return mob_by_id["Mobs"]["Mob"][code - cls.offset]
        except Exception as e:
            print(e)
            return None
        
    @classmethod
    def get_mob_by_name(cls, name: str):
        for index, mob in enumerate(mob_by_id["Mobs"]["Mob"]):
            if mob["@uniquename"] == name:
                return index + cls.offset, mob
        return None, None

    @classmethod
    def deserialize(cls, data, enchant, HarvestablesInfo):
        tier = data["@tier"]
        unique_name = data["@uniquename"]
        harvestable_type = cls._convert_harvestable_type(data, HarvestablesInfo)
        type = cls._convert_mob_type(data, harvestable_type)
        # rarity = cls._convert_rarity(data)
        mob_name = cls._convert_mob_name(data)
        avatar = cls.convert_avater(type, harvestable_type, tier, enchant)

        return {
            "tier": tier,
            "unique_name": unique_name,
            "type": type,
            "harvestable_type": harvestable_type,
            # "rarity": rarity,
            "mob_name": mob_name,
            "avatar": avatar
        }
    
    @staticmethod
    def convert_avater(type, harvestable_type, tier, enchant):
        if type == "HARVESTABLE":
            if tier != '2' or tier != '1':
                return f"{harvestable_type.lower()}_{tier}_{enchant}"
        return None
    

    @staticmethod
    def _convert_harvestable_type(data, HarvestablesInfo):
        if data.get("Loot") and data["Loot"].get("Harvestable") and data["Loot"]["Harvestable"].get("@type"):
            data = HarvestablesInfo.get_harvestables_by_name(HarvestablesInfo, data["Loot"]["Harvestable"]["@type"])
            if data:
                return data.get("@resource")
        return None
    
    @staticmethod
    def _convert_mob_type(data, harvestable_type):
        if harvestable_type != None:
            return "HARVESTABLE"

        if "EVENT" in data["@uniquename"]:
            return "EVENT"

        if "_MOB_MISTS_" in data["@uniquename"]:
            return "BOSS"
        
        if "_BOSS" in data["@uniquename"]:
            return "BOSS"

        if "_CHAMPION" in data["@uniquename"] or "_MINIBOSS" in data["@uniquename"] or "_MINIBOSS" in data["@uniquename"]:
            return "WORLD_PROCKED"

        return None
    

    # @staticmethod
    # def _convert_rarity(mob_metadata):
    #     if mob_metadata["@uniquename"].endswith("_STANDARD"):
    #         return 1
    #     if mob_metadata["@uniquename"].endswith("_UNCOMMON"):
    #         return 2
    #     if mob_metadata["@uniquename"].endswith("_RARE"):
    #         return 3
    #     if mob_metadata["@uniquename"].endswith("_LEGENDARY"):
    #         return 4

    #     return 0
    
    @staticmethod
    def _convert_mob_name(mob_metadata):
        if "_CRYSTALSPIDER_" in mob_metadata["@uniquename"]:
            return "CRYSTAL_SPIDER"
        if "_MISTS_SPIDER_" in mob_metadata["@uniquename"]:
            return "SPIDER"
        if "_MISTS_FAIRYDRAGON" in mob_metadata["@uniquename"]:
            return "DRAGON"
        if "_MISTS_GRIFFIN" in mob_metadata["@uniquename"]:
            return "GRIFFIN"
        if "AVALON_TREASURE_MINION" in mob_metadata["@uniquename"]:
            return "DRONE"
        

        return None

