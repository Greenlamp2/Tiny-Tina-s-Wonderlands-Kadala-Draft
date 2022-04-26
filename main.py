import os.path
import shutil
import tkinter as tk
from datetime import datetime

from Items import Items
from ttw_save_editor import WonderlandsItem
from ttw_save_editor.WonderlandsSave import WonderlandsSave
from ttw_save_editor.constants import MELEE, WEAPON1, WEAPON2, WEAPON3, WEAPON4, RING1, SHIELD, Amulet, RING2, \
    Pauldrons, SPELL, slot_to_eng, MONEY
from ui import menu, kadala
from tkinter import filedialog as fd

from ui.kadala import ToolTip


class Kadala:
    def __init__(self):
        self.ui = None
        self.save_from = None
        self.save_path_from = None
        self.new_save = None

        self.slot_from = None

        self.name = None
        self.gold = 0
        self.cost = 150000
        self.gambled = 0
        self.equips = {
            "melee": {
                "name": "None",
                "enabled": "disabled",
            },
            "w1": {
                "name": "None",
                "enabled": "disabled",
            },
            "w2": {
                "name": "None",
                "enabled": "disabled",
            },
            "w3": {
                "name": "None",
                "enabled": "disabled",
            },
            "w4": {
                "name": "None",
                "enabled": "disabled",
            },
            "r1": {
                "name": "None",
                "enabled": "disabled",
            },
            "r2": {
                "name": "None",
                "enabled": "disabled",
            },
            "amulet": {
                "name": "None",
                "enabled": "disabled",
            },
            "shield": {
                "name": "None",
                "enabled": "disabled",
            },
            "mod": {
                "name": "None",
                "enabled": "disabled",
            },
            "spell": {
                "name": "None",
                "enabled": "disabled",
            },
        }
        self.db = Items()
        self.db.load('export/gun_balances_long.csv', "GUNS")
        self.db.load('export/shield_balances_long.csv', "SHIELDS")
        self.db.load('export/pauldron_balances_long.csv', "PAULDRONS")
        self.db.load('export/spell_balances_long.csv', "SPELLS")
        self.db.load('export/ring_balances_long.csv', "RINGS")
        self.db.load('export/amulet_balances_long.csv', "AMULETS")
        self.db.load('export/melee_balances_long.csv', "MELEE")

    def set_slot(self, slot_name):
        self.slot_from = slot_name
        self.update_ui()

    def backup_save(self):
        target_to_save = self.save_path_from
        if not os.path.isdir("save_backups/"):
            os.mkdir("save_backups/")
        dt = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
        folder = "save_backups/{}/".format(dt)
        if not os.path.isdir(folder):
            os.mkdir(folder)
        filename = target_to_save.split("/")[-1]
        final = "{}{}".format(folder, filename)
        shutil.copyfile(target_to_save, final)


    def get_equips(self):
        melee = self.save_from.get_item_at(MELEE)
        self.equips["melee"]["name"] = melee.balance_short.split("_")[-1]
        test = "_Unique" in melee.balance
        self.equips["melee"]["enable"] = "normal" if "_Unique" in melee.balance else "normal"

        w1 = self.save_from.get_item_at(WEAPON1)
        self.equips["w1"]["name"] = w1.balance_short.split("Balance_")[-1]
        self.equips["w1"]["enable"] = "normal" if "_Unique" in w1.balance else "normal"

        w2 = self.save_from.get_item_at(WEAPON2)
        self.equips["w2"]["name"] = w2.balance_short.split("Balance_")[-1]
        self.equips["w2"]["enable"] = "normal" if "_Unique" in w2.balance else "normal"

        w3 = self.save_from.get_item_at(WEAPON3)
        self.equips["w3"]["name"] = w3.balance_short.split("Balance_")[-1]
        self.equips["w3"]["enable"] = "normal" if "_Unique" in w3.balance else "normal"

        w4 = self.save_from.get_item_at(WEAPON4)
        self.equips["w4"]["name"] = w4.balance_short.split("Balance_")[-1]
        self.equips["w4"]["enable"] = "normal" if "_Unique" in w4.balance else "normal"

        r1 = self.save_from.get_item_at(RING1)
        self.equips["r1"]["name"] = r1.balance_short.split("Balance_")[-1]
        self.equips["r1"]["enable"] = "normal" if "_Unique" in r1.balance else "normal"

        r2 = self.save_from.get_item_at(RING2)
        self.equips["r2"]["name"] = r2.balance_short.split("Balance_")[-1]
        self.equips["r2"]["enable"] = "normal" if "_Unique" in r2.balance else "normal"

        shield = self.save_from.get_item_at(SHIELD)
        self.equips["shield"]["name"] = shield.balance_short.split("Balance_")[-1]
        self.equips["shield"]["enable"] = "normal" if "_Unique" in shield.balance else "normal"

        amulet = self.save_from.get_item_at(Amulet)
        self.equips["amulet"]["name"] = amulet.balance_short.split("Balance_")[-1]
        self.equips["amulet"]["enable"] = "normal" if "_Unique" in amulet.balance else "normal"

        mod = self.save_from.get_item_at(Pauldrons)
        self.equips["mod"]["name"] = mod.balance_short.split("Balance_")[-1]
        self.equips["mod"]["enable"] = "normal" if "_Unique" in mod.balance else "normal"

        spell = self.save_from.get_item_at(SPELL)
        self.equips["spell"]["name"] = spell.balance_short.split("Balance_")[-1]
        self.equips["spell"]["enable"] = "normal" if "_Unique" in spell.balance else "normal"

    def load_save_from(self, path):
        self.save_from = WonderlandsSave(path)
        self.name = self.save_from.get_char_name()
        self.gold = self.save_from.get_currency(MONEY)
        self.get_equips()
        self.update_ui()

    def load_save(self):
        self.save_path_from = menu.open()
        self.backup_save()
        self.load_save_from(self.save_path_from)

    def can_gamble(self):
        return self.gold >= self.cost

    def save_to(self):
        self.new_save = self.save_from
        self.ui.label_status.configure(text="Success !")
        f = fd.asksaveasfile(mode='w', filetypes=[('Save File', '*.sav')])
        if f is None:
            return
        self.new_save.save_to(f.name)

    def gamble(self):
        if self.can_gamble():
            self.ui.button_gamble.configure(state="disabled")
            target = self.save_from.get_item_at(self.slot_from)
            success = False
            self.gold -= self.cost
            while not success:
                self.save_from.generate_random_item(self.db, target, 1)
                self.gambled = self.gambled + 1
                self.ui.button_gamble.configure(state="normal")
                self.update_ui()
                success = True
            self.save_from.set_currency(MONEY, self.gold)

    def start_gui(self):
        global root
        root = tk.Tk()
        root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
        global _top1, _w1
        _top1 = root
        _w1 = kadala.Toplevel1(self, _top1)
        root.mainloop()

    def select_offhand(self):
        self.set_slot(MELEE)

    def select_weapon_1(self):
        self.set_slot(WEAPON1)

    def select_weapon_2(self):
        self.set_slot(WEAPON2)

    def select_weapon_3(self):
        self.set_slot(WEAPON3)

    def select_weapon_4(self):
        self.set_slot(WEAPON4)

    def select_ring_1(self):
        self.set_slot(RING1)

    def select_shield(self):
        self.set_slot(SHIELD)

    def select_amulet(self):
        self.set_slot(Amulet)

    def select_ring_2(self):
        self.set_slot(RING2)

    def select_mod(self):
        self.set_slot(Pauldrons)

    def select_spell(self):
        self.set_slot(SPELL)

    def del_from(self):
        self.slot_from = None
        self.update_ui()

    def del_to(self):
        self.slot_to = None
        self.update_ui()

    def transfer(self):
        self.new_save = self.save_from
        self.save_as()
        self.ui.label_status.configure(text="Success !")

    def update_ui(self):
        if self.slot_from != None:
            from_name = slot_to_eng[self.slot_from]
            self.ui.label_from.configure(text=from_name)
        else:
            self.ui.label_from.configure(text="None")

        if self.name:
            self.ui.text_name.set(self.name)
        else:
            self.ui.text_name.set("")

        self.ui.text_gold.set(self.gold)
        self.ui.text_price.set(self.cost)
        self.ui.label_gambled.set(self.gambled)

        if self.slot_from != None:
            self.ui.label_status.configure(text="Ready !")
        else:
            self.ui.label_status.configure(text="Waiting...")

        if self.save_from:
            self.ui.label_melee.configure(text=self.equips["melee"]["name"])
            self.ui.label_w1.configure(text=self.equips["w1"]["name"])
            self.ui.label_w2.configure(text=self.equips["w2"]["name"])
            self.ui.label_w3.configure(text=self.equips["w3"]["name"])
            self.ui.label_w4.configure(text=self.equips["w4"]["name"])
            self.ui.label_r1.configure(text=self.equips["r1"]["name"])
            self.ui.label_r2.configure(text=self.equips["r2"]["name"])
            self.ui.label_amulet.configure(text=self.equips["amulet"]["name"])
            self.ui.label_shield.configure(text=self.equips["shield"]["name"])
            self.ui.label_mod.configure(text=self.equips["mod"]["name"])
            self.ui.label_spell.configure(text=self.equips["spell"]["name"])

            ToolTip(self.ui.label_melee, "TkDefaultFont", self.equips["melee"]["name"])
            ToolTip(self.ui.label_w1, "TkDefaultFont", self.equips["w1"]["name"])
            ToolTip(self.ui.label_w2, "TkDefaultFont", self.equips["w2"]["name"])
            ToolTip(self.ui.label_w3, "TkDefaultFont", self.equips["w3"]["name"])
            ToolTip(self.ui.label_w4, "TkDefaultFont", self.equips["w4"]["name"])
            ToolTip(self.ui.label_r1, "TkDefaultFont", self.equips["r1"]["name"])
            ToolTip(self.ui.label_r2, "TkDefaultFont", self.equips["r2"]["name"])
            ToolTip(self.ui.label_amulet, "TkDefaultFont", self.equips["amulet"]["name"])
            ToolTip(self.ui.label_shield, "TkDefaultFont", self.equips["shield"]["name"])
            ToolTip(self.ui.label_mod, "TkDefaultFont", self.equips["mod"]["name"])
            ToolTip(self.ui.label_spell, "TkDefaultFont", self.equips["spell"]["name"])

        self.lock_all()


    def lock_all(self):
        if self.save_from:
            self.ui.button_browse.configure(state="disabled")
        self.ui.Button4.configure(state=self.equips["melee"]["enable"])
        self.ui.Button4_1.configure(state=self.equips["w1"]["enable"])
        self.ui.Button4_1_1.configure(state=self.equips["w2"]["enable"])
        self.ui.Button4_1_1_1.configure(state=self.equips["w3"]["enable"])
        self.ui.Button4_1_1_1_1.configure(state=self.equips["w4"]["enable"])
        self.ui.Button4_1_1_1_1_1.configure(state=self.equips["r1"]["enable"])
        self.ui.Button4_1_1_1_1_1_1.configure(state=self.equips["shield"]["enable"])
        self.ui.Button4_1_1_1_1_1_1_1.configure(state=self.equips["amulet"]["enable"])
        self.ui.Button4_1_1_1_1_1_1_1_1.configure(state=self.equips["r2"]["enable"])
        self.ui.Button4_1_1_1_1_1_1_1_1_1.configure(state=self.equips["mod"]["enable"])
        self.ui.Button4_1_1_1_1_1_1_1_1_1_1.configure(state=self.equips["spell"]["enable"])

        if self.slot_from != None:
            self.ui.Button1.configure(state="normal")
        else:
            self.ui.Button1.configure(state="disabled")

        if self.save_from and self.slot_from != None:
            self.ui.button_save_to.configure(state="normal")

        if self.can_gamble() and self.save_from and self.slot_from != None:
            self.ui.button_gamble.configure(state="normal")
        else:
            self.ui.button_gamble.configure(state="disabled")




if __name__ == '__main__':
    editor = Kadala()
    editor.start_gui()
