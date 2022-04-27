import os

from Items import Items
from ttw_save_editor.WonderlandsItem import WonderlandsItem
from ttw_save_editor.WonderlandsSave import WonderlandsSave

if __name__ == '__main__':
    db = Items()
    db.load('export/gun_balances_long.csv', "GUNS")
    db.load('export/shield_balances_long.csv', "SHIELDS")
    db.load('export/pauldron_balances_long.csv', "PAULDRONS")
    db.load('export/spell_balances_long.csv', "SPELLS")
    db.load('export/ring_balances_long.csv', "RINGS")
    db.load('export/amulet_balances_long.csv', "AMULETS")
    db.load('export/melee_balances_long.csv', "MELEE")

    liquid_cooling = "TTW(BQAAAAA7kIA745WggIKuqaIsOpIg1PBYMsODgBAAAAAAAKCMAQEB)"
    materwork = "TTW(BQAAAAAt4IC76J0ggnomj4gEEtzxKhqcaDQUBgEhAAAAAACAGQMEAA==)"
    spellblade = "TTW(BQAAAADlpYC74BXhgDJUk9WDMwoEABAE)"
    mod_bladesinger = "TTW(BQAAAADzsIA7LAbhh4oEEHCeC3fDYUnqoIMOuukSosQSzaCDgQAAAAAI)"
    amulet_theruge = "TTW(BQAAAABiwIA7HyLAgDKuMpbygwMAAAA=)"
    ring = "TTW(BQAAAABMOYC7JioAgTKAeEREJqAAAAAA)"
    crash = "TTW(BQAAAACya4A7ecCAgJIckMhDSCwOJ6mXqAOKVVCZICAEAAAAAAAgAwIAAA==)"
    mod_test_good = "TTW(BQAAAABHDoC7hwbBh4oEEHAeDHfLIUzmnIvFOedigQgizSCCgQAAAAAY)"
    mod_test_missing_ranger = "TTW(BQAAAADJE4C7hwbBh4oEEHAeDHfLIUzmnIvFOef2g0gOiDSDgQAAAAAY)"
    mod_test_rogue_not_medium = "TTW(BQAAAAAXpIC7hwbBh4oEEJAeDHfLIUzmnIPOOef2g0gOiDSDgQAAAAAY)"
    mod_test_passive_from_outside = "TTW(BQAAAAAR+4C7hwbBh4oEEHAeDHfLIUzmnIPOOef2g0gOiDSDgQAAAAAY)"
    mod_test_duplicate_rarity = "TTW(BQAAAAAiV4C7hwbBh5IEEJAeDHfLIUzmnHPOOef2g0gOiDTTDAYCAAAAAA==)"
    # for serial in [
    #     # mod_test_good,
    #     mod_bladesinger,
    #     # mod_test_too_much,
    #     # mod_test_duplicate_rarity,
    # ]:
    #     item = db.reverse_item_serial(serial)
    #     print(db.is_legit(item))
    item = db.reverse_item_serial(mod_test_good)
    new_item = db.generate_random(item)
    print(new_item.get_serial_base64())

    # __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    # save_a = WonderlandsSave(os.path.join(__location__, "saves_test/9.sav"))
    # save_a.generate_random_item(db, item, 1)
    # save_a.save_to("saves_test/9.sav")
