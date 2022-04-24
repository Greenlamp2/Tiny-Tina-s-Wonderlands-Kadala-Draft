import tkinter as tk

from ttw_save_editor.WonderlandsSave import WonderlandsSave
from ttw_save_editor.constants import MELEE, WEAPON1, WEAPON2, WEAPON3, WEAPON4, RING1, SHIELD, Amulet, RING2, \
    Pauldrons, SPELL, slot_to_eng, MONEY
from ui import menu, kadala
from tkinter import filedialog as fd


class Kadala:
    def __init__(self):
        self.ui = None
        self.save_from = None
        self.save_path_from = None
        self.new_save = None

        self.slot_from = None

        self.name = None
        self.gold = 0
        self.cost = 250000
        self.gambled = 0
        self.equips = {
            "melee": "None",
            "w1": "None",
            "w2": "None",
            "w3": "None",
            "w4": "None",
            "ring1": "None",
            "ring2": "None",
            "amulet": "None",
            "shield": "None",
            "mod": "None",
            "spell": "None",
        }

    def set_slot(self, slot_name):
        self.slot_from = slot_name
        self.update_ui()

    def get_equips(self):
        a = self.save_from.get_item_at(MELEE).balance_short
        self.equips["melee"] = self.save_from.get_item_at(MELEE).balance_short.split("_")[-1]
        self.equips["w1"] = self.save_from.get_item_at(WEAPON1).balance_short.split("BALANCE_M")[-1]
        self.equips["w2"] = self.save_from.get_item_at(WEAPON2).balance_short.split("BALANCE_M")[-1]
        self.equips["w3"] = self.save_from.get_item_at(WEAPON3).balance_short.split("BALANCE_M")[-1]
        self.equips["w4"] = self.save_from.get_item_at(WEAPON4).balance_short.split("BALANCE_M")[-1]

    def load_save_from(self, path):
        self.save_from = WonderlandsSave(path)
        self.name = self.save_from.get_char_name()
        self.gold = self.save_from.get_currency(MONEY)
        self.get_equips()
        self.update_ui()

    def load_save(self):
        self.save_path_from = menu.open()
        self.load_save_from(self.save_path_from)

    def save_to(self):
        f = fd.asksaveasfile(mode='w', filetypes=[('Save File', '*.sav')])
        if f is None:
            return
        self.new_save.save_to(f.name)

    def gamble(self):
        self.ui.button_gamble.configure(state="disabled")
        target = self.save_from.get_item_at(self.slot_from)
        success = False
        while not success:
            try:
                self.save_from.generate_random_item(target, 1)
                self.gambled = self.gambled + 1
                self.ui.button_gamble.configure(state="normal")
                self.update_ui()
                success = True
            except:
                pass

    def start_gui(self):
        global root
        root = tk.Tk()
        root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
        global _top1, _w1
        _top1 = root
        _w1 = kadala.Toplevel1(self, _top1)
        root.mainloop()

    def proceed(self):
        self.new_save = self.save_to
        self.new_save.clone_PT(self.save_from)
        self.save_as()

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
        self.new_save.transfertEnchant(self.slot_to, self.slot_from)
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

        self.ui.label_melee.configure(text=self.equips["melee"])
        self.ui.label_w1.configure(text=self.equips["w1"])
        self.ui.label_w2.configure(text=self.equips["w2"])
        self.ui.label_w3.configure(text=self.equips["w3"])
        self.ui.label_w4.configure(text=self.equips["w4"])
        self.ui.label_r1.configure(text=self.equips["ring1"])
        self.ui.label_r2.configure(text=self.equips["ring2"])
        self.ui.label_amulet.configure(text=self.equips["amulet"])
        self.ui.label_shield.configure(text=self.equips["shield"])
        self.ui.label_mod.configure(text=self.equips["mod"])
        self.ui.label_spell.configure(text=self.equips["spell"])

        self.lock_all()


    def lock_all(self):
        if not self.save_from or self.slot_from != None:
            self.ui.Button4.configure(state="disabled")
            self.ui.Button4_1.configure(state="disabled")
            self.ui.Button4_1_1.configure(state="disabled")
            self.ui.Button4_1_1_1.configure(state="disabled")
            self.ui.Button4_1_1_1_1.configure(state="disabled")
            self.ui.Button4_1_1_1_1_1.configure(state="disabled")
            self.ui.Button4_1_1_1_1_1_1.configure(state="disabled")
            self.ui.Button4_1_1_1_1_1_1_1.configure(state="disabled")
            self.ui.Button4_1_1_1_1_1_1_1_1.configure(state="disabled")
            self.ui.Button4_1_1_1_1_1_1_1_1_1.configure(state="disabled")
            self.ui.Button4_1_1_1_1_1_1_1_1_1_1.configure(state="disabled")
        else:
            self.ui.Button4.configure(state="normal")
            self.ui.Button4_1.configure(state="normal")
            self.ui.Button4_1_1.configure(state="normal")
            self.ui.Button4_1_1_1.configure(state="normal")
            self.ui.Button4_1_1_1_1.configure(state="normal")
            self.ui.Button4_1_1_1_1_1.configure(state="normal")
            self.ui.Button4_1_1_1_1_1_1.configure(state="normal")
            self.ui.Button4_1_1_1_1_1_1_1.configure(state="normal")
            self.ui.Button4_1_1_1_1_1_1_1_1.configure(state="normal")
            self.ui.Button4_1_1_1_1_1_1_1_1_1.configure(state="normal")
            self.ui.Button4_1_1_1_1_1_1_1_1_1_1.configure(state="normal")

        if self.slot_from != None:
            self.ui.Button1.configure(state="normal")
        else:
            self.ui.Button1.configure(state="disabled")

        if self.save_from and self.slot_from != None:
            self.ui.button_gamble.configure(state="normal")




if __name__ == '__main__':
    editor = Kadala()
    editor.start_gui()
