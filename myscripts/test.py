class Offsets:
    LEAVE = [0]
    HARVESTABLE_CHANGE_STATE = [0, 1, 2]
    MOVE_REQUEST = [1, 3, 4]  # Last offset not used
    MOB_CHANGE_STATE = [0, 1]
    NEW_HARVESTABLE_OBJECT = [0, 5, 7, 8, 10, 11]
    NEW_DUNGEON_EXIT = [0, 1, 3, 8]
    
    NEW_MOB_EVENT = [0, 1, 8, 13, 14, 33]

    CHANGE_FLAGGING_FINISHED = [0, 1]
    CHARACTER_EQUIPMENT_CHANGED = [0, 2, 7]
    HEALTH_UPDATE_EVENT = [0, 3]
    JOIN_RESPONSE = [0, 2, 57, 77, 8, 48, 9]
    NEW_CHARACTER = [0, 1, 8, 51, 53, 16, 20, 22, 23, 40, 43]
    
    NEW_FISHING_ZONE_OBJECT = [0, 1, 2, 3]
    
    NEW_WISP_GATE = [0, 2, 5]
    WISP_GATE_OPENED = [0, 1]

    # Not used yet
    REGENERATION_HEALTH_CHANGED_EVENT = [0, 4, 2, 3, 4]
    MOUNTED = [0, 2]

    # Used by original
    CHANGE_CLUSTER = [0, 1, 3]

    # Not supported
    KEY_SYNC = [0]  # Note Used
    MOVE = [0, 1]  # Used own logic
    NEW_LOOT_CHEST = [0, 1, 3, 17]  # Used own logic


print(Offsets.HARVESTABLE_CHANGE_STATE[0])
