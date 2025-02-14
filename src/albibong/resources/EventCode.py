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
    REMOVE_SILVER = 63
    ACTION_ON_BUILDING_START = 64
    ACTION_ON_BUILDING_CANCEL = 65
    ACTION_ON_BUILDING_FINISHED = 66
    ITEM_REROLL_QUALITY_FINISHED = 67
    INSTALL_RESOURCE_START = 68
    INSTALL_RESOURCE_CANCEL = 69
    INSTALL_RESOURCE_FINISHED = 70
    CRAFT_ITEM_FINISHED = 71
    LOGOUT_CANCEL = 72
    CHAT_MESSAGE = 73
    CHAT_SAY = 74
    CHAT_WHISPER = 75
    CHAT_MUTED = 76
    PLAY_EMOTE = 77
    STOP_EMOTE = 78
    SYSTEM_MESSAGE = 79
    UTILITY_TEXT_MESSAGE = 80
    UPDATE_MONEY = 81
    UPDATE_FAME = 82
    UPDATE_LEARNING_POINTS = 83
    UPDATE_RE_SPEC_POINTS = 84
    UPDATE_CURRENCY = 85
    UPDATE_FACTION_STANDING = 86
    UPDATE_STANDING = 87
    RESPAWN = 88
    SERVER_DEBUG_LOG = 89
    CHARACTER_EQUIPMENT_CHANGED = 90
    REGENERATION_HEALTH_CHANGED = 91
    REGENERATION_ENERGY_CHANGED = 92
    REGENERATION_MOUNT_HEALTH_CHANGED = 93
    REGENERATION_CRAFTING_CHANGED = 94
    REGENERATION_HEALTH_ENERGY_COMBO_CHANGED = 95
    REGENERATION_PLAYER_COMBO_CHANGED = 96
    DURABILITY_CHANGED = 97
    NEW_LOOT = 98
    ATTACH_ITEM_CONTAINER = 99
    DETACH_ITEM_CONTAINER = 100
    INVALIDATE_ITEM_CONTAINER = 101
    LOCK_ITEM_CONTAINER = 102
    GUILD_UPDATE = 103
    GUILD_PLAYER_UPDATED = 104
    INVITED_TO_GUILD = 105
    GUILD_MEMBER_WORLD_UPDATE = 106
    UPDATE_MATCH_DETAILS = 107
    OBJECT_EVENT = 108
    NEW_MONOLITH_OBJECT = 109
    MONOLITH_HAS_BANNERS_PLACED_UPDATE = 110
    NEW_ORB_OBJECT = 111
    NEW_CASTLE_OBJECT = 112
    NEW_SPELL_EFFECT_AREA = 113
    UPDATE_SPELL_EFFECT_AREA = 114
    NEW_CHAIN_SPELL = 115
    UPDATE_CHAIN_SPELL = 116
    NEW_TREASURE_CHEST = 117
    START_MATCH = 118
    START_ARENA_MATCH_INFOS = 119
    END_ARENA_MATCH = 120
    MATCH_UPDATE = 121
    ACTIVE_MATCH_UPDATE = 122
    NEW_MOB = 123
    DEBUG_MOB_INFO = 124
    DEBUG_VARIABLES_INFO = 125
    DEBUG_REPUTATION_INFO = 126
    DEBUG_DIMINISHING_RETURN_INFO = 127
    DEBUG_SMART_CLUSTER_QUEUE_INFO = 128
    CLAIM_ORB_START = 129
    CLAIM_ORB_FINISHED = 130
    CLAIM_ORB_CANCEL = 131
    ORB_UPDATE = 132
    ORB_CLAIMED = 133
    ORB_RESET = 134
    NEW_WAR_CAMP_OBJECT = 135
    NEW_MATCH_LOOT_CHEST_OBJECT = 136
    NEW_ARENA_EXIT = 137
    GUILD_MEMBER_TERRITORY_UPDATE = 138
    INVITED_MERCENARY_TO_MATCH = 139
    CLUSTER_INFO_UPDATE = 140
    FORCED_MOVEMENT = 141
    FORCED_MOVEMENT_CANCEL = 142
    CHARACTER_STATS = 143
    CHARACTER_STATS_KILL_HISTORY = 144
    CHARACTER_STATS_DEATH_HISTORY = 145
    CHARACTER_STATS_KNOCK_DOWN_HISTORY = 146
    CHARACTER_STATS_KNOCKED_DOWN_HISTORY = 147
    GUILD_STATS = 148
    KILL_HISTORY_DETAILS = 149
    ITEM_KILL_HISTORY_DETAILS = 150
    FULL_ACHIEVEMENT_INFO = 151
    FINISHED_ACHIEVEMENT = 152
    ACHIEVEMENT_PROGRESS_INFO = 153
    FULL_ACHIEVEMENT_PROGRESS_INFO = 154
    FULL_TRACKED_ACHIEVEMENT_INFO = 155
    FULL_AUTO_LEARN_ACHIEVEMENT_INFO = 156
    QUEST_GIVER_QUEST_OFFERED = 157
    QUEST_GIVER_DEBUG_INFO = 158
    CONSOLE_EVENT = 159
    TIME_SYNC = 160
    CHANGE_AVATAR = 161
    CHANGE_MOUNT_SKIN = 162
    GAME_EVENT = 163
    KILLED_PLAYER = 164
    DIED = 165
    KNOCKED_DOWN = 166
    UNCONCIOUS = 167
    MATCH_PLAYER_JOINED_EVENT = 168
    MATCH_PLAYER_STATS_EVENT = 169
    MATCH_PLAYER_STATS_COMPLETE_EVENT = 170
    MATCH_TIME_LINE_EVENT_EVENT = 171
    MATCH_PLAYER_MAIN_GEAR_STATS_EVENT = 172
    MATCH_PLAYER_CHANGED_AVATAR_EVENT = 173
    INVITATION_PLAYER_TRADE = 174
    PLAYER_TRADE_START = 175
    PLAYER_TRADE_CANCEL = 176
    PLAYER_TRADE_UPDATE = 177
    PLAYER_TRADE_FINISHED = 178
    PLAYER_TRADE_ACCEPT_CHANGE = 179
    MINI_MAP_PING = 180
    MARKET_PLACE_NOTIFICATION = 181
    DUELLING_CHALLENGE_PLAYER = 182
    NEW_DUELLING_POST = 183
    DUEL_STARTED = 184
    DUEL_ENDED = 185
    DUEL_DENIED = 186
    DUEL_REQUEST_CANCELED = 187
    DUEL_LEFT_AREA = 188
    DUEL_RE_ENTERED_AREA = 189
    NEW_REAL_ESTATE = 190
    MINI_MAP_OWNED_BUILDINGS_POSITIONS = 191
    REAL_ESTATE_LIST_UPDATE = 192
    GUILD_LOGO_UPDATE = 193
    GUILD_LOGO_CHANGED = 194
    PLACEABLE_OBJECT_PLACE = 195
    PLACEABLE_OBJECT_PLACE_CANCEL = 196
    FURNITURE_OBJECT_BUFF_PROVIDER_INFO = 197
    FURNITURE_OBJECT_CHEAT_PROVIDER_INFO = 198
    FARMABLE_OBJECT_INFO = 199
    NEW_UNREAD_MAILS = 200
    MAIL_OPERATION_POSSIBLE = 201
    GUILD_LOGO_OBJECT_UPDATE = 202
    START_LOGOUT = 203
    NEW_CHAT_CHANNELS = 204
    JOINED_CHAT_CHANNEL = 205
    LEFT_CHAT_CHANNEL = 206
    REMOVED_CHAT_CHANNEL = 207
    ACCESS_STATUS = 208
    MOUNTED = 209
    MOUNT_START = 210
    MOUNT_CANCEL = 211
    NEW_TRAVELPOINT = 212
    NEW_ISLAND_ACCESS_POINT = 213
    NEW_EXIT = 214
    UPDATE_HOME = 215
    UPDATE_CHAT_SETTINGS = 216
    RESURRECTION_OFFER = 217
    RESURRECTION_REPLY = 218
    LOOT_EQUIPMENT_CHANGED = 219
    UPDATE_UNLOCKED_GUILD_LOGOS = 220
    UPDATE_UNLOCKED_AVATARS = 221
    UPDATE_UNLOCKED_AVATAR_RINGS = 222
    UPDATE_UNLOCKED_BUILDINGS = 223
    NEW_ISLAND_MANAGEMENT = 224
    NEW_TELEPORT_STONE = 225
    CLOAK = 226
    PARTY_INVITATION = 227
    PARTY_JOIN_REQUEST = 228
    PARTY_JOINED = 229
    PARTY_DISBANDED = 230
    PARTY_PLAYER_JOINED = 231
    PARTY_CHANGED_ORDER = 232
    PARTY_PLAYER_LEFT = 233
    PARTY_LEADER_CHANGED = 234
    PARTY_LOOT_SETTING_CHANGED_PLAYER = 235
    PARTY_SILVER_GAINED = 236
    PARTY_PLAYER_UPDATED = 237
    PARTY_INVITATION_ANSWER = 238
    PARTY_JOIN_REQUEST_ANSWER = 239
    PARTY_MARKED_OBJECTS_UPDATED = 240
    PARTY_ON_CLUSTER_PARTY_JOINED = 241
    PARTY_SET_ROLE_FLAG = 242
    PARTY_INVITE_OR_JOIN_PLAYER_EQUIPMENT_INFO = 243
    PARTY_READY_CHECK_UPDATE = 244
    SPELL_COOLDOWN_UPDATE = 245
    NEW_HELLGATE_EXIT_PORTAL = 246
    NEW_EXPEDITION_EXIT = 247
    NEW_EXPEDITION_NARRATOR = 248
    EXIT_ENTER_START = 249
    EXIT_ENTER_CANCEL = 250
    EXIT_ENTER_FINISHED = 251
    NEW_QUEST_GIVER_OBJECT = 252
    FULL_QUEST_INFO = 253
    QUEST_PROGRESS_INFO = 254
    QUEST_GIVER_INFO_FOR_PLAYER = 255
    FULL_EXPEDITION_INFO = 256
    EXPEDITION_QUEST_PROGRESS_INFO = 257
    INVITED_TO_EXPEDITION = 258
    EXPEDITION_REGISTRATION_INFO = 259
    ENTERING_EXPEDITION_START = 260
    ENTERING_EXPEDITION_CANCEL = 261
    REWARD_GRANTED = 262
    ARENA_REGISTRATION_INFO = 263
    ENTERING_ARENA_START = 264
    ENTERING_ARENA_CANCEL = 265
    ENTERING_ARENA_LOCK_START = 266
    ENTERING_ARENA_LOCK_CANCEL = 267
    INVITED_TO_ARENA_MATCH = 268
    USING_HELLGATE_SHRINE = 269
    ENTERING_HELLGATE_LOCK_START = 270
    ENTERING_HELLGATE_LOCK_CANCEL = 271
    PLAYER_COUNTS = 272
    IN_COMBAT_STATE_UPDATE = 273
    OTHER_GRABBED_LOOT = 274
    TREASURE_CHEST_USING_START = 275
    TREASURE_CHEST_USING_FINISHED = 276
    TREASURE_CHEST_USING_CANCEL = 277
    TREASURE_CHEST_USING_OPENING_COMPLETE = 278
    TREASURE_CHEST_FORCE_CLOSE_INVENTORY = 279
    LOCAL_TREASURES_UPDATE = 280
    LOOT_CHEST_SPAWNPOINTS_UPDATE = 281
    PREMIUM_CHANGED = 282
    PREMIUM_EXTENDED = 283
    PREMIUM_LIFE_TIME_REWARD_GAINED = 284
    GOLD_PURCHASED = 285
    LABORER_GOT_UPGRADED = 286
    JOURNAL_GOT_FULL = 287
    JOURNAL_FILL_ERROR = 288
    FRIEND_REQUEST = 289
    FRIEND_REQUEST_INFOS = 290
    FRIEND_INFOS = 291
    FRIEND_REQUEST_ANSWERED = 292
    FRIEND_ONLINE_STATUS = 293
    FRIEND_REQUEST_CANCELED = 294
    FRIEND_REMOVED = 295
    FRIEND_UPDATED = 296
    PARTY_LOOT_ITEMS = 297
    PARTY_LOOT_ITEMS_REMOVED = 298
    REPUTATION_UPDATE = 299
    DEFENSE_UNIT_ATTACK_BEGIN = 300
    DEFENSE_UNIT_ATTACK_END = 301
    DEFENSE_UNIT_ATTACK_DAMAGE = 302
    UNRESTRICTED_PVP_ZONE_UPDATE = 303
    UNRESTRICTED_PVP_ZONE_STATUS = 304
    REPUTATION_IMPLICATION_UPDATE = 305
    NEW_MOUNT_OBJECT = 306
    MOUNT_HEALTH_UPDATE = 307
    MOUNT_COOLDOWN_UPDATE = 308
    NEW_EXPEDITION_AGENT = 309
    NEW_EXPEDITION_CHECK_POINT = 310
    EXPEDITION_START_EVENT = 311
    VOTE_EVENT = 312
    RATING_EVENT = 313
    NEW_ARENA_AGENT = 314
    BOOST_FARMABLE = 315
    USE_FUNCTION = 316
    NEW_PORTAL_ENTRANCE = 317
    NEW_PORTAL_EXIT = 318
    NEW_RANDOM_DUNGEON_EXIT = 319
    WAITING_QUEUE_UPDATE = 320
    PLAYER_MOVEMENT_RATE_UPDATE = 321
    OBSERVE_START = 322
    MINIMAP_ZERGS = 323
    MINIMAP_SMART_CLUSTER_ZERGS = 324
    PAYMENT_TRANSACTIONS = 325
    PERFORMANCE_STATS_UPDATE = 326
    OVERLOAD_MODE_UPDATE = 327
    DEBUG_DRAW_EVENT = 328
    RECORD_CAMERA_MOVE = 329
    RECORD_START = 330
    DELIVER_CARRIABLE_OBJECT_START = 331
    DELIVER_CARRIABLE_OBJECT_CANCEL = 332
    DELIVER_CARRIABLE_OBJECT_RESET = 333
    DELIVER_CARRIABLE_OBJECT_FINISHED = 334
    TERRITORY_CLAIM_START = 335
    TERRITORY_CLAIM_CANCEL = 336
    TERRITORY_CLAIM_FINISHED = 337
    TERRITORY_SCHEDULE_RESULT = 338
    TERRITORY_UPGRADE_WITH_POWER_CRYSTAL_RESULT = 339
    RECEIVE_CARRIABLE_OBJECT_START = 340
    RECEIVE_CARRIABLE_OBJECT_FINISHED = 341
    UPDATE_ACCOUNT_STATE = 342
    START_DETERMINISTIC_ROAM = 343
    GUILD_FULL_ACCESS_TAGS_UPDATED = 344
    GUILD_ACCESS_TAG_UPDATED = 345
    GVG_SEASON_UPDATE = 346
    GVG_SEASON_CHEAT_COMMAND = 347
    SEASON_POINTS_BY_KILLING_BOOSTER = 348
    FISHING_START = 349
    FISHING_CAST = 350
    FISHING_CATCH = 351
    FISHING_FINISHED = 352
    FISHING_CANCEL = 353
    NEW_FLOAT_OBJECT = 354
    NEW_FISHING_ZONE_OBJECT = 355
    FISHING_MINI_GAME = 356
    ALBION_JOURNAL_ACHIEVEMENT_COMPLETED = 357
    UPDATE_PUPPET = 358
    CHANGE_FLAGGING_FINISHED = 359
    NEW_OUTPOST_OBJECT = 360
    OUTPOST_UPDATE = 361
    OUTPOST_CLAIMED = 362
    OVER_CHARGE_END = 363
    OVER_CHARGE_STATUS = 364
    PARTY_FINDER_FULL_UPDATE = 365
    PARTY_FINDER_UPDATE = 366
    PARTY_FINDER_APPLICANTS_UPDATE = 367
    PARTY_FINDER_EQUIPMENT_SNAPSHOT = 368
    PARTY_FINDER_JOIN_REQUEST_DECLINED = 369
    NEW_UNLOCKED_PERSONAL_SEASON_REWARDS = 370
    PERSONAL_SEASON_POINTS_GAINED = 371
    PERSONAL_SEASON_PAST_SEASON_DATA_EVENT = 372
    EASY_ANTI_CHEAT_MESSAGE_TO_CLIENT = 373
    MATCH_LOOT_CHEST_OPENING_START = 374
    MATCH_LOOT_CHEST_OPENING_FINISHED = 375
    MATCH_LOOT_CHEST_OPENING_CANCEL = 376
    NOTIFY_CRYSTAL_MATCH_REWARD = 377
    CRYSTAL_REALM_FEEDBACK = 378
    NEW_LOCATION_MARKER = 379
    NEW_TUTORIAL_BLOCKER = 380
    NEW_TILE_SWITCH = 381
    NEW_INFORMATION_PROVIDER = 382
    NEW_DYNAMIC_GUILD_LOGO = 383
    NEW_DECORATION = 384
    TUTORIAL_UPDATE = 385
    TRIGGER_HINT_BOX = 386
    RANDOM_DUNGEON_POSITION_INFO = 387
    NEW_LOOT_CHEST = 388
    UPDATE_LOOT_CHEST = 389
    LOOT_CHEST_OPENED = 390
    UPDATE_LOOT_PROTECTED_BY_MOBS_WITH_MINIMAP_DISPLAY = 391
    NEW_SHRINE = 392
    UPDATE_SHRINE = 393
    UPDATE_ROOM = 394
    NEW_MIST_DUNGEON_ROOM_MOB_SOUL = 395
    NEW_HELLGATE_SHRINE = 396
    UPDATE_HELLGATE_SHRINE = 397
    ACTIVATE_HELLGATE_EXIT = 398
    MUTE_PLAYER_UPDATE = 399
    SHOP_TILE_UPDATE = 400
    SHOP_UPDATE = 401
    ANTI_CHEAT_KICK = 402
    BATTL_EYE_SERVER_MESSAGE = 403
    UNLOCK_VANITY_UNLOCK = 404
    AVATAR_UNLOCKED = 405
    CUSTOMIZATION_CHANGED = 406
    BASE_VAULT_INFO = 407
    GUILD_VAULT_INFO = 408
    BANK_VAULT_INFO = 409
    RECOVERY_VAULT_PLAYER_INFO = 410
    RECOVERY_VAULT_GUILD_INFO = 411
    UPDATE_WARDROBE = 412
    CASTLE_PHASE_CHANGED = 413
    GUILD_ACCOUNT_LOG_EVENT = 414
    NEW_HIDEOUT_OBJECT = 415
    NEW_HIDEOUT_MANAGEMENT = 416
    NEW_HIDEOUT_EXIT = 417
    INIT_HIDEOUT_ATTACK_START = 418
    INIT_HIDEOUT_ATTACK_CANCEL = 419
    INIT_HIDEOUT_ATTACK_FINISHED = 420
    HIDEOUT_MANAGEMENT_UPDATE = 421
    HIDEOUT_UPGRADE_WITH_POWER_CRYSTAL_RESULT = 422
    IP_CHANGED = 423
    SMART_CLUSTER_QUEUE_UPDATE_INFO = 424
    SMART_CLUSTER_QUEUE_ACTIVE_INFO = 425
    SMART_CLUSTER_QUEUE_KICK_WARNING = 426
    SMART_CLUSTER_QUEUE_INVITE = 427
    RECEIVED_GVG_SEASON_POINTS = 428
    TOWER_POWER_POINT_UPDATE = 429
    OPEN_WORLD_ATTACK_SCHEDULE_START = 430
    OPEN_WORLD_ATTACK_SCHEDULE_FINISHED = 431
    OPEN_WORLD_ATTACK_SCHEDULE_CANCEL = 432
    OPEN_WORLD_ATTACK_CONQUER_START = 433
    OPEN_WORLD_ATTACK_CONQUER_FINISHED = 434
    OPEN_WORLD_ATTACK_CONQUER_CANCEL = 435
    OPEN_WORLD_ATTACK_CONQUER_STATUS = 436
    OPEN_WORLD_ATTACK_START = 437
    OPEN_WORLD_ATTACK_END = 438
    NEW_RANDOM_RESOURCE_BLOCKER = 439
    NEW_HOME_OBJECT = 440
    HIDEOUT_OBJECT_UPDATE = 441
    UPDATE_INFAMY = 442
    MINIMAP_POSITION_MARKERS = 443
    NEW_TUNNEL_EXIT = 444
    CORRUPTED_DUNGEON_UPDATE = 445
    CORRUPTED_DUNGEON_STATUS = 446
    CORRUPTED_DUNGEON_INFAMY = 447
    HELLGATE_RESTRICTED_AREA_UPDATE = 448
    HELLGATE_INFAMY = 449
    HELLGATE_STATUS = 450
    HELLGATE_STATUS_UPDATE = 451
    HELLGATE_SUSPENSE = 452
    REPLACE_SPELL_SLOT_WITH_MULTI_SPELL = 453
    NEW_CORRUPTED_SHRINE = 454
    UPDATE_CORRUPTED_SHRINE = 455
    CORRUPTED_SHRINE_USAGE_START = 456
    CORRUPTED_SHRINE_USAGE_CANCEL = 457
    EXIT_USED = 458
    LINKED_TO_OBJECT = 459
    LINK_TO_OBJECT_BROKEN = 460
    ESTIMATED_MARKET_VALUE_UPDATE = 461
    STUCK_CANCEL = 462
    DUNGON_ESCAPE_READY = 463
    FACTION_WARFARE_CLUSTER_STATE = 464
    FACTION_WARFARE_HAS_UNCLAIMED_WEEKLY_REPORTS_EVENT = 465
    SIMPLE_FEEDBACK = 466
    SMART_CLUSTER_QUEUE_SKIP_CLUSTER_ERROR = 467
    XIGN_CODE_EVENT = 468
    BATCH_USE_ITEM_START = 469
    BATCH_USE_ITEM_END = 470
    RED_ZONE_EVENT_CLUSTER_STATUS = 471
    RED_ZONE_PLAYER_NOTIFICATION = 472
    RED_ZONE_WORLD_EVENT = 473
    FACTION_WARFARE_STATS = 474
    UPDATE_FACTION_BALANCE_FACTORS = 475
    FACTION_ENLISTMENT_CHANGED = 476
    UPDATE_FACTION_RANK = 477
    FACTION_WARFARE_CAMPAIGN_REWARDS_UNLOCKED = 478
    FEATURED_FEATURE_UPDATE = 479
    NEW_CARRIABLE_OBJECT = 480
    MINIMAP_CRYSTAL_POSITION_MARKER = 481
    CARRIED_OBJECT_UPDATE = 482
    PICKUP_CARRIABLE_OBJECT_START = 483
    PICKUP_CARRIABLE_OBJECT_CANCEL = 484
    PICKUP_CARRIABLE_OBJECT_FINISHED = 485
    DO_SIMPLE_ACTION_START = 486
    DO_SIMPLE_ACTION_CANCEL = 487
    DO_SIMPLE_ACTION_FINISHED = 488
    NOTIFY_GUEST_ACCOUNT_VERIFIED = 489
    MIGHT_AND_FAVOR_RECEIVED_EVENT = 490
    WEEKLY_PVP_CHALLENGE_REWARD_STATE_UPDATE = 491
    NEW_UNLOCKED_PVP_SEASON_CHALLENGE_REWARDS = 492
    STATIC_DUNGEON_ENTRANCES_DUNGEON_EVENT_STATUS_UPDATES = 493
    STATIC_DUNGEON_DUNGEON_VALUE_UPDATE = 494
    STATIC_DUNGEON_ENTRANCE_DUNGEON_EVENTS_ABORTED = 495
    IN_APP_PURCHASE_CONFIRMED_GOOGLE_PLAY = 496
    FEATURE_SWITCH_INFO = 497
    PARTY_JOIN_REQUEST_ABORTED = 498
    PARTY_INVITE_ABORTED = 499
    PARTY_START_HUNT_REQUEST = 500
    PARTY_START_HUNT_REQUESTED = 501
    PARTY_START_HUNT_REQUEST_ANSWER = 502
    PARTY_PLAYER_LEAVE_SCHEDULED = 503
    GUILD_INVITE_DECLINED = 504
    CANCEL_MULTI_SPELL_SLOTS = 505
    NEW_VISUAL_EVENT_OBJECT = 506
    CASTLE_CLAIM_PROGRESS = 507
    CASTLE_CLAIM_PROGRESS_LOGO = 508
    TOWN_PORTAL_UPDATE_STATE = 509
    TOWN_PORTAL_FAILED = 510
    CONSUMABLE_VANITY_CHARGES_ADDED = 511
    FESTIVITIES_UPDATE = 512
    NEW_BANNER_OBJECT = 513
    NEW_MISTS_IMMEDIATE_RETURN_EXIT = 514
    MISTS_PLAYER_JOINED_INFO = 515
    NEW_MISTS_STATIC_ENTRANCE = 516
    NEW_MISTS_OPEN_WORLD_EXIT = 517
    NEW_TUNNEL_EXIT_TEMP = 518
    NEW_MISTS_WISP_SPAWN = 519
    MISTS_WISP_SPAWN_STATE_CHANGE = 520
    NEW_MISTS_CITY_ENTRANCE = 521
    NEW_MISTS_CITY_ROADS_ENTRANCE = 522
    MISTS_CITY_ROADS_ENTRANCE_PARTY_STATE_UPDATE = 523
    MISTS_CITY_ROADS_ENTRANCE_CLEAR_STATE_FOR_PARTY = 524
    MISTS_ENTRANCE_DATA_CHANGED = 525
    NEW_CAGED_OBJECT = 526
    CAGED_OBJECT_STATE_UPDATED = 527
    MISTS_ENTRANCE_PARTY_BINDING_CREATED = 528
    MISTS_ENTRANCE_PARTY_BINDING_CLEARED = 529
    MISTS_ENTRANCE_PARTY_BINDING_INFOS = 530
    NEW_MISTS_BORDER_EXIT = 531
    NEW_MISTS_DUNGEON_EXIT = 532
    LOCAL_QUEST_INFOS = 533
    LOCAL_QUEST_STARTED = 534
    LOCAL_QUEST_ACTIVE = 535
    LOCAL_QUEST_INACTIVE = 536
    LOCAL_QUEST_PROGRESS_UPDATE = 537
    NEW_UNRESTRICTED_PVP_ZONE = 538
    TEMPORARY_FLAGGING_STATUS_UPDATE = 539
    SPELL_TEST_PERFORMANCE_UPDATE = 540
    TRANSFORMATION = 541
    TRANSFORMATION_END = 542
    UPDATE_TRUSTLEVEL = 543
    REVEAL_HIDDEN_TIME_STAMPS = 544
    MODIFY_ITEM_TRAIT_FINISHED = 545
    REROLL_ITEM_TRAIT_VALUE_FINISHED = 546
    HUNT_QUEST_PROGRESS_INFO = 547
    HUNT_STARTED = 548
    HUNT_FINISHED = 549
    HUNT_ABORTED = 550
    HUNT_MISSION_STEP_STATE_UPDATE = 551
    NEW_HUNT_TRACK = 552
    HUNT_MISSION_UPDATE = 553
    HUNT_QUEST_MISSION_PROGRESS_UPDATE = 554
    HUNT_TRACK_USED = 555
    HUNT_TRACK_USEABLE_AGAIN = 556
    MINIMAP_HUNT_TRACK_MARKERS = 557
    NO_TRACKS_FOUND = 558
    HUNT_QUEST_ABORTED = 559
    INTERACT_WITH_TRACK_START = 560
    INTERACT_WITH_TRACK_CANCEL = 561
    INTERACT_WITH_TRACK_FINISHED = 562
    NEW_DYNAMIC_COMPOUND = 563
    LEGENDARY_ITEM_DESTROYED = 564
    ATTUNEMENT_INFO = 565
    TERRITORY_CLAIM_RAIDED_RAW_ENERGY_CRYSTAL_RESULT = 566
    CARRIED_OBJECT_EXPIRY_WARNING = 567
    CARRIED_OBJECT_EXPIRED = 568
    TERRITORY_RAID_START = 569
    TERRITORY_RAID_CANCEL = 570
    TERRITORY_RAID_FINISHED = 571
    TERRITORY_RAID_RESULT = 572
    TERRITORY_MONOLITH_ACTIVE_RAID_STATUS = 573
    TERRITORY_MONOLITH_ACTIVE_RAID_CANCELLED = 574
    MONOLITH_ENERGY_STORAGE_UPDATE = 575
    MONOLITH_NEXT_SCHEDULED_OPEN_WORLD_ATTACK_UPDATE = 576
    MONOLITH_PROTECTED_BUILDINGS_DAMAGE_REDUCTION_UPDATE = 577
    NEW_BUILDING_BASE_EVENT = 578
    NEW_FORTIFICATION_BUILDING = 579
    NEW_CASTLE_GATE_BUILDING = 580
    BUILDING_DURABILITY_UPDATE = 581
    MONOLITH_FORTIFICATION_POINTS_UPDATE = 582
    FORTIFICATION_BUILDING_UPGRADE_INFO = 583
    FORTIFICATION_BUILDINGS_DAMAGE_STATE_UPDATE = 584
    SIEGE_NOTIFICATION_EVENT = 585
    UPDATE_ENEMY_WAR_BANNER_ACTIVE = 586
    TERRITORY_ANNOUNCE_PLAYER_EJECTION = 587
    CASTLE_GATE_SWITCH_USE_STARTED = 588
    CASTLE_GATE_SWITCH_USE_FINISHED = 589
    FORTIFICATION_BUILDING_WILL_DOWNGRADE = 590
    BOT_COMMAND = 591
    JOURNAL_ACHIEVEMENT_PROGRESS_UPDATE = 592
    JOURNAL_CLAIMABLE_REWARD_UPDATE = 593
    KEY_SYNC = 594
    LOCAL_QUEST_AREA_GONE = 595
    DYNAMIC_TEMPLATE = 596
    DYNAMIC_TEMPLATE_FORCED_STATE_CHANGE = 597
    NEW_OUTLANDS_TELEPORTATION_PORTAL = 598
    NEW_OUTLANDS_TELEPORTATION_RETURN_PORTAL = 599
    OUTLANDS_TELEPORTATION_BINDING_CLEARED = 600
    OUTLANDS_TELEPORTATION_RETURN_PORTAL_UPDATE_EVENT = 601
    PLAYER_USED_OUTLANDS_TELEPORTATION_PORTAL = 602
    ENCUMBERED_RESTRICTED = 603
    NEW_PILED_OBJECT = 604
    PILED_OBJECT_STATE_CHANGED = 605
    NEW_SMUGGLER_CRATE_DELIVERY_STATION = 606
    KILL_REWARDED_NO_FAME = 607
    PICKUP_FROM_PILED_OBJECT_START = 608
    PICKUP_FROM_PILED_OBJECT_CANCEL = 609
    PICKUP_FROM_PILED_OBJECT_RESET = 610
    PICKUP_FROM_PILED_OBJECT_FINISHED = 611
    ARMORY_ACTIVITY_CHANGE = 612
    NEW_KILL_TROPHY_FURNITURE_BUILDING = 61
