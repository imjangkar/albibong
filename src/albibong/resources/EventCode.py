from enum import Enum


class EventCode(Enum):
    LEAVE = 1
    JOIN_FINISHED = 2
    MOVE = 3
    TELEPORT = 4
    CHANGE_EQUIPMENT = 5
    HEALTH_UPDATE = 6
    HEALTH_UPDATES = 7
    ENERGY_UPDATE = 8
    DAMAGE_SHIELD_UPDATE = 9
    CRAFTING_FOCUS_UPDATE = 10
    ACTIVE_SPELL_EFFECTS_UPDATE = 11
    RESET_COOLDOWNS = 12
    ATTACK = 13
    CAST_START = 14
    CHANNELING_UPDATE = 15
    CAST_CANCEL = 16
    CAST_TIME_UPDATE = 17
    CAST_FINISHED = 18
    CAST_SPELL = 19
    CAST_SPELLS = 20
    CAST_HIT = 21
    CAST_HITS = 22
    STORED_TARGETS_UPDATE = 23
    CHANNELING_ENDED = 24
    ATTACK_BUILDING = 25
    INVENTORY_PUT_ITEM = 26
    INVENTORY_DELETE_ITEM = 27
    INVENTORY_STATE = 28
    NEW_CHARACTER = 29
    NEW_EQUIPMENT_ITEM = 30
    NEW_SIEGE_BANNER_ITEM = 31
    NEW_SIMPLE_ITEM = 32
    NEW_FURNITURE_ITEM = 33
    NEW_KILL_TROPHY_ITEM = 34
    NEW_JOURNAL_ITEM = 35
    NEW_LABORER_ITEM = 36
    NEW_EQUIPMENT_ITEM_LEGENDARY_SOUL = 37
    NEW_SIMPLE_HARVESTABLE_OBJECT = 38
    NEW_SIMPLE_HARVESTABLE_OBJECT_LIST = 39
    NEW_HARVESTABLE_OBJECT = 40
    NEW_TREASURE_DESTINATION_OBJECT = 41
    TREASURE_DESTINATION_OBJECT_STATUS = 42
    CLOSE_TREASURE_DESTINATION_OBJECT = 43
    NEW_SILVER_OBJECT = 44
    NEW_BUILDING = 45
    HARVESTABLE_CHANGE_STATE = 46
    MOB_CHANGE_STATE = 47
    FACTION_BUILDING_INFO = 48
    CRAFT_BUILDING_INFO = 49
    REPAIR_BUILDING_INFO = 50
    MELD_BUILDING_INFO = 51
    CONSTRUCTION_SITE_INFO = 52
    PLAYER_BUILDING_INFO = 53
    FARM_BUILDING_INFO = 54
    TUTORIAL_BUILDING_INFO = 55
    LABORER_OBJECT_INFO = 56
    LABORER_OBJECT_JOB_INFO = 57
    MARKET_PLACE_BUILDING_INFO = 58
    HARVEST_START = 59
    HARVEST_CANCEL = 60
    HARVEST_FINISHED = 61
    TAKE_SILVER = 62
    ACTION_ON_BUILDING_START = 63
    ACTION_ON_BUILDING_CANCEL = 64
    ACTION_ON_BUILDING_FINISHED = 65
    ITEM_REROLL_QUALITY_FINISHED = 66
    INSTALL_RESOURCE_START = 67
    INSTALL_RESOURCE_CANCEL = 68
    INSTALL_RESOURCE_FINISHED = 69
    CRAFT_ITEM_FINISHED = 70
    LOGOUT_CANCEL = 71
    CHAT_MESSAGE = 72
    CHAT_SAY = 73
    CHAT_WHISPER = 74
    CHAT_MUTED = 75
    PLAY_EMOTE = 76
    STOP_EMOTE = 77
    SYSTEM_MESSAGE = 78
    UTILITY_TEXT_MESSAGE = 79
    UPDATE_MONEY = 80
    UPDATE_FAME = 81
    UPDATE_LEARNING_POINTS = 82
    UPDATE_RE_SPEC_POINTS = 83
    UPDATE_CURRENCY = 84
    UPDATE_FACTION_STANDING = 85
    UPDATE_MIST_CITY_STANDING = 86
    RESPAWN = 87
    SERVER_DEBUG_LOG = 88
    CHARACTER_EQUIPMENT_CHANGED = 89
    REGENERATION_HEALTH_CHANGED = 90
    REGENERATION_ENERGY_CHANGED = 91
    REGENERATION_MOUNT_HEALTH_CHANGED = 92
    REGENERATION_CRAFTING_CHANGED = 93
    REGENERATION_HEALTH_ENERGY_COMBO_CHANGED = 94
    REGENERATION_PLAYER_COMBO_CHANGED = 95
    DURABILITY_CHANGED = 96
    NEW_LOOT = 97
    ATTACH_ITEM_CONTAINER = 98
    DETACH_ITEM_CONTAINER = 99
    INVALIDATE_ITEM_CONTAINER = 100
    LOCK_ITEM_CONTAINER = 101
    GUILD_UPDATE = 102
    GUILD_PLAYER_UPDATED = 103
    INVITED_TO_GUILD = 104
    GUILD_MEMBER_WORLD_UPDATE = 105
    UPDATE_MATCH_DETAILS = 106
    OBJECT_EVENT = 107
    NEW_MONOLITH_OBJECT = 108
    MONOLITH_HAS_BANNERS_PLACED_UPDATE = 109
    NEW_ORB_OBJECT = 110
    NEW_CASTLE_OBJECT = 111
    NEW_SPELL_EFFECT_AREA = 112
    UPDATE_SPELL_EFFECT_AREA = 113
    NEW_CHAIN_SPELL = 114
    UPDATE_CHAIN_SPELL = 115
    NEW_TREASURE_CHEST = 116
    START_MATCH = 117
    START_ARENA_MATCH_INFOS = 118
    END_ARENA_MATCH = 119
    MATCH_UPDATE = 120
    ACTIVE_MATCH_UPDATE = 121
    NEW_MOB = 122
    DEBUG_AGGRO_INFO = 123
    DEBUG_VARIABLES_INFO = 124
    DEBUG_REPUTATION_INFO = 125
    DEBUG_DIMINISHING_RETURN_INFO = 126
    DEBUG_SMART_CLUSTER_QUEUE_INFO = 127
    CLAIM_ORB_START = 128
    CLAIM_ORB_FINISHED = 129
    CLAIM_ORB_CANCEL = 130
    ORB_UPDATE = 131
    ORB_CLAIMED = 132
    ORB_RESET = 133
    NEW_WAR_CAMP_OBJECT = 134
    NEW_MATCH_LOOT_CHEST_OBJECT = 135
    NEW_ARENA_EXIT = 136
    GUILD_MEMBER_TERRITORY_UPDATE = 137
    INVITED_MERCENARY_TO_MATCH = 138
    CLUSTER_INFO_UPDATE = 139
    FORCED_MOVEMENT = 140
    FORCED_MOVEMENT_CANCEL = 141
    CHARACTER_STATS = 142
    CHARACTER_STATS_KILL_HISTORY = 143
    CHARACTER_STATS_DEATH_HISTORY = 144
    GUILD_STATS = 145
    KILL_HISTORY_DETAILS = 146
    FULL_ACHIEVEMENT_INFO = 147
    FINISHED_ACHIEVEMENT = 148
    ACHIEVEMENT_PROGRESS_INFO = 149
    FULL_ACHIEVEMENT_PROGRESS_INFO = 150
    FULL_TRACKED_ACHIEVEMENT_INFO = 151
    FULL_AUTO_LEARN_ACHIEVEMENT_INFO = 152
    QUEST_GIVER_QUEST_OFFERED = 153
    QUEST_GIVER_DEBUG_INFO = 154
    CONSOLE_EVENT = 155
    TIME_SYNC = 156
    CHANGE_AVATAR = 157
    CHANGE_MOUNT_SKIN = 158
    GAME_EVENT = 159
    KILLED_PLAYER = 160
    DIED = 161
    KNOCKED_DOWN = 162
    UNCONCIOUS = 163
    MATCH_PLAYER_JOINED_EVENT = 164
    MATCH_PLAYER_STATS_EVENT = 165
    MATCH_PLAYER_STATS_COMPLETE_EVENT = 166
    MATCH_TIME_LINE_EVENT_EVENT = 167
    MATCH_PLAYER_MAIN_GEAR_STATS_EVENT = 168
    MATCH_PLAYER_CHANGED_AVATAR_EVENT = 169
    INVITATION_PLAYER_TRADE = 170
    PLAYER_TRADE_START = 171
    PLAYER_TRADE_CANCEL = 172
    PLAYER_TRADE_UPDATE = 173
    PLAYER_TRADE_FINISHED = 174
    PLAYER_TRADE_ACCEPT_CHANGE = 175
    MINI_MAP_PING = 176
    MARKET_PLACE_NOTIFICATION = 177
    DUELLING_CHALLENGE_PLAYER = 178
    NEW_DUELLING_POST = 179
    DUEL_STARTED = 180
    DUEL_ENDED = 181
    DUEL_DENIED = 182
    DUEL_REQUEST_CANCELED = 183
    DUEL_LEFT_AREA = 184
    DUEL_RE_ENTERED_AREA = 185
    NEW_REAL_ESTATE = 186
    MINI_MAP_OWNED_BUILDINGS_POSITIONS = 187
    REAL_ESTATE_LIST_UPDATE = 188
    GUILD_LOGO_UPDATE = 189
    GUILD_LOGO_CHANGED = 190
    PLACEABLE_OBJECT_PLACE = 191
    PLACEABLE_OBJECT_PLACE_CANCEL = 192
    FURNITURE_OBJECT_BUFF_PROVIDER_INFO = 193
    FURNITURE_OBJECT_CHEAT_PROVIDER_INFO = 194
    FARMABLE_OBJECT_INFO = 195
    NEW_UNREAD_MAILS = 196
    MAIL_OPERATION_POSSIBLE = 197
    GUILD_LOGO_OBJECT_UPDATE = 198
    START_LOGOUT = 199
    NEW_CHAT_CHANNELS = 200
    JOINED_CHAT_CHANNEL = 201
    LEFT_CHAT_CHANNEL = 202
    REMOVED_CHAT_CHANNEL = 203
    ACCESS_STATUS = 204
    MOUNTED = 205
    MOUNT_START = 206
    MOUNT_CANCEL = 207
    NEW_TRAVELPOINT = 208
    NEW_ISLAND_ACCESS_POINT = 209
    NEW_EXIT = 210
    UPDATE_HOME = 211
    UPDATE_CHAT_SETTINGS = 212
    RESURRECTION_OFFER = 213
    RESURRECTION_REPLY = 214
    LOOT_EQUIPMENT_CHANGED = 215
    UPDATE_UNLOCKED_GUILD_LOGOS = 216
    UPDATE_UNLOCKED_AVATARS = 217
    UPDATE_UNLOCKED_AVATAR_RINGS = 218
    UPDATE_UNLOCKED_BUILDINGS = 219
    NEW_ISLAND_MANAGEMENT = 220
    NEW_TELEPORT_STONE = 221
    CLOAK = 222
    PARTY_INVITATION = 223
    PARTY_JOIN_REQUEST = 224
    PARTY_JOINED = 225
    PARTY_DISBANDED = 226
    PARTY_PLAYER_JOINED = 227
    PARTY_CHANGED_ORDER = 228
    PARTY_PLAYER_LEFT = 229
    PARTY_LEADER_CHANGED = 230
    PARTY_LOOT_SETTING_CHANGED_PLAYER = 231
    PARTY_SILVER_GAINED = 232
    PARTY_PLAYER_UPDATED = 233
    PARTY_INVITATION_ANSWER = 234
    PARTY_JOIN_REQUEST_ANSWER = 235
    PARTY_MARKED_OBJECTS_UPDATED = 236
    PARTY_ON_CLUSTER_PARTY_JOINED = 237
    PARTY_SET_ROLE_FLAG = 238
    PARTY_INVITE_OR_JOIN_PLAYER_EQUIPMENT_INFO = 239
    SPELL_COOLDOWN_UPDATE = 240
    NEW_HELLGATE_EXIT_PORTAL = 241
    NEW_EXPEDITION_EXIT = 242
    NEW_EXPEDITION_NARRATOR = 243
    EXIT_ENTER_START = 244
    EXIT_ENTER_CANCEL = 245
    EXIT_ENTER_FINISHED = 246
    NEW_QUEST_GIVER_OBJECT = 247
    FULL_QUEST_INFO = 248
    QUEST_PROGRESS_INFO = 249
    QUEST_GIVER_INFO_FOR_PLAYER = 250
    FULL_EXPEDITION_INFO = 251
    EXPEDITION_QUEST_PROGRESS_INFO = 252
    INVITED_TO_EXPEDITION = 253
    EXPEDITION_REGISTRATION_INFO = 254
    ENTERING_EXPEDITION_START = 255
    ENTERING_EXPEDITION_CANCEL = 256
    REWARD_GRANTED = 257
    ARENA_REGISTRATION_INFO = 258
    ENTERING_ARENA_START = 259
    ENTERING_ARENA_CANCEL = 260
    ENTERING_ARENA_LOCK_START = 261
    ENTERING_ARENA_LOCK_CANCEL = 262
    INVITED_TO_ARENA_MATCH = 263
    USING_HELLGATE_SHRINE = 264
    ENTERING_HELLGATE_LOCK_START = 265
    ENTERING_HELLGATE_LOCK_CANCEL = 266
    PLAYER_COUNTS = 267
    IN_COMBAT_STATE_UPDATE = 268
    OTHER_GRABBED_LOOT = 269
    TREASURE_CHEST_USING_START = 270
    TREASURE_CHEST_USING_FINISHED = 271
    TREASURE_CHEST_USING_CANCEL = 272
    TREASURE_CHEST_USING_OPENING_COMPLETE = 273
    TREASURE_CHEST_FORCE_CLOSE_INVENTORY = 274
    LOCAL_TREASURES_UPDATE = 275
    LOOT_CHEST_SPAWNPOINTS_UPDATE = 276
    PREMIUM_CHANGED = 277
    PREMIUM_EXTENDED = 278
    PREMIUM_LIFE_TIME_REWARD_GAINED = 279
    GOLD_PURCHASED = 280
    LABORER_GOT_UPGRADED = 281
    JOURNAL_GOT_FULL = 282
    JOURNAL_FILL_ERROR = 283
    FRIEND_REQUEST = 284
    FRIEND_REQUEST_INFOS = 285
    FRIEND_INFOS = 286
    FRIEND_REQUEST_ANSWERED = 287
    FRIEND_ONLINE_STATUS = 288
    FRIEND_REQUEST_CANCELED = 289
    FRIEND_REMOVED = 290
    FRIEND_UPDATED = 291
    PARTY_LOOT_ITEMS = 292
    PARTY_LOOT_ITEMS_REMOVED = 293
    REPUTATION_UPDATE = 294
    DEFENSE_UNIT_ATTACK_BEGIN = 295
    DEFENSE_UNIT_ATTACK_END = 296
    DEFENSE_UNIT_ATTACK_DAMAGE = 297
    UNRESTRICTED_PVP_ZONE_UPDATE = 298
    REPUTATION_IMPLICATION_UPDATE = 299
    NEW_MOUNT_OBJECT = 300
    MOUNT_HEALTH_UPDATE = 301
    MOUNT_COOLDOWN_UPDATE = 302
    NEW_EXPEDITION_AGENT = 303
    NEW_EXPEDITION_CHECK_POINT = 304
    EXPEDITION_START_EVENT = 305
    VOTE_EVENT = 306
    RATING_EVENT = 307
    NEW_ARENA_AGENT = 308
    BOOST_FARMABLE = 309
    USE_FUNCTION = 310
    NEW_PORTAL_ENTRANCE = 311
    NEW_PORTAL_EXIT = 312
    NEW_RANDOM_DUNGEON_EXIT = 313
    WAITING_QUEUE_UPDATE = 314
    PLAYER_MOVEMENT_RATE_UPDATE = 315
    OBSERVE_START = 316
    MINIMAP_ZERGS = 317
    MINIMAP_SMART_CLUSTER_ZERGS = 318
    PAYMENT_TRANSACTIONS = 319
    PERFORMANCE_STATS_UPDATE = 320
    OVERLOAD_MODE_UPDATE = 321
    DEBUG_DRAW_EVENT = 322
    RECORD_CAMERA_MOVE = 323
    RECORD_START = 324
    CLAIM_POWER_CRYSTAL_START = 325
    CLAIM_POWER_CRYSTAL_CANCEL = 326
    CLAIM_POWER_CRYSTAL_RESET = 327
    CLAIM_POWER_CRYSTAL_FINISHED = 328
    TERRITORY_CLAIM_START = 329
    TERRITORY_CLAIM_CANCEL = 330
    TERRITORY_CLAIM_FINISHED = 331
    TERRITORY_SCHEDULE_RESULT = 332
    TERRITORY_UPGRADE_WITH_POWER_CRYSTAL_RESULT = 333
    RETURNING_POWER_CRYSTAL_START = 334
    RETURNING_POWER_CRYSTAL_FINISHED = 335
    UPDATE_ACCOUNT_STATE = 336
    START_DETERMINISTIC_ROAM = 337
    GUILD_FULL_ACCESS_TAGS_UPDATED = 338
    GUILD_ACCESS_TAG_UPDATED = 339
    GVG_SEASON_UPDATE = 340
    GVG_SEASON_CHEAT_COMMAND = 341
    SEASON_POINTS_BY_KILLING_BOOSTER = 342
    FISHING_START = 343
    FISHING_CAST = 344
    FISHING_CATCH = 345
    FISHING_FINISHED = 346
    FISHING_CANCEL = 347
    NEW_FLOAT_OBJECT = 348
    NEW_FISHING_ZONE_OBJECT = 349
    FISHING_MINI_GAME = 350
    STEAM_ACHIEVEMENT_COMPLETED = 351
    UPDATE_PUPPET = 352
    CHANGE_FLAGGING_FINISHED = 353
    NEW_OUTPOST_OBJECT = 354
    OUTPOST_UPDATE = 355
    OUTPOST_CLAIMED = 356
    OVER_CHARGE_END = 357
    OVER_CHARGE_STATUS = 358
    PARTY_FINDER_FULL_UPDATE = 359
    PARTY_FINDER_UPDATE = 360
    PARTY_FINDER_APPLICANTS_UPDATE = 361
    PARTY_FINDER_EQUIPMENT_SNAPSHOT = 362
    PARTY_FINDER_JOIN_REQUEST_DECLINED = 363
    NEW_UNLOCKED_PERSONAL_SEASON_REWARDS = 364
    PERSONAL_SEASON_POINTS_GAINED = 365
    PERSONAL_SEASON_PAST_SEASON_DATA_EVENT = 366
    EASY_ANTI_CHEAT_MESSAGE_TO_CLIENT = 367
    MATCH_LOOT_CHEST_OPENING_START = 368
    MATCH_LOOT_CHEST_OPENING_FINISHED = 369
    MATCH_LOOT_CHEST_OPENING_CANCEL = 370
    NOTIFY_CRYSTAL_MATCH_REWARD = 371
    CRYSTAL_REALM_FEEDBACK = 372
    NEW_LOCATION_MARKER = 373
    NEW_TUTORIAL_BLOCKER = 374
    NEW_TILE_SWITCH = 375
    NEW_INFORMATION_PROVIDER = 376
    NEW_DYNAMIC_GUILD_LOGO = 377
    NEW_DECORATION = 378
    TUTORIAL_UPDATE = 379
    TRIGGER_HINT_BOX = 380
    RANDOM_DUNGEON_POSITION_INFO = 381
    NEW_LOOT_CHEST = 382
    UPDATE_LOOT_CHEST = 383
    LOOT_CHEST_OPENED = 384
    UPDATE_LOOT_PROTECTED_BY_MOBS_WITH_MINIMAP_DISPLAY = 385
    NEW_SHRINE = 386
    UPDATE_SHRINE = 387
    UPDATE_ROOM = 388
    NEW_MIST_DUNGEON_ROOM_MOB_SOUL = 389
    NEW_HELLGATE_SHRINE = 390
    UPDATE_HELLGATE_SHRINE = 391
    ACTIVATE_HELLGATE_EXIT = 392
    MUTE_PLAYER_UPDATE = 393
    SHOP_TILE_UPDATE = 394
    SHOP_UPDATE = 395
    EASY_ANTI_CHEAT_KICK = 396
    BATTL_EYE_SERVER_MESSAGE = 397
    UNLOCK_VANITY_UNLOCK = 398
    AVATAR_UNLOCKED = 399
    CUSTOMIZATION_CHANGED = 400
    BASE_VAULT_INFO = 401
    GUILD_VAULT_INFO = 402
    BANK_VAULT_INFO = 403
    RECOVERY_VAULT_PLAYER_INFO = 404
    RECOVERY_VAULT_GUILD_INFO = 405
    UPDATE_WARDROBE = 406
    CASTLE_PHASE_CHANGED = 407
    GUILD_ACCOUNT_LOG_EVENT = 408
    NEW_HIDEOUT_OBJECT = 409
    NEW_HIDEOUT_MANAGEMENT = 410
    NEW_HIDEOUT_EXIT = 411
    INIT_HIDEOUT_ATTACK_START = 412
    INIT_HIDEOUT_ATTACK_CANCEL = 413
    INIT_HIDEOUT_ATTACK_FINISHED = 414
    HIDEOUT_MANAGEMENT_UPDATE = 415
    HIDEOUT_UPGRADE_WITH_POWER_CRYSTAL_RESULT = 416
    IP_CHANGED = 417
    SMART_CLUSTER_QUEUE_UPDATE_INFO = 418
    SMART_CLUSTER_QUEUE_ACTIVE_INFO = 419
    SMART_CLUSTER_QUEUE_KICK_WARNING = 420
    SMART_CLUSTER_QUEUE_INVITE = 421
    RECEIVED_GVG_SEASON_POINTS = 422
    TOWER_POWER_POINT_UPDATE = 423
    OPEN_WORLD_ATTACK_SCHEDULE_START = 424
    OPEN_WORLD_ATTACK_SCHEDULE_FINISHED = 425
    OPEN_WORLD_ATTACK_SCHEDULE_CANCEL = 426
    OPEN_WORLD_ATTACK_CONQUER_START = 427
    OPEN_WORLD_ATTACK_CONQUER_FINISHED = 428
    OPEN_WORLD_ATTACK_CONQUER_CANCEL = 429
    OPEN_WORLD_ATTACK_CONQUER_STATUS = 430
    OPEN_WORLD_ATTACK_START = 431
    OPEN_WORLD_ATTACK_END = 432
    NEW_RANDOM_RESOURCE_BLOCKER = 433
    NEW_HOME_OBJECT = 434
    HIDEOUT_OBJECT_UPDATE = 435
    UPDATE_INFAMY = 436
    MINIMAP_POSITION_MARKERS = 437
    NEW_TUNNEL_EXIT = 438
    CORRUPTED_DUNGEON_UPDATE = 439
    CORRUPTED_DUNGEON_STATUS = 440
    CORRUPTED_DUNGEON_INFAMY = 441
    HELLGATE_RESTRICTED_AREA_UPDATE = 442
    HELLGATE_INFAMY = 443
    HELLGATE_STATUS = 444
    HELLGATE_STATUS_UPDATE = 445
    HELLGATE_SUSPENSE = 446
    REPLACE_SPELL_SLOT_WITH_MULTI_SPELL = 447
    NEW_CORRUPTED_SHRINE = 448
    UPDATE_CORRUPTED_SHRINE = 449
    CORRUPTED_SHRINE_USAGE_START = 450
    CORRUPTED_SHRINE_USAGE_CANCEL = 451
    EXIT_USED = 452
    LINKED_TO_OBJECT = 453
    LINK_TO_OBJECT_BROKEN = 454
    ESTIMATED_MARKET_VALUE_UPDATE = 455
    STUCK_CANCEL = 456
    DUNGON_ESCAPE_READY = 457
    FACTION_WARFARE_CLUSTER_STATE = 458
    FACTION_WARFARE_HAS_UNCLAIMED_WEEKLY_REPORTS_EVENT = 459
    SIMPLE_FEEDBACK = 460
    SMART_CLUSTER_QUEUE_SKIP_CLUSTER_ERROR = 461
    XIGN_CODE_EVENT = 462
    BATCH_USE_ITEM_START = 463
    BATCH_USE_ITEM_END = 464
    RED_ZONE_EVENT_CLUSTER_STATUS = 465
    RED_ZONE_PLAYER_NOTIFICATION = 466
    RED_ZONE_WORLD_EVENT = 467
    FACTION_WARFARE_STATS = 468
    UPDATE_FACTION_BALANCE_FACTORS = 469
    FACTION_ENLISTMENT_CHANGED = 470
    UPDATE_FACTION_RANK = 471
    FACTION_WARFARE_CAMPAIGN_REWARDS_UNLOCKED = 472
    FEATURED_FEATURE_UPDATE = 473
    NEW_POWER_CRYSTAL_OBJECT = 474
    MINIMAP_CRYSTAL_POSITION_MARKER = 475
    CARRY_POWER_CRYSTAL_UPDATE = 476
    PICKUP_POWER_CRYSTAL_START = 477
    PICKUP_POWER_CRYSTAL_CANCEL = 478
    PICKUP_POWER_CRYSTAL_FINISHED = 479
    DO_SIMPLE_ACTION_START = 480
    DO_SIMPLE_ACTION_CANCEL = 481
    DO_SIMPLE_ACTION_FINISHED = 482
    NOTIFY_GUEST_ACCOUNT_VERIFIED = 483
    MIGHT_AND_FAVOR_RECEIVED_EVENT = 484
    WEEKLY_PVP_CHALLENGE_REWARD_STATE_UPDATE = 485
    NEW_UNLOCKED_PVP_SEASON_CHALLENGE_REWARDS = 486
    STATIC_DUNGEON_ENTRANCES_DUNGEON_EVENT_STATUS_UPDATES = 487
    STATIC_DUNGEON_DUNGEON_VALUE_UPDATE = 488
    STATIC_DUNGEON_ENTRANCE_DUNGEON_EVENTS_ABORTED = 489
    IN_APP_PURCHASE_CONFIRMED_GOOGLE_PLAY = 490
    FEATURE_SWITCH_INFO = 491
    PARTY_JOIN_REQUEST_ABORTED = 492
    PARTY_INVITE_ABORTED = 493
    PARTY_START_HUNT_REQUEST = 494
    PARTY_START_HUNT_REQUESTED = 495
    PARTY_START_HUNT_REQUEST_ANSWER = 496
    GUILD_INVITE_DECLINED = 497
    CANCEL_MULTI_SPELL_SLOTS = 498
    NEW_VISUAL_EVENT_OBJECT = 499
    CASTLE_CLAIM_PROGRESS = 500
    CASTLE_CLAIM_PROGRESS_LOGO = 501
    TOWN_PORTAL_UPDATE_STATE = 502
    TOWN_PORTAL_FAILED = 503
    CONSUMABLE_VANITY_CHARGES_ADDED = 504
    FESTIVITIES_UPDATE = 505
    NEW_BANNER_OBJECT = 506
    NEW_MISTS_IMMEDIATE_RETURN_EXIT = 507
    MISTS_PLAYER_JOINED_INFO = 508
    NEW_MISTS_STATIC_ENTRANCE = 509
    NEW_MISTS_OPEN_WORLD_EXIT = 510
    NEW_TUNNEL_EXIT_TEMP = 511
    NEW_MISTS_WISP_SPAWN = 512
    MISTS_WISP_SPAWN_STATE_CHANGE = 513
    NEW_MISTS_CITY_ENTRANCE = 514
    NEW_MISTS_CITY_ROADS_ENTRANCE = 515
    MISTS_CITY_ROADS_ENTRANCE_PARTY_STATE_UPDATE = 516
    MISTS_CITY_ROADS_ENTRANCE_CLEAR_STATE_FOR_PARTY = 517
    MISTS_ENTRANCE_DATA_CHANGED = 518
    NEW_MISTS_CAGED_WISP = 519
    MISTS_WISP_CAGE_OPENED = 520
    MISTS_ENTRANCE_PARTY_BINDING_CREATED = 521
    MISTS_ENTRANCE_PARTY_BINDING_CLEARED = 522
    MISTS_ENTRANCE_PARTY_BINDING_INFOS = 523
    NEW_MISTS_BORDER_EXIT = 524
    NEW_MISTS_DUNGEON_EXIT = 525
    LOCAL_QUEST_INFOS = 526
    LOCAL_QUEST_STARTED = 527
    LOCAL_QUEST_ACTIVE = 528
    LOCAL_QUEST_INACTIVE = 529
    LOCAL_QUEST_PROGRESS_UPDATE = 530
    NEW_UNRESTRICTED_PVP_ZONE = 531
    TEMPORARY_FLAGGING_STATUS_UPDATE = 532
    SPELL_TEST_PERFORMANCE_UPDATE = 533
    TRANSFORMATION = 534
    TRANSFORMATION_END = 535
    UPDATE_TRUSTLEVEL = 536
    REVEAL_HIDDEN_TIME_STAMPS = 537
    MODIFY_ITEM_TRAIT_FINISHED = 538
    REROLL_ITEM_TRAIT_VALUE_FINISHED = 539
    HUNT_QUEST_PROGRESS_INFO = 540
    HUNT_STARTED = 541
    HUNT_FINISHED = 542
    HUNT_ABORTED = 543
    HUNT_MISSION_STEP_STATE_UPDATE = 544
    NEW_HUNT_TRACK = 545
    HUNT_MISSION_UPDATE = 546
    HUNT_QUEST_MISSION_PROGRESS_UPDATE = 547
    HUNT_TRACK_USED = 548
    HUNT_TRACK_USEABLE_AGAIN = 549
    MINIMAP_HUNT_TRACK_MARKERS = 550
    NO_TRACKS_FOUND = 551
    HUNT_QUEST_ABORTED = 552
    INTERACT_WITH_TRACK_START = 553
    INTERACT_WITH_TRACK_CANCEL = 554
    INTERACT_WITH_TRACK_FINISHED = 555
    NEW_DYNAMIC_COMPOUND = 556
    LEGENDARY_ITEM_DESTROYED = 557
    ATTUNEMENT_INFO = 558
    TERRITORY_CLAIM_RAIDED_RAW_ENERGY_CRYSTAL_RESULT = 559
    CARRIED_OBJECT_EXPIRY_WARNING = 560
    CARRIED_OBJECT_EXPIRED = 561
    TERRITORY_RAID_START = 562
    TERRITORY_RAID_CANCEL = 563
    TERRITORY_RAID_FINISHED = 564
    TERRITORY_RAID_RESULT = 565
    TERRITORY_MONOLITH_ACTIVE_RAID_STATUS = 566
    TERRITORY_MONOLITH_ACTIVE_RAID_CANCELLED = 567
    MONOLITH_ENERGY_STORAGE_UPDATE = 568
    MONOLITH_NEXT_SCHEDULED_OPEN_WORLD_ATTACK_UPDATE = 569
    MONOLITH_PROTECTED_BUILDINGS_DAMAGE_REDUCTION_UPDATE = 570
    NEW_BUILDING_BASE_EVENT = 571
    NEW_FORTIFICATION_BUILDING = 572
    NEW_CASTLE_GATE_BUILDING = 573
    BUILDING_DURABILITY_UPDATE = 574
    MONOLITH_FORTIFICATION_POINTS_UPDATE = 575
    FORTIFICATION_BUILDING_UPGRADE_INFO = 576
    FORTIFICATION_BUILDINGS_DAMAGE_STATE_UPDATE = 577
    SIEGE_NOTIFICATION_EVENT = 578
    UPDATE_ENEMY_WAR_BANNER_ACTIVE = 579
    TERRITORY_ANNOUNCE_PLAYER_EJECTION = 580
    CASTLE_GATE_SWITCH_USE_STARTED = 581
    CASTLE_GATE_SWITCH_USE_FINISHED = 582
    FORTIFICATION_BUILDING_WILL_DOWNGRADE = 583
    BOT_COMMAND = 584
