import csv
import random

from ttw_save_editor import datalib
from ttw_save_editor.datalib import BL3Serial


class Items:
    def __init__(self):
        self.items = {}
        self.clusters = {}
        self.clusters_raw = [
            [
                "MoveSpeed",
                "CompanionCritChance",
                "SkillCritChance",
            ], [
                "WardMax",
                "WardDelay",
                "WardRegenRate",
                "HealthMax",
                "HealthRegen",
            ], [
                "AllDamage",
                "SkillDamage",
            ], [
                "GunCritChance",
                "SpellCritChance",
                "MeleeCritChance",
            ], [
                "GunDamage",
                "SpellDamage",
                "MeleeDamage",
            ], [
                "CompanionDamage",
                "SplashDamage",
                "FireRate",
            ]
        ]
        self.passives_raw = {
            "Rogue": {
                "Follow Up": "Passive_01",
                "Sneak Attack": "Passive_02",
                "Alchemical Agent": "Passive_03",
                "Nimble Finger": "Passive_04",
                "Swift Death": "Passive_05",
                "Potent Poisons": "Passive_06",
                "Arsenal": "Passive_07",
                "Shadow Step": "Passive_08",
                "Haste": "Passive_10",
                "Contagion": "Passive_12",
                "Elusive": "Passive_13",
                "A Thousand Cuts": "Passive_14",
                "Exploit Weakness": "Passive_15",
                "Executioner's Blade": "Passive_17",
            },
            "GunMage": {
                "Font of Mana": "Passive_01",
                "Glass Cannon": "Passive_02",
                "Double Knot": "Passive_08",
                "Spell Sniper": "Passive_09",
                "Imbued Weapon": "Passive_13",
                "Prestidigitation": "Passive_14",
                "Sever the Thread": "Passive_15",
                "Just Warming Up": "Passive_16",
                "High Thread Count": "Passive_17",
                "War Caster": "Passive_18",
                "One Slot, One Kill": "Passive_19",
                "Mage Armor": "Passive_20",
                "Magic Bullets": "Passive_21",
            },
            "Graveborn": {
                "Mortal Vessel": "Passive_01",
                "Dark Pact": "Passive_02",
                "Faithful Thralls": "Passive_03",
                "Sanguine Sacrament": "Passive_04",
                "Essence Drain": "Passive_05",
                "Punishment": "Passive_06",
                "Dark Hydra": "Passive_08",
                "Dread Covenant": "Passive_09",
                "Lord of Edges": "Passive_10",
                "Blast Gasp": "Passive_12",
                "Ascension": "Passive_13",
                "Stain of the Soul": "Passive_14",
                "Harvest": "Passive_15",
                "Morhaim's Blessing": "Passive_17",
            },
            "Barbarian": {
                "Ancestral Frost": "Passive_01",
                "Savagery": "Passive_02",
                "Unyielding": "Passive_03",
                "Ice Breaker": "Passive_04",
                "The Old Ways": "Passive_05",
                "Instinct": "Passive_06",
                "Cold Snap": "Passive_07",
                "Unarmored Defense": "Passive_08",
                "Blood Frenzy": "Passive_09",
                "Blood of the Fallen": "Passive_11",
                "Iron Squall": "Passive_13",
                "Ancient Fury": "Passive_14",
                "Relentless Rage": "Passive_15",
                "Blast Chill": "Passive_17",
            },
            "Ranger": {
                "Bounty of the Hunt": "Passive_01",
                "Kindred Heart": "Passive_02",
                "Eagle Eye": "Passive_03",
                "Quiver of Holding": "Passive_04",
                "Headhunter": "Passive_05",
                "Bullseye": "Passive_06",
                "Medicinal Mushroom": "Passive_07",
                "Windrunner": "Passive_09",
                "Affinity": "Passive_10",
                "Spore Cloud": "Passive_11",
                "Wrath of Nature": "Passive_13",
                "Thrill of the Hunt": "Passive_14",
                "Called Shot": "Passive_15",
                "Play the Angles": "Passive_17",
            },
            "Necromancer": {
                "Oath of Fire": "Passive_03",
                "Friend to Flame": "Passive_04",
                "Radiance": "Passive_14",
                "Dedication": "Passive_15",
                "Oath of Thunder": "Passive_19",
                "Storm Smite": "Passive_21",
                "Rebuke": "Passive_22",
                "Blasthamut's Favor": "Passive_24",
                "Dragon Aura": "Passive_25",
                "Awe": "Passive_27",
                "Indomitable": "Passive_28",
                "Fire Bolt": "Passive_29",
                "Storm Breath": "Passive_30",
            }
        }
        self.combos = {}
        self.combos_raw = {
            "Barbarian": {
                "Necromancer": ["Savagery", "Blast Chill", "Dragon Aura"],
                "Graveborn": ["Ancient Fury", "Unyielding", "Blast Gasp"],
                "GunMage": ["Ancestral Frost", "Ice Breaker", "Imbued Weapon"],
                "Ranger": ["Ice Breaker", "Cold Snap", "Affinity"],
                "Rogue": ["Iron Squall", "The Old Ways", "Follow Up"],
            },
            "Necromancer": {
                "Barbarian": ["Rebuke", "Oath of Thunder", "Iron Squall"],
                "Graveborn": ["Friend to Flame", "Oath of Fire", "Harvest"],
                "GunMage": ["Radiance", "Dedication", "Mage Armor"],
                "Ranger": ["Blasthamut's Favor", "Oath of Fire", "Called Shot"],
                "Rogue": ["Awe", "Oath of Thunder", "Nimble Finger"],
            },
            "Graveborn": {
                "Barbarian": ["Mortal Vessel", "Ascension", "Blood Frenzy"],
                "Necromancer": ["Essence Drain", "Blast Gasp", "Dragon Aura"],
                "GunMage": ["Essence Drain", "Ascension", "War Caster"],
                "Ranger": ["Faithful Thralls", "Dark Hydra", "Thrill of the Hunt"],
                "Rogue": ["Dark Pact", "Stain of the Soul", "Contagion"],
            },
            "GunMage": {
                "Barbarian": ["Just Warming Up", "High Thread Count", "Instinct"],
                "Necromancer": ["Just Warming Up", "Font of Mana", "Awe"],
                "Graveborn": ["Spell Sniper", "Font of Mana", "Stain of the Soul"],
                "Ranger": ["High Thread Count", "Prestidigitation", "Windrunner"],
                "Rogue": ["Spell Sniper", "Double Knot", "A Thousand Cuts"],
            },
            "Ranger": {
                "Barbarian": ["Bounty of the Hunt", "Wrath of Nature", "Iron Squall"],
                "Necromancer": ["Kindred Heart", "Bullseye", "Friend to Flame"],
                "Graveborn": ["Kindred Heart", "Windrunner", "Harvest"],
                "GunMage": ["Called Shot", "Eagle Eye", "Imbued Weapon"],
                "Rogue": ["Bullseye", "Eagle Eye", "A Thousand Cuts"],
            },
            "Rogue": {
                "Barbarian": ["Haste", "Swift Death", "Cold Snap"],
                "Necromancer": ["Exploit Weakness", "Potent Poisons", "Dragon Aura"],
                "Graveborn": ["Arsenal", "Sneak Attack", "Lord of Edges"],
                "GunMage": ["Nimble Finger", "Arsenal", "Magic Bullets"],
                "Ranger": ["Swift Death", "Follow Up", "Windrunner"],
            },
        }
        self.can_roll = {
            "Rogue": [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
            "GunMage": [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
            "Graveborn": [1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0],
            "Barbarian": [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
            "Ranger": [1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
            "Necromancer": [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
        }
        self.levels = {
            "Rogue": [3, 5, 1, 3, 5, 5, 5, 1, 3, 3, 1, 5, 3, 1],
            "GunMage": [5, 1, 3, 5, 5, 5, 1, 5, 1, 5, 1, 1, 3],
            "Graveborn": [5, 5, 3, 3, 5, 1, 3, 1, 1, 5, 3, 5, 3, 1],
            "Barbarian": [5, 5, 3, 3, 5, 3, 3, 1, 3, 1, 5, 5, 1, 1],
            "Ranger": [5, 5, 5, 3, 1, 5, 1, 3, 5, 1, 3, 3, 3, 1],
            "Necromancer": [],
        }
        self.base_weights = {
            "light": 0,
            "medium": 0,
            "heavy": 0,
        }
        self.class_weights = {
            "GunMage": "Light",
            "Ranger": "Medium",
            "Rogue": "Medium",
            "Barbarian": "Heavy",
            "Knight": "Heavy",
            "Necromancer": "Light",
        }
        self.spread = {
            "Legendary": 5,
        }
        self.excluders = {}
        self.dependencies = {}

    def setup(self):
        self.compute_clusters()
        self.compute_skill_combos()
        self.compute_excluders_dependencies()

    def compute_excluders_dependencies(self):
        for balance, parts in self.items.items():
            for part in parts:
                if len(part.dependencies) > 0:
                    for dependency in part.dependencies:
                        if part.parts not in self.dependencies:
                            self.dependencies[part.parts] = []
                        if dependency not in self.dependencies[part.parts]:
                            self.dependencies[part.parts].append(dependency)
                if len(part.excluders) > 0:
                    for excluder in part.excluders:
                        if part.parts not in self.excluders:
                            self.excluders[part.parts] = []
                        if excluder not in self.excluders[part.parts]:
                            self.excluders[part.parts].append(excluder)

    def compute_clusters(self):
        for cluster in self.clusters_raw:
            for elm in cluster:
                for elm2 in cluster:
                    if elm == elm2:
                        continue
                    if elm not in self.clusters:
                        self.clusters[elm] = []
                    self.clusters[elm].append(elm2)

    def compute_skill_combos(self):
        self.combos = {}
        for characterA in self.combos_raw:
            for characterB in self.combos_raw[characterA]:
                skills = self.combos_raw[characterA][characterB]
                skillA = skills[0]
                skillA_key = self.passives_raw[characterA][skillA]
                skillB = skills[1]
                skillB_key = self.passives_raw[characterA][skillB]
                skillC = skills[2]
                skillC_key = self.passives_raw[characterB][skillC]
                if characterA not in self.combos:
                    self.combos[characterA] = {}
                self.combos[characterA][characterB] = [skillA_key, skillB_key, skillC_key]

    def load(self, filename, type):
        with open(filename, newline='\n') as file:
            reader = csv.reader(file, delimiter=',')
            header = next(reader)
            for row in reader:
                self.add(row, type)

    def add(self, row, type):
        item = Item(row, type)
        if not self.items.get(item.balance, None):
            self.items[item.balance] = []
        self.items[item.balance].append(item)

    def get_parts(self, balance):
        ret = {}
        for elm in self.items.get(balance, []):
            if not ret.get(elm.category, None):
                ret[elm.category] = []
            ret[elm.category].append(elm)
        return ret

    def get_category(self, balance_short, part):
        parts = self.items.get(balance_short, [])
        for elm in parts:
            if elm.parts and elm.parts.replace('\\', '/').split('/')[-1] == part:
                return elm.category

    def is_in_category(self, item, part, category):
        all_parts = self.get_parts(item.balance_short)
        parts = all_parts.get(category, [])
        for elm in parts:
            if elm.parts and elm.parts.replace('\\', '/').split('/')[-1] == part:
                return True
        return False

    def get_min_max(self, item, category):
        all_parts = self.get_parts(item.balance_short)
        to_sub = 0
        for elm in all_parts[category]:
            if not elm.parts:
                to_sub += 1
        part = all_parts[category][0]
        return part.min_parts-to_sub, part.max_parts

    def get_random_part(self, part_list):
        pool = []
        for part in part_list:
            if not part.parts:
                continue
            occurence = int(1.0 * part.weight * 100)
            for i in range(0, occurence):
                pool.append(part)
        n = random.randint(0, len(pool) - 1)
        return pool[n]

    def get_random_type(self):
        item_types = [
            (0, 58.14),
            (1, 23.26),
            (2, 17.44),
            (3, 1.16),
        ]
        pool = []
        for key, percent in item_types:
            occurence = int(percent * 100)
            for i in range(0, occurence):
                pool.append(key)

        n = random.randint(0, len(pool) - 1)
        return pool[n]

    # def check_excluders(self, pool, new_part):
    #     if new_part.parts in self.excluders:
    #         excluders = self.excluders[new_part.parts]
    #         for excluder in excluders:
    #             if excluder in pool:
    #                 return True
    #     return False

    def check_excluders(self, new_part, prev):
        if len(new_part.excluders) == 0:
            return True

        whatihave = {}
        whatifear = {}
        for elm in prev:
            if elm.category not in whatihave:
                whatihave[elm.category] = []
            whatihave[elm.category].append(elm.parts)
        for elm in new_part.excluders:
            cat = self.get_category(new_part.balance, elm.replace('\\', '/').split('/')[-1])
            if cat not in whatifear:
                whatifear[cat] = []
            whatifear[cat].append(elm)

        # return True if one value of whatihave is in whatineed for each key
        for key, value in whatifear.items():
            if key not in whatihave:
                continue
            not_found = True
            for elm in value:
                if elm in whatihave[key]:
                    not_found = False
                    break
            if not not_found:
                return False
        return True

    def check_included(self, new_part, prev):
        if len(new_part.dependencies) == 0:
            return True

        whatihave = {}
        whatineed = {}
        for elm in prev:
            if elm.category not in whatihave:
                whatihave[elm.category] = []
            whatihave[elm.category].append(elm.parts)
        for elm in new_part.dependencies:
            cat = self.get_category(new_part.balance, elm.replace('\\', '/').split('/')[-1])
            if not cat:
                continue
            if cat not in whatineed:
                whatineed[cat] = []
            whatineed[cat].append(elm)

        # return True if one value of whatihave is in whatineed for each key
        for key, value in whatineed.items():
            if key not in whatihave:
                return False
            found = False
            for elm in value:
                if elm in whatihave[key]:
                    found = True
                    break
            if not found:
                return False
        return True


    # def prev_get_random_min_max(self, parts, min, max, prev=None):
    #     def sort_fn(elm):
    #         return elm.parts
    #     ret = []
    #     pool = []
    #     for part in parts:
    #         if not part.parts:
    #             continue
    #         occurence = int((1.0 * part.weight) * 100)
    #         for i in range(0, occurence):
    #             pool.append(part)
    #     random.shuffle(pool)
    #
    #     m = random.randint(min, max)
    #     if m == 0:
    #         return ret
    #     while len(ret) < m:
    #         n = random.randint(0, len(pool) - 1)
    #         if not self.check_excluders(ret, pool[n]):
    #             ret.append(pool[n])
    #         else:
    #             pool.sort(key=sort_fn)
    #             new_pool = list(filter(lambda elm: elm.parts != pool[n].parts, pool))
    #             pool = new_pool
    #             random.shuffle(pool)
    #     return ret

    def count_occurrence(self, pool):
        ret = {}
        for elm in pool:
            id = elm.parts.split("/")[-1]
            if id not in ret:
                ret[id] = 0
            ret[id] += 1
        return ret

    def get_random_min_max(self, parts, min, max, prev=[]):
        def sort_fn(elm):
            return elm.parts
        ret = []
        pool = []
        for part in parts:
            if not part.parts:
                continue
            occurence = int((1.0 * part.weight) * 100)
            for i in range(0, occurence):
                pool.append(part)
        random.shuffle(pool)

        m = random.randint(min, max)
        if m == 0:
            return ret
        while len(ret) < m:
            if len(pool) == 0:
                print("")
            n = random.randint(0, len(pool) - 1)
            target = pool[n]
            name = target.parts
            if self.check_excluders(target, prev+ret) and self.check_included(target, prev+ret):
                ret.append(pool[n])
            else:
                pool.sort(key=sort_fn)
                prev_count_occu = self.count_occurrence(pool)
                new_pool = [elm for elm in pool if elm.parts != target.parts]
                count_occu = self.count_occurrence(new_pool)
                pool = new_pool
                random.shuffle(pool)
        return ret

    def get_part_with_dep_and_exc(self, values, dep=None, exc=None):
        pool = []
        for elm in values:
            if len(elm.dependencies) > 1:
                print("")
            one_of = False
            for depen in elm.dependencies:
                if not one_of:
                    for p in dep:
                        if p.parts == depen:
                            one_of = True
                            break
            included = not dep or len(elm.dependencies) == 0 or one_of
            excluded = exc and (len(elm.excluders) > 0 and exc[0].parts in elm.excluders)
            if included and not excluded:
                pool.append(elm)
        min, max = values[0].min_parts, values[0].max_parts
        return self.get_random_min_max(pool, min, max)


    def generate_new_pauldron_parts(self, item):
        new_item_parts = []
        all_parts = self.get_parts(item.balance_short)
        body = self.get_part_with_dep_and_exc(all_parts["BODY"])
        primary_class = self.get_part_with_dep_and_exc(all_parts["CLASS"], body, None)
        body_secondary = self.get_part_with_dep_and_exc(all_parts["BODY SECONDARY"], None, body)
        secondary_class = self.get_part_with_dep_and_exc(all_parts["CLASS SECONDARY"], body_secondary, primary_class)
        class_stat = self.get_part_with_dep_and_exc(all_parts["CLASS STAT"], primary_class, None)
        class_stat_secondary = self.get_part_with_dep_and_exc(all_parts["CLASS STAT SECONDARY"], secondary_class, class_stat)
        legendary_aug = self.get_part_with_dep_and_exc(all_parts["LEGENDARY AUG"], None, None)
        skill_combo = self.get_part_with_dep_and_exc(all_parts["PASSIVE SKILL COMBO"], primary_class+secondary_class, None)
        # trim possible skill part
        skill_part = self.get_part_with_dep_and_exc(all_parts["PASSIVE SKILL PARTS"], skill_combo, None)
        player_stat = self.get_part_with_dep_and_exc(all_parts["PLAYER STAT"], body+body_secondary, None)
        rarity = self.get_part_with_dep_and_exc(all_parts["RARITY"], body+body_secondary, None)
        new_item_parts = body + primary_class + body_secondary + secondary_class + class_stat + class_stat_secondary + legendary_aug + skill_combo + skill_part + player_stat + rarity
        return new_item_parts

    def get_legit_random_parts(self, item):
        new_item_parts = []
        all_parts = self.get_parts(item.balance_short)
        for type, parts in all_parts.items():
            if len(parts) == parts[0].min_parts:
                new_item_parts += parts
                continue
            min, max = parts[0].min_parts, parts[0].max_parts
            res = self.get_random_min_max(parts, min, max, new_item_parts)
            new_item_parts += res
        return new_item_parts

    def reverse_item_serial(self, serial_number):
        c = BL3Serial.decode_serial_base64(serial_number)
        datawrapper = datalib.DataWrapper()
        return datalib.BL3Serial(c, datawrapper)

    def get_serial_string(self, item):
        return item.get_serial_base64()

    def generate_random(self, original_item):
        serial = original_item.get_serial_base64()
        item = self.reverse_item_serial(serial)
        legit = False
        while not legit:
            new_parts = self.get_legit_random_parts(item)
            item.set_parts(new_parts)
            item_type = self.get_random_type()
            item.set_item_type(item_type)
            if self.is_legit(item):
                legit = True
        return item

    def is_legit(self, item, silent=False):
        item_parts = item.parts
        counts = {}
        parts_list = []
        parts_list_long = []
        for part, id in item_parts:
            part_name = part.split('.')[-1]
            parts_list_long.append(part)
            cat = self.get_category(item.balance_short, part_name)
            if not cat:
                if not silent:
                    print("{} for {} is not a possible part".format(part_name, item.balance_short, cat))
                return False
            good = self.is_in_category(item, part_name, cat)
            if good:
                if not counts.get(cat, None):
                    counts[cat] = 0
                counts[cat] = counts[cat] + 1
            else:
                if not silent:
                    print("{} for {} is not a possible part as {}".format(part_name, item.balance_short, cat))
                return False
            # if part_name in parts_list \
            #         and "Minor" not in part_name \
            #         and "_Enh_" not in part_name \
            #         and "_Aug_" not in part_name \
            #         and "_PassiveSkill_" not in part_name:
            #     if not silent:
            #         print("{} for {} is present more than once".format(part_name, item.balance_short))
            #     return False
            parts_list.append(part_name)

        for key, value in counts.items():
            min, max = self.get_min_max(item, key)
            if value < min:
                if not silent:
                    print("{} for {} should be {} min but there is only {}".format(key, item.balance_short, min, value))
                return False
            if value > max:
                if not silent:
                    print("{} for {} should be {} max but there is {}".format(key, item.balance_short, max, value))
                return False

        if self.has_excluders(item.balance_short, parts_list_long):
            return False
        if self.missing_dependant(item.balance_short, parts_list_long):
            return False

        # if "/Pauldrons" in item.balance:
        #     # print(item.get_serial_base64())
        #     if self.has_wrong_pauldron_stats(item.balance_short, parts_list_long):
        #         return False

        if not silent:
            print("{} is legit".format(item.balance_short))
        return True

    def get_excluders(self, balance, target):
        parts = self.items[balance]
        for part in parts:
            if part.parts == target:
                return part.excluders
        return []

    def get_dependant(self, balance, target):
        parts = self.items[balance]
        for part in parts:
            if part.parts == target:
                return part.dependencies
        return []

    def has_wrong_clusters(self, balance, parts_target, silent=False):
        for part in parts_target:
            if "/PlayerStat/" not in part:
                continue
            for part2 in parts_target:
                if "/PlayerStat/" not in part2 or part == part2:
                    continue
                part_name = part.split("PlayerStat_")[1].split("_")[0]
                part2_name = part2.split("PlayerStat_")[1].split("_")[0]
                cluster = self.clusters[part_name]
                if part2_name in cluster:
                    if not silent:
                        print('{} is a passive stat in the same cluster as {}'.format(part_name, part2_name))
                    return False

    def has_wrong_pauldron_stats(self, balance, parts_target, silent=False):
        characterA = None
        characterB = None
        weightA = None
        weightB = None
        combo = None
        unique_part = 0
        rarity = None
        count_part = 0
        skills = []
        overrides = []
        for part in parts_target:
            if "/Class/Part" in part:
                characterA = part.split("Primary_")[1].split(".")[0]
            if "/Class/Secondary/Part" in part:
                characterB = part.split("Secondary_")[1].split(".")[0]
            if "/Base/" in part and "P_Base_" in part:
                weightA = part.split("Base_")[1].split(".")[0]
            if "/Base_Secondary/Part_" in part:
                weightB = part.split("Base_Secondary_")[1].split(".")[0]
            if "/SkillCombos/" in part:
                combo = part.split("SkillCombo_")[1].split("_0")[0]
            if "/_Uniques/" in part:
                unique_part += 1
            if "/Rarity/" in part:
                rarity = part.split("Rarity_")[-1].split("_")[-1]
            if "/SkillParts/" in part:
                count_part += 1
            if "/SkillParts/" in part:
                skill = part.split("PassiveSkill_")[1].split(".")[0]
                skills.append("{}_Passive_{}".format(skill.split("_")[0], skill.split("_")[1]))
            if "/PlayerStat/" in part:
                override = part.split("PlayerStat_")[1].split(".")[0]
                overrides.append(override.split("_")[0])

        if rarity != "Legendary":
            if not silent:
                print("This is not a legendary, i don't check it")
            return False
        if self.class_weights[characterA] != weightA:
            if not silent:
                print('{} should have a base part {} but got {}'.format(characterA, self.class_weights[characterA], weightA))
            return True
        if self.class_weights[characterB] != weightB:
            if not silent:
                print('{} should have a base part {} but got {}'.format(characterB, self.class_weights[characterB], weightB))
            return True
        if combo != "{}_{}".format(characterA, characterB):
            if not silent:
                print('skill combo should be {}_{} but is {}'.format(characterA, characterB, combo))
            return True
        if unique_part > 1:
            if not silent:
                print("There is more than 1 unique part")
            return True
        if self.spread[rarity] != count_part:
            if not silent:
                print('Amount of skill part should be {} but is {}'.format(self.spread[rarity], count_part))
            return True

        for part in overrides:
            for part2 in overrides:
                if part == part2:
                    continue
                cluster = self.clusters[part]
                if part2 in cluster:
                    if not silent:
                        print('{} is a passive stat in the same cluster as {}'.format(part, part2))
                    return True

        skill_counts = {}
        for skill in skills:
            if characterA == "Knight" or characterB == "Knight":
                print("")
            t = self.combos[characterA][characterB]
            possible_skills = [
                "{}_{}".format(characterA, t[0]),
                "{}_{}".format(characterA, t[1]),
                "{}_{}".format(characterB, t[2]),
            ]
            if skill not in skill_counts:
                skill_counts[skill] = 1
            else:
                skill_counts[skill] += 1

            if skill not in possible_skills:
                if not silent:
                    print("{} should not be present with {} as primary and {} as secondary".format(skill, characterA, characterB))
                return True

        for key, value in skill_counts.items():
            character = key.split("_")[0]
            passive = "Passive_{}".format(key.split("Passive_")[1])
            index = self.get_index_passive_raw(character, passive)

            if not self.can_roll[character][index]:
                if not silent:
                    print("{} should not be present on a mod class for {}".format(key, character))
                return True

            a = self.levels[character]
            if value > self.levels[character][index]:
                if not silent:
                    print("{} can be max level {} but is {}".format(key, self.levels[character][index], value))
                return True
        return False

    def get_index_passive_raw(self, character, passive):
        for i, key in enumerate(self.passives_raw[character]):
            value = self.passives_raw[character][key]
            if value == passive:
                return i
        return None

    def missing_dependant(self, balance, parts_target):
        whatihave = {}
        whatineed = {}
        for part in parts_target:
            part_name = part.replace('\\', '/')
            cat = self.get_category(balance, part_name.split(".")[-1])
            if cat not in whatihave:
                whatihave[cat] = []
            whatihave[cat].append(part.split(".")[0])
            dependencies = self.get_dependant(balance, part_name.split(".")[0])
            for elm in dependencies:
                cat = self.get_category(balance, elm.replace('\\', '/').split('/')[-1])
                if not cat:
                    continue
                if cat not in whatineed:
                    whatineed[cat] = []
                whatineed[cat].append(elm.split(".")[-1])

        # return True if one value of whatihave is in whatineed for each key
        for key, value in whatineed.items():
            if key not in whatihave:
                return True
            found = False
            for elm in value:
                if elm in whatihave[key]:
                    found = True
                    break
            if not found:
                print("Missing dependency {} for {}".format(elm, key))
                return True
        return False

    def has_excluders(self, balance, parts_target):
        whatihave = {}
        whatifear = {}
        for part in parts_target:
            part_name = part.replace('\\', '/')
            cat = self.get_category(balance, part_name.split(".")[-1])
            if cat not in whatihave:
                whatihave[cat] = []
            whatihave[cat].append(part.split(".")[0])
            excluders = self.get_excluders(balance, part_name.split(".")[0])
            for elm in excluders:
                cat = self.get_category(balance, elm.replace('\\', '/').split('/')[-1])
                if not cat:
                    continue
                if cat not in whatifear:
                    whatifear[cat] = []
                whatifear[cat].append(elm.split(".")[-1])

        for key, value in whatifear.items():
            if key not in whatihave:
                continue
            not_found = True
            for elm in value:
                if elm in whatihave[key]:
                    not_found = False
                    print("{} is in conflict as {}".format(elm, key))
                    break
            if not not_found:
                return True
        return False

        #     for partB in parts_target:
        #         if partB in excluders:
        #             print('{} is a part excluded by {}'.format(partB, part))
        #             return True
        # return False

    # def has_dependant(self, balance, parts_target):
    #     for part in parts_target:
    #         dependant = self.get_dependant(balance, part)
    #         if len(dependant) == 0:
    #             continue
    #
    #         dep = False
    #         for partB in parts_target:
    #             if partB in dependant:
    #                 dep = True
    #                 break
    #         if not dep:
    #             print('{} is missing a depencies in {}'.format(part, ', '.join(dependant)))
    #             return False
    #     return True


class Item:
    def __init__(self, row, type):
        if type == "GUNS":
            self.manufacturer = row[0]
            self.gun_type = row[1]
            self.rarity = row[2]
            self.balance_long = row[3]
            self.balance = self.balance_long.replace('\\', '/').split('/')[-1]
            self.category = row[4]
            self.min_parts = int(row[5])
            self.max_parts = int(row[6])
            self.weight = float(row[7])
            self.parts = row[8] if row[8] != "None" else None
            self.dependencies = [e.strip() for e in row[9].split(',')] if row[9] != "" else []
            self.excluders = [e.strip() for e in row[10].split(',')] if row[10] != "" else []
        elif type == "SHIELDS":
            self.manufacturer = row[0]
            self.rarity = row[1]
            self.balance_long = row[2]
            self.balance = self.balance_long.replace('\\', '/').split('/')[-1]
            self.category = row[3]
            self.min_parts = int(row[4])
            self.max_parts = int(row[5])
            self.weight = float(row[6])
            self.parts = row[7] if row[7] != "None" else None
            self.dependencies = [e.strip() for e in row[8].split(',')] if row[8] != "" else []
            self.excluders = [e.strip() for e in row[9].split(',')] if row[9] != "" else []
        elif type == "PAULDRONS":
            self.manufacturer = row[0]
            self.rarity = row[1]
            self.balance_long = row[2]
            self.balance = self.balance_long.replace('\\', '/').split('/')[-1]
            self.category = row[3]
            self.min_parts = int(row[4])
            self.max_parts = int(row[5])
            self.weight = float(row[6])
            self.parts = row[7] if row[7] != "None" else None
            self.dependencies = [e.strip() for e in row[8].split(',')] if row[8] != "" else []
            self.excluders = [e.strip() for e in row[9].split(',')] if row[9] != "" else []
        elif type == 'SPELLS':
            self.name = row[0]
            self.type = row[1]
            self.rarity = row[2]
            self.balance_long = row[3]
            self.balance = self.balance_long.replace('\\', '/').split('/')[-1]
            self.category = row[4]
            self.min_parts = int(row[5])
            self.max_parts = int(row[6])
            self.weight = float(row[7])
            self.parts = row[8] if row[8] != "None" else None
            self.dependencies = [e.strip() for e in row[9].split(',')] if row[9] != "" else []
            self.excluders = [e.strip() for e in row[10].split(',')] if row[10] != "" else []
        elif type == 'RINGS':
            self.name = row[0]
            self.type = row[1]
            self.rarity = row[2]
            self.balance_long = row[3]
            self.balance = self.balance_long.replace('\\', '/').split('/')[-1]
            self.category = row[4]
            self.min_parts = int(row[5])
            self.max_parts = int(row[6])
            self.weight = float(row[7])
            self.parts = row[8] if row[8] != "None" else None
            self.dependencies = [e.strip() for e in row[9].split(',')] if row[9] != "" else []
            self.excluders = [e.strip() for e in row[10].split(',')] if row[10] != "" else []
        elif type == 'MELEE':
            self.name = row[0]
            self.type = row[1]
            self.rarity = row[2]
            self.balance_long = row[3]
            self.balance = self.balance_long.replace('\\', '/').split('/')[-1]
            self.category = row[4]
            self.min_parts = int(row[5])
            self.max_parts = int(row[6])
            self.weight = float(row[7])
            self.parts = row[8] if row[8] != "None" else None
            self.dependencies = [e.strip() for e in row[9].split(',')] if row[9] != "" else []
            self.excluders = [e.strip() for e in row[10].split(',')] if row[10] != "" else []
        elif type == 'AMULETS':
            self.name = row[0]
            self.rarity = row[1]
            self.balance_long = row[2]
            self.balance = self.balance_long.replace('\\', '/').split('/')[-1]
            self.category = row[3]
            self.min_parts = int(row[4])
            self.max_parts = int(row[5])
            self.weight = float(row[6])
            self.parts = row[7] if row[7] != "None" else None
            self.dependencies = [e.strip() for e in row[8].split(',')] if row[8] != "" else []
            self.excluders = [e.strip() for e in row[9].split(',')] if row[9] != "" else []
        else:
            self.manufacturer = row[0]
            self.rarity = row[1]
            self.balance_long = row[3]
            self.balance = self.balance_long.replace('\\', '/').split('/')[-1]
            self.category = row[3]
            self.min_parts = int(row[4])
            self.max_parts = int(row[5])
            self.weight = float(row[6])
            self.parts = row[7] if row[7] != "None" else None
            self.dependencies = [e.strip() for e in row[8].split(',')] if row[8] != "" else []
            self.excluders = [e.strip() for e in row[9].split(',')] if row[9] != "" else []
