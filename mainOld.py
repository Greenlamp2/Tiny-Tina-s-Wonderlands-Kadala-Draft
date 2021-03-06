import os
import random
import sys

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
    mod_weird = "TTW(BQAAAABsaYC7hwbBh4oEEHCeC3fDIUzqoIMOuvymg4hFFjWDgQAAAAAQ)"
    gneu = "TTW(BQAAAADVdIA7McGAgIIcD0hES7VOWCNNKIbZZsKAEAAAAAAAYIwBBAE=)"
    gneu2 = "TTW(BQAAAACntIC7ECLAgCqm0loABwAAAA==)"
    gneu3 = "TTW(BQAAAADlDIC7/i2AgToClNiWRzoogwMABAA=)"
    gneu4 = "TTW(BQAAAACZHIA7EGJAETIErDRTgKYAAAAE)"
    tide = "TTW(BQAAAADl1oC7hwbBh4oEEJAeC3e7IUzpPpHvE+fkg0gOiDSDgQAAAAAY)"
    # for serial in [
    #     liquid_cooling,
    #     materwork,
    #     spellblade
    # ]:
    #     item = db.reverse_item_serial(serial)
    #     print(db.is_legit(item))

    # db.get_category('Balance_Armor_CapeOfTides', 'Part_P_SkillCombo_GunMage_Ranger_01')

    # seed = 8037935898601526959
    seed = random.randrange(sys.maxsize)
    rng = random.Random(seed)
    print("Seed was:", seed)
    # item = db.reverse_item_serial(gneu4)
    # new_item = db.generate_random(item, seed=5508852444783207627)
    # print(new_item.get_serial_base64())

    # item = db.reverse_item_serial(gneu)
    # print(db.is_legit(item))

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    save_a = WonderlandsSave(os.path.join(__location__, "saves_test/1.sav"))
    for item in save_a.get_items():
        new_item = db.generate_random(item, seed=seed)
    # save_a.save_to("saves_test/9.sav")
