import tkinter as tk

from ttw_save_editor.WonderlandsSave import WonderlandsSave
from ttw_save_editor.constants import MELEE, WEAPON1, WEAPON2, WEAPON3, WEAPON4, RING1, SHIELD, Amulet, RING2, \
    Pauldrons, SPELL, slot_to_eng
from ui import menu, kadalaUI


class Kadala:
    def __init__(self):
        self.ui = None
        self.save_from = None
        self.save_path_from = None
        self.new_save = None

        self.slot_from = None
        self.slot_to = None

        self.name = None

    def set_slot(self, slot_name):
        if not self.slot_from:
            self.slot_from = slot_name
        elif not self.slot_to:
            self.slot_to = slot_name
        self.update_ui()

    def load_save_from(self, path):
        self.save_from = WonderlandsSave(path)
        self.name = self.save_from.get_char_name()
        self.update_ui()

    def load_save(self):
        self.save_path_from = menu.open()
        self.load_save_from(self.save_path_from)

    def save_as(self):
        f = fd.asksaveasfile(mode='w', filetypes=[('Save File', '*.sav')])
        if f is None:
            return
        self.new_save.save_to(f.name)

    def start_gui(self):
        global root
        root = tk.Tk()
        root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
        global _top1, _w1
        _top1 = root
        _w1 = kadalaUI.Toplevel1(self, _top1)
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

        if self.slot_to != None:
            to_name = slot_to_eng[self.slot_to]
            self.ui.label_to.configure(text=to_name)
        else:
            self.ui.label_to.configure(text="None")

        if self.name:
            self.ui.text_name.set(self.name)
        else:
            self.ui.text_name.set("")

        if self.slot_from != None and self.slot_to != None:
            self.ui.label_status.configure(text="Ready !")
        else:
            self.ui.label_status.configure(text="Waiting...")

        self.lock_all()


    def lock_all(self):
        if not self.save_from or (self.slot_from != None and self.slot_to != None):
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
            self.ui.Button3.configure(state="disabled")
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

        if self.slot_from != None and self.slot_to!= None:
            self.ui.Button3.configure(state="normal")
        else:
            self.ui.Button3.configure(state="disabled")

        if self.slot_from != None:
            self.ui.Button1.configure(state="normal")
        else:
            self.ui.Button1.configure(state="disabled")

        if self.slot_to != None:
            self.ui.Button1_1.configure(state="normal")
        else:
            self.ui.Button1_1.configure(state="disabled")




if __name__ == '__main__':
    editor = Kadala()
    editor.start_gui()
