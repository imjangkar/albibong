from enum import Enum


class OperationCode(Enum):
    UNUSED = 0
    PING = 1
    JOIN = 2
    VERSIONED_OPERATION = 3
    CREATE_ACCOUNT = 4
    LOGIN = 5
    CREATE_GUEST_ACCOUNT = 6
    SEND_CRASH_LOG = 7
    SEND_TRACE_ROUTE = 8
    SEND_VFX_STATS = 9
    SEND_GAME_PING_INFO = 10
    CREATE_CHARACTER = 11
    DELETE_CHARACTER = 12
    SELECT_CHARACTER = 13
    ACCEPT_POPUPS = 14
    REDEEM_KEYCODE = 15
    GET_GAME_SERVER_BY_CLUSTER = 16
    GET_SHOP_PURCHASE_URL = 17
    GET_REFERRAL_SEASON_DETAILS = 18
    GET_REFERRAL_LINK = 19
    GET_SHOP_TILES_FOR_CATEGORY = 20
    MOVE = 21
    ATTACK_START = 22
    CAST_START = 23
    CAST_CANCEL = 24
    TERMINATE_TOGGLE_SPELL = 25
    CHANNELING_CANCEL = 26
    ATTACK_BUILDING_START = 27
    INVENTORY_DESTROY_ITEM = 28
    INVENTORY_MOVE_ITEM = 29
    INVENTORY_RECOVER_ITEM = 30
    INVENTORY_RECOVER_ALL_ITEMS = 31
    INVENTORY_SPLIT_STACK = 32
    INVENTORY_SPLIT_STACK_INTO = 33
    GET_CLUSTER_DATA = 34
    CHANGE_CLUSTER = 35
    CONSOLE_COMMAND = 36
    CHAT_MESSAGE = 37
    REPORT_CLIENT_ERROR = 38
    REGISTER_TO_OBJECT = 39
    UN_REGISTER_FROM_OBJECT = 40
    CRAFT_BUILDING_CHANGE_SETTINGS = 41
    CRAFT_BUILDING_TAKE_MONEY = 42
    REPAIR_BUILDING_CHANGE_SETTINGS = 43
    REPAIR_BUILDING_TAKE_MONEY = 44
    ACTION_BUILDING_CHANGE_SETTINGS = 45
    HARVEST_START = 46
    HARVEST_CANCEL = 47
    TAKE_SILVER = 48
    ACTION_ON_BUILDING_START = 49
    ACTION_ON_BUILDING_CANCEL = 50
    INSTALL_RESOURCE_START = 51
    INSTALL_RESOURCE_CANCEL = 52
    INSTALL_SILVER = 53
    BUILDING_FILL_NUTRITION = 54
    BUILDING_CHANGE_RENOVATION_STATE = 55
    BUILDING_BUY_SKIN = 56
    BUILDING_CLAIM = 57
    BUILDING_GIVEUP = 58
    BUILDING_NUTRITION_SILVER_STORAGE_DEPOSIT = 59
    BUILDING_NUTRITION_SILVER_STORAGE_WITHDRAW = 60
    BUILDING_NUTRITION_SILVER_REWARD_SET = 61
    CONSTRUCTION_SITE_CREATE = 62
    PLACEABLE_OBJECT_PLACE = 63
    PLACEABLE_OBJECT_PLACE_CANCEL = 64
    PLACEABLE_OBJECT_PICKUP = 65
    FURNITURE_OBJECT_USE = 66
    FARMABLE_HARVEST = 67
    FARMABLE_FINISH_GROWN_ITEM = 68
    FARMABLE_DESTROY = 69
    FARMABLE_GET_PRODUCT = 70
    FARMABLE_FILL = 71
    TEAR_DOWN_CONSTRUCTION_SITE = 72
    AUCTION_CREATE_OFFER = 73
    AUCTION_CREATE_REQUEST = 74
    AUCTION_GET_OFFERS = 75
    AUCTION_GET_REQUESTS = 76
    AUCTION_BUY_OFFER = 77
    AUCTION_ABORT_AUCTION = 78
    AUCTION_MODIFY_AUCTION = 79
    AUCTION_ABORT_OFFER = 80
    AUCTION_ABORT_REQUEST = 81
    AUCTION_SELL_REQUEST = 82
    AUCTION_GET_FINISHED_AUCTIONS = 83
    AUCTION_GET_FINISHED_AUCTIONS_COUNT = 84
    AUCTION_FETCH_AUCTION = 85
    AUCTION_GET_MY_OPEN_OFFERS = 86
    AUCTION_GET_MY_OPEN_REQUESTS = 87
    AUCTION_GET_MY_OPEN_AUCTIONS = 88
    AUCTION_GET_ITEM_AVERAGE_STATS = 89
    AUCTION_GET_ITEM_AVERAGE_VALUE = 90
    CONTAINER_OPEN = 91
    CONTAINER_CLOSE = 92
    CONTAINER_MANAGE_SUB_CONTAINER = 93
    RESPAWN = 94
    SUICIDE = 95
    JOIN_GUILD = 96
    LEAVE_GUILD = 97
    CREATE_GUILD = 98
    INVITE_TO_GUILD = 99
    DECLINE_GUILD_INVITATION = 100
    KICK_FROM_GUILD = 101
    INSTANT_JOIN_GUILD = 102
    DUELLING_CHALLENGE_PLAYER = 103
    DUELLING_ACCEPT_CHALLENGE = 104
    DUELLING_DENY_CHALLENGE = 105
    CHANGE_CLUSTER_TAX = 106
    CLAIM_TERRITORY = 107
    GIVE_UP_TERRITORY = 108
    CHANGE_TERRITORY_ACCESS_RIGHTS = 109
    GET_MONOLITH_INFO = 110
    GET_CLAIM_INFO = 111
    GET_ATTACK_INFO = 112
    GET_TERRITORY_SEASON_POINTS = 113
    GET_ATTACK_SCHEDULE = 114
    GET_MATCHES = 115
    GET_MATCH_DETAILS = 116
    JOIN_MATCH = 117
    LEAVE_MATCH = 118
    GET_CLUSTER_INSTANCE_INFO_FOR_STATIC_CLUSTER = 119
    CHANGE_CHAT_SETTINGS = 120
    LOGOUT_START = 121
    LOGOUT_CANCEL = 122
    CLAIM_ORB_START = 123
    CLAIM_ORB_CANCEL = 124
    MATCH_LOOT_CHEST_OPENING_START = 125
    MATCH_LOOT_CHEST_OPENING_CANCEL = 126
    DEPOSIT_TO_GUILD_ACCOUNT = 127
    WITHDRAWAL_FROM_ACCOUNT = 128
    CHANGE_GUILD_PAY_UPKEEP_FLAG = 129
    CHANGE_GUILD_TAX = 130
    GET_MY_TERRITORIES = 131
    MORGANA_COMMAND = 132
    GET_SERVER_INFO = 133
    SUBSCRIBE_TO_CLUSTER = 134
    ANSWER_MERCENARY_INVITATION = 135
    GET_CHARACTER_EQUIPMENT = 136
    GET_CHARACTER_STEAM_ACHIEVEMENTS = 137
    GET_CHARACTER_STATS = 138
    GET_KILL_HISTORY_DETAILS = 139
    LEARN_MASTERY_LEVEL = 140
    RE_SPEC_ACHIEVEMENT = 141
    CHANGE_AVATAR = 142
    GET_RANKINGS = 143
    GET_RANK = 144
    GET_GVG_SEASON_RANKINGS = 145
    GET_GVG_SEASON_RANK = 146
    GET_GVG_SEASON_HISTORY_RANKINGS = 147
    GET_GVG_SEASON_GUILD_MEMBER_HISTORY = 148
    KICK_FROM_GV_G_MATCH = 149
    GET_CRYSTAL_LEAGUE_DAILY_SEASON_POINTS = 150
    GET_CHEST_LOGS = 151
    GET_ACCESS_RIGHT_LOGS = 152
    GET_GUILD_ACCOUNT_LOGS = 153
    GET_GUILD_ACCOUNT_LOGS_LARGE_AMOUNT = 154
    INVITE_TO_PLAYER_TRADE = 155
    PLAYER_TRADE_CANCEL = 156
    PLAYER_TRADE_INVITATION_ACCEPT = 157
    PLAYER_TRADE_ADD_ITEM = 158
    PLAYER_TRADE_REMOVE_ITEM = 159
    PLAYER_TRADE_ACCEPT_TRADE = 160
    PLAYER_TRADE_SET_SILVER_OR_GOLD = 161
    SEND_MINI_MAP_PING = 162
    STUCK = 163
    BUY_REAL_ESTATE = 164
    CLAIM_REAL_ESTATE = 165
    GIVE_UP_REAL_ESTATE = 166
    CHANGE_REAL_ESTATE_OUTLINE = 167
    GET_MAIL_INFOS = 168
    GET_MAIL_COUNT = 169
    READ_MAIL = 170
    SEND_NEW_MAIL = 171
    DELETE_MAIL = 172
    MARK_MAIL_UNREAD = 173
    CLAIM_ATTACHMENT_FROM_MAIL = 174
    APPLY_TO_GUILD = 175
    ANSWER_GUILD_APPLICATION = 176
    REQUEST_GUILD_FINDER_FILTERED_LIST = 177
    UPDATE_GUILD_RECRUITMENT_INFO = 178
    REQUEST_GUILD_RECRUITMENT_INFO = 179
    REQUEST_GUILD_FINDER_NAME_SEARCH = 180
    REQUEST_GUILD_FINDER_RECOMMENDED_LIST = 181
    REGISTER_CHAT_PEER = 182
    SEND_CHAT_MESSAGE = 183
    SEND_MODERATOR_MESSAGE = 184
    JOIN_CHAT_CHANNEL = 185
    LEAVE_CHAT_CHANNEL = 186
    SEND_WHISPER_MESSAGE = 187
    SAY = 188
    PLAY_EMOTE = 189
    STOP_EMOTE = 190
    GET_CLUSTER_MAP_INFO = 191
    ACCESS_RIGHTS_CHANGE_SETTINGS = 192
    MOUNT = 193
    MOUNT_CANCEL = 194
    BUY_JOURNEY = 195
    SET_SALE_STATUS_FOR_ESTATE = 196
    RESOLVE_GUILD_OR_PLAYER_NAME = 197
    GET_RESPAWN_INFOS = 198
    MAKE_HOME = 199
    LEAVE_HOME = 200
    RESURRECTION_REPLY = 201
    ALLIANCE_CREATE = 202
    ALLIANCE_DISBAND = 203
    ALLIANCE_GET_MEMBER_INFOS = 204
    ALLIANCE_INVITE = 205
    ALLIANCE_ANSWER_INVITATION = 206
    ALLIANCE_CANCEL_INVITATION = 207
    ALLIANCE_KICK_GUILD = 208
    ALLIANCE_LEAVE = 209
    ALLIANCE_CHANGE_GOLD_PAYMENT_FLAG = 210
    ALLIANCE_GET_DETAIL_INFO = 211
    GET_ISLAND_INFOS = 212
    BUY_MY_ISLAND = 213
    BUY_GUILD_ISLAND = 214
    UPGRADE_MY_ISLAND = 215
    UPGRADE_GUILD_ISLAND = 216
    TERRITORY_FILL_NUTRITION = 217
    TELEPORT_BACK = 218
    PARTY_INVITE_PLAYER = 219
    PARTY_REQUEST_JOIN = 220
    PARTY_ANSWER_INVITATION = 221
    PARTY_ANSWER_JOIN_REQUEST = 222
    PARTY_LEAVE = 223
    PARTY_KICK_PLAYER = 224
    PARTY_MAKE_LEADER = 225
    PARTY_CHANGE_LOOT_SETTING = 226
    PARTY_MARK_OBJECT = 227
    PARTY_SET_ROLE = 228
    SET_GUILD_CODEX = 229
    EXIT_ENTER_START = 230
    EXIT_ENTER_CANCEL = 231
    QUEST_GIVER_REQUEST = 232
    GOLD_MARKET_GET_BUY_OFFER = 233
    GOLD_MARKET_GET_BUY_OFFER_FROM_SILVER = 234
    GOLD_MARKET_GET_SELL_OFFER = 235
    GOLD_MARKET_GET_SELL_OFFER_FROM_SILVER = 236
    GOLD_MARKET_BUY_GOLD = 237
    GOLD_MARKET_SELL_GOLD = 238
    GOLD_MARKET_CREATE_SELL_ORDER = 239
    GOLD_MARKET_CREATE_BUY_ORDER = 240
    GOLD_MARKET_GET_INFOS = 241
    GOLD_MARKET_CANCEL_ORDER = 242
    GOLD_MARKET_GET_AVERAGE_INFO = 243
    TREASURE_CHEST_USING_START = 244
    TREASURE_CHEST_USING_CANCEL = 245
    USE_LOOT_CHEST = 246
    USE_SHRINE = 247
    USE_HELLGATE_SHRINE = 248
    GET_SIEGE_BANNER_INFO = 249
    LABORER_START_JOB = 250
    LABORER_TAKE_JOB_LOOT = 251
    LABORER_DISMISS = 252
    LABORER_MOVE = 253
    LABORER_BUY_ITEM = 254
    LABORER_UPGRADE = 255
    BUY_PREMIUM = 256
    REAL_ESTATE_GET_AUCTION_DATA = 257
    REAL_ESTATE_BID_ON_AUCTION = 258
    FRIEND_INVITE = 259
    FRIEND_ANSWER_INVITATION = 260
    FRIEND_CANCELNVITATION = 261
    FRIEND_REMOVE = 262
    INVENTORY_STACK = 263
    INVENTORY_REORDER = 264
    INVENTORY_DROP_ALL = 265
    INVENTORY_ADD_TO_STACKS = 266
    EQUIPMENT_ITEM_CHANGE_SPELL = 267
    EXPEDITION_REGISTER = 268
    EXPEDITION_REGISTER_CANCEL = 269
    JOIN_EXPEDITION = 270
    DECLINE_EXPEDITION_INVITATION = 271
    VOTE_START = 272
    VOTE_DO_VOTE = 273
    RATING_DO_RATE = 274
    ENTERING_EXPEDITION_START = 275
    ENTERING_EXPEDITION_CANCEL = 276
    ACTIVATE_EXPEDITION_CHECK_POINT = 277
    ARENA_REGISTER = 278
    ARENA_ADD_INVITE = 279
    ARENA_REGISTER_CANCEL = 280
    ARENA_LEAVE = 281
    JOIN_ARENA_MATCH = 282
    DECLINE_ARENA_INVITATION = 283
    ENTERING_ARENA_START = 284
    ENTERING_ARENA_CANCEL = 285
    ARENA_CUSTOM_MATCH = 286
    UPDATE_CHARACTER_STATEMENT = 287
    BOOST_FARMABLE = 288
    GET_STRIKE_HISTORY = 289
    USE_FUNCTION = 290
    USE_PORTAL_ENTRANCE = 291
    RESET_PORTAL_BINDING = 292
    QUERY_PORTAL_BINDING = 293
    CLAIM_PAYMENT_TRANSACTION = 294
    CHANGE_USE_FLAG = 295
    CLIENT_PERFORMANCE_STATS = 296
    EXTENDED_HARDWARE_STATS = 297
    CLIENT_LOW_MEMORY_WARNING = 298
    TERRITORY_CLAIM_START = 299
    TERRITORY_CLAIM_CANCEL = 300
    DELIVER_CARRIABLE_OBJECT_START = 301
    DELIVER_CARRIABLE_OBJECT_CANCEL = 302
    TERRITORY_UPGRADE_WITH_POWER_CRYSTAL = 303
    REQUEST_APP_STORE_PRODUCTS = 304
    VERIFY_PRODUCT_PURCHASE = 305
    QUERY_GUILD_PLAYER_STATS = 306
    QUERY_ALLIANCE_GUILD_STATS = 307
    TRACK_ACHIEVEMENTS = 308
    SET_ACHIEVEMENTS_AUTO_LEARN = 309
    DEPOSIT_ITEM_TO_GUILD_CURRENCY = 310
    WITHDRAWAL_ITEM_FROM_GUILD_CURRENCY = 311
    AUCTION_SELL_SPECIFIC_ITEM_REQUEST = 312
    FISHING_START = 313
    FISHING_CASTING = 314
    FISHING_CAST = 315
    FISHING_CATCH = 316
    FISHING_PULL = 317
    FISHING_GIVE_LINE = 318
    FISHING_FINISH = 319
    FISHING_CANCEL = 320
    CREATE_GUILD_ACCESS_TAG = 321
    DELETE_GUILD_ACCESS_TAG = 322
    RENAME_GUILD_ACCESS_TAG = 323
    FLAG_GUILD_ACCESS_TAG_GUILD_PERMISSION = 324
    ASSIGN_GUILD_ACCESS_TAG = 325
    REMOVE_GUILD_ACCESS_TAG_FROM_PLAYER = 326
    MODIFY_GUILD_ACCESS_TAG_EDITORS = 327
    REQUEST_PUBLIC_ACCESS_TAGS = 328
    CHANGE_ACCESS_TAG_PUBLIC_FLAG = 329
    UPDATE_GUILD_ACCESS_TAG = 330
    STEAM_START_MICROTRANSACTION = 331
    STEAM_FINISH_MICROTRANSACTION = 332
    STEAM_ID_HAS_ACTIVE_ACCOUNT = 333
    CHECK_EMAIL_ACCOUNT_STATE = 334
    LINK_ACCOUNT_TO_STEAM_ID = 335
    IN_APP_CONFIRM_PAYMENT_GOOGLE_PLAY = 336
    IN_APP_CONFIRM_PAYMENT_APPLE_APP_STORE = 337
    IN_APP_PURCHASE_REQUEST = 338
    IN_APP_PURCHASE_FAILED = 339
    CHARACTER_SUBSCRIPTION_INFO = 340
    ACCOUNT_SUBSCRIPTION_INFO = 341
    BUY_GVG_SEASON_BOOSTER = 342
    CHANGE_FLAGGING_PREPARE = 343
    OVER_CHARGE = 344
    OVER_CHARGE_END = 345
    REQUEST_TRUSTED = 346
    CHANGE_GUILD_LOGO = 347
    PARTY_FINDER_REGISTER_FOR_UPDATES = 348
    PARTY_FINDER_UNREGISTER_FOR_UPDATES = 349
    PARTY_FINDER_ENLIST_NEW_PARTY_SEARCH = 350
    PARTY_FINDER_DELETE_PARTY_SEARCH = 351
    PARTY_FINDER_CHANGE_PARTY_SEARCH = 352
    PARTY_FINDER_CHANGE_ROLE = 353
    PARTY_FINDER_APPLY_FOR_GROUP = 354
    PARTY_FINDER_ACCEPT_OR_DECLINE_APPLY_FOR_GROUP = 355
    PARTY_FINDER_GET_EQUIPMENT_SNAPSHOT = 356
    PARTY_FINDER_REGISTER_APPLICANTS = 357
    PARTY_FINDER_UNREGISTER_APPLICANTS = 358
    PARTY_FINDER_FULLTEXT_SEARCH = 359
    PARTY_FINDER_REQUEST_EQUIPMENT_SNAPSHOT = 360
    GET_PERSONAL_SEASON_TRACKER_DATA = 361
    GET_PERSONAL_SEASON_PAST_REWARD_DATA = 362
    USE_CONSUMABLE_FROM_INVENTORY = 363
    CLAIM_PERSONAL_SEASON_REWARD = 364
    EASY_ANTI_CHEAT_MESSAGE_TO_SERVER = 365
    XIGN_CODE_MESSAGE_TO_SERVER = 366
    BATTL_EYE_MESSAGE_TO_SERVER = 367
    SET_NEXT_TUTORIAL_STATE = 368
    ADD_PLAYER_TO_MUTE_LIST = 369
    REMOVE_PLAYER_FROM_MUTE_LIST = 370
    PRODUCT_SHOP_USER_EVENT = 371
    GET_VANITY_UNLOCKS = 372
    BUY_VANITY_UNLOCKS = 373
    GET_MOUNT_SKINS = 374
    SET_MOUNT_SKIN = 375
    SET_WARDROBE = 376
    CHANGE_CUSTOMIZATION = 377
    CHANGE_PLAYER_ISLAND_DATA = 378
    GET_GUILD_CHALLENGE_POINTS = 379
    SMART_QUEUE_JOIN = 380
    SMART_QUEUE_LEAVE = 381
    SMART_QUEUE_SELECT_SPAWN_CLUSTER = 382
    UPGRADE_HIDEOUT = 383
    INIT_HIDEOUT_ATTACK_START = 384
    INIT_HIDEOUT_ATTACK_CANCEL = 385
    HIDEOUT_FILL_NUTRITION = 386
    HIDEOUT_GET_INFO = 387
    HIDEOUT_GET_OWNER_INFO = 388
    HIDEOUT_SET_TRIBUTE = 389
    HIDEOUT_UPGRADE_WITH_POWER_CRYSTAL = 390
    HIDEOUT_DECLARE_H_Q = 391
    HIDEOUT_UNDECLARE_H_Q = 392
    HIDEOUT_GET_H_Q_REQUIREMENTS = 393
    HIDEOUT_BOOST = 394
    HIDEOUT_BOOST_CONSTRUCTION = 395
    OPEN_WORLD_ATTACK_SCHEDULE_START = 396
    OPEN_WORLD_ATTACK_SCHEDULE_CANCEL = 397
    OPEN_WORLD_ATTACK_CONQUER_START = 398
    OPEN_WORLD_ATTACK_CONQUER_CANCEL = 399
    GET_OPEN_WORLD_ATTACK_DETAILS = 400
    GET_NEXT_OPEN_WORLD_ATTACK_SCHEDULE_TIME = 401
    RECOVER_VAULT_FROM_HIDEOUT = 402
    GET_GUILD_ENERGY_DRAIN_INFO = 403
    CHANNELING_UPDATE = 404
    USE_CORRUPTED_SHRINE = 405
    REQUEST_ESTIMATED_MARKET_VALUE = 406
    LOG_FEEDBACK = 407
    GET_INFAMY_INFO = 408
    GET_PARTY_SMART_CLUSTER_QUEUE_PRIORITY = 409
    SET_PARTY_SMART_CLUSTER_QUEUE_PRIORITY = 410
    CLIENT_ANTI_AUTO_CLICKER_INFO = 411
    CLIENT_BOT_PATTERN_DETECTION_INFO = 412
    CLIENT_ANTI_GATHER_CLICKER_INFO = 413
    LOADOUT_CREATE = 414
    LOADOUT_READ = 415
    LOADOUT_READ_HEADERS = 416
    LOADOUT_UPDATE = 417
    LOADOUT_DELETE = 418
    LOADOUT_ORDER_UPDATE = 419
    LOADOUT_EQUIP = 420
    BATCH_USE_ITEM_CANCEL = 421
    ENLIST_FACTION_WARFARE = 422
    GET_FACTION_WARFARE_WEEKLY_REPORT = 423
    CLAIM_FACTION_WARFARE_WEEKLY_REPORT = 424
    GET_FACTION_WARFARE_CAMPAIGN_DATA = 425
    CLAIM_FACTION_WARFARE_ITEM_REWARD = 426
    SEND_MEMORY_CONSUMPTION = 427
    PICKUP_CARRIABLE_OBJECT_START = 428
    PICKUP_CARRIABLE_OBJECT_CANCEL = 429
    SET_SAVING_CHEST_LOGS_FLAG = 430
    GET_SAVING_CHEST_LOGS_FLAG = 431
    REGISTER_GUEST_ACCOUNT = 432
    RESEND_GUEST_ACCOUNT_VERIFICATION_EMAIL = 433
    DO_SIMPLE_ACTION_START = 434
    DO_SIMPLE_ACTION_CANCEL = 435
    GET_GVG_SEASON_CONTRIBUTION_BY_ACTIVITY = 436
    GET_GVG_SEASON_CONTRIBUTION_BY_CRYSTAL_LEAGUE = 437
    GET_GUILD_MIGHT_CATEGORY_CONTRIBUTION = 438
    GET_GUILD_MIGHT_CATEGORY_OVERVIEW = 439
    GET_PVP_CHALLENGE_DATA = 440
    CLAIM_PVP_CHALLENGE_WEEKLY_REWARD = 441
    GET_PERSONAL_MIGHT_STATS = 442
    AUCTION_GET_LOADOUT_OFFERS = 443
    AUCTION_BUY_LOADOUT_OFFER = 444
    ACCOUNT_DELETION_REQUEST = 445
    ACCOUNT_REACTIVATION_REQUEST = 446
    GET_MODERATION_ESCALATION_DEFINITON = 447
    EVENT_BASED_POPUP_ADD_SEEN = 448
    GET_ITEM_KILL_HISTORY = 449
    GET_VANITY_CONSUMABLES = 450
    EQUIP_KILL_EMOTE = 451
    CHANGE_KILL_EMOTE_PLAY_ON_KNOCKDOWN_SETTING = 452
    BUY_VANITY_CONSUMABLE_CHARGES = 453
    RECLAIM_VANITY_ITEM = 454
    GET_ARENA_RANKINGS = 455
    GET_CRYSTAL_LEAGUE_STATISTICS = 456
    SEND_OPTIONS_LOG = 457
    SEND_CONTROLS_OPTIONS_LOG = 458
    MISTS_USE_IMMEDIATE_RETURN_EXIT = 459
    MISTS_USE_STATIC_ENTRANCE = 460
    MISTS_USE_CITY_ROADS_ENTRANCE = 461
    CHANGE_NEW_GUILD_MEMBER_MAIL = 462
    GET_NEW_GUILD_MEMBER_MAIL = 463
    CHANGE_GUILD_FACTION_ALLEGIANCE = 464
    GET_GUILD_FACTION_ALLEGIANCE = 465
    GUILD_BANNER_CHANGE = 466
    GUILD_GET_OPTIONAL_STATS = 467
    GUILD_SET_OPTIONAL_STATS = 468
    GET_PLAYER_INFO_FOR_STALK = 469
    PAY_GOLD_FOR_CHARACTER_TYPE_CHANGE = 470
    QUICK_SELL_AUCTION_QUERY_ACTION = 471
    QUICK_SELL_AUCTION_SELL_ACTION = 472
    FCM_TOKEN_TO_SERVER = 473
    APNS_TOKEN_TO_SERVER = 474
    DEATH_RECAP = 475
    AUCTION_FETCH_FINISHED_AUCTIONS = 476
    ABORT_AUCTION_FETCH_FINISHED_AUCTIONS = 477
    REQUEST_LEGENDARY_EVEN_HISTORY = 478
    PARTY_ANSWER_START_HUNT_REQUEST = 479
    HUNT_ABORT = 480
    USE_FIND_TRACK_SPELL_FROM_ITEM_PREPARE = 481
    INTERACT_WITH_TRACK_START = 482
    INTERACT_WITH_TRACK_CANCEL = 483
    TERRITORY_RAID_START = 484
    TERRITORY_RAID_CANCEL = 485
    TERRITORY_CLAIM_RAIDED_RAW_ENERGY_CRYSTAL_RESULT = 486
    GV_G_SEASON_PLAYER_GUILD_PARTICIPATION_DETAILS = 487
    DAILY_MIGHT_BONUS = 488
    CLAIM_DAILY_MIGHT_BONUS = 489
    GET_FORTIFICATION_GROUP_INFO = 490
    UPGRADE_FORTIFICATION_GROUP = 491
    CANCEL_UPGRADE_FORTIFICATION_GROUP = 492
    DOWNGRADE_FORTIFICATION_GROUP = 493
    GET_CLUSTER_ACTIVITY_CHEST_ESTIMATES = 494
    PARTY_READY_CHECK_BEGIN = 495
    PARTY_READY_CHECK_UPDATE = 496
    CLAIM_ALBION_JOURNAL_REWARD = 497
    TRACK_ALBION_JOURNAL_ACHIEVEMENTS = 498
    REQUEST_OUTLANDS_TELEPORTATION_USAGE = 499
