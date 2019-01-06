#!/usr/bin/env python3



import math

import tkinter as tk
from PIL import Image, ImageTk

import item as production


__img_buffer = []

def load_img(name):
        global __img_buffer
        s = './imgs/%s.png' % name
        print(s)
        img = Image.open(s)
        photo = ImageTk.PhotoImage(img)
        __img_buffer += [photo]
        return photo

class App(tk.Frame):

        def __init__(self, master):
                super().__init__(master)

                self.rowconfigure(0, weight=1, pad=5)
                self.rowconfigure(1, weight=1, pad=5)
                self.columnconfigure(0, weight=1, pad=5)

                self.container_class = tk.Frame()
                self.container_prod = tk.Frame()

                class_c = self.container_class
                prod_c = self.container_prod
                for i in range(0, 2):
                        class_c.rowconfigure(i, weight=0, pad=5)
                for i in range(0, 7):
                        class_c.columnconfigure(i, weight=1, pad=5)


                for i in range(0, 2):
                        prod_c.rowconfigure(i, weight=0, pad=5)
                for i in range(0, 22):
                        prod_c.columnconfigure(i, weight=1, pad=5)



                self._lbl_beggar = tk.Label(class_c, text='Beggar')
                self._lbl_peasant = tk.Label(class_c, text='Peasant')
                self._lbl_citizen = tk.Label(class_c, text='Citizen')
                self._lbl_patrician = tk.Label(class_c, text='Patrician')
                self._lbl_nobleman = tk.Label(class_c, text='Nobleman')
                self._lbl_nomad = tk.Label(class_c, text='Nomad')
                self._lbl_envoy = tk.Label(class_c, text='Envoy')

                self._ent_beggar = tk.Entry(class_c)
                self._ent_peasant = tk.Entry(class_c)
                self._ent_citizen = tk.Entry(class_c)
                self._ent_patrician = tk.Entry(class_c)
                self._ent_nobleman = tk.Entry(class_c)
                self._ent_nomad = tk.Entry(class_c)
                self._ent_envoy = tk.Entry(class_c)

                self._lbl_fish = tk.Label(prod_c, image=load_img('fish'))
                self._lbl_spices = tk.Label(prod_c, image=load_img('spices'))
                self._lbl_bread = tk.Label(prod_c, image=load_img('bread'))
                self._lbl_meat = tk.Label(prod_c, image=load_img('meat'))
                self._lbl_cider = tk.Label(prod_c, image=load_img('cider'))
                self._lbl_beer = tk.Label(prod_c, image=load_img('beer'))
                self._lbl_wine = tk.Label(prod_c, image=load_img('wine'))
                self._lbl_linen = tk.Label(prod_c, image=load_img('linen'))
                self._lbl_leather = tk.Label(prod_c, image=load_img('leather'))
                self._lbl_fur = tk.Label(prod_c, image=load_img('fur'))
                self._lbl_brocade = tk.Label(prod_c, image=load_img('brocade'))
                self._lbl_books = tk.Label(prod_c, image=load_img('books'))
                self._lbl_candles = tk.Label(prod_c, image=load_img('candles'))
                self._lbl_glasses = tk.Label(prod_c, image=load_img('glasses'))
                self._lbl_dates = tk.Label(prod_c, image=load_img('dates'))
                self._lbl_milk = tk.Label(prod_c, image=load_img('milk'))
                self._lbl_carpets = tk.Label(prod_c, image=load_img('carpets'))
                self._lbl_coffee = tk.Label(prod_c, image=load_img('coffee'))
                self._lbl_pearl_necklaces = tk.Label(prod_c, image=load_img('pearl_necklaces'))
                self._lbl_parfum = tk.Label(prod_c, image=load_img('parfum'))
                self._lbl_marzipan = tk.Label(prod_c, image=load_img('marzipan'))

                self._ent_fish = tk.Entry(prod_c)
                self._ent_spices = tk.Entry(prod_c)
                self._ent_bread = tk.Entry(prod_c)
                self._ent_meat = tk.Entry(prod_c)
                self._ent_cider = tk.Entry(prod_c)
                self._ent_beer = tk.Entry(prod_c)
                self._ent_wine = tk.Entry(prod_c)
                self._ent_linen = tk.Entry(prod_c)
                self._ent_leather = tk.Entry(prod_c)
                self._ent_fur = tk.Entry(prod_c)
                self._ent_brocade = tk.Entry(prod_c)
                self._ent_books = tk.Entry(prod_c)
                self._ent_candles = tk.Entry(prod_c)
                self._ent_glasses = tk.Entry(prod_c)
                self._ent_dates = tk.Entry(prod_c)
                self._ent_milk = tk.Entry(prod_c)
                self._ent_carpets = tk.Entry(prod_c)
                self._ent_coffee = tk.Entry(prod_c)
                self._ent_pearl_necklaces = tk.Entry(prod_c)
                self._ent_parfum = tk.Entry(prod_c)
                self._ent_marzipan = tk.Entry(prod_c)

                self._class_labels = [
                                self._lbl_beggar,
                                self._lbl_peasant,
                                self._lbl_citizen,
                                self._lbl_patrician,
                                self._lbl_nobleman,
                                self._lbl_nomad,
                                self._lbl_envoy,
                ]
                self._prod_labels = [
                                self._lbl_fish,
                                self._lbl_spices,
                                self._lbl_bread,
                                self._lbl_meat,
                                self._lbl_cider,
                                self._lbl_beer,
                                self._lbl_wine,
                                self._lbl_linen,
                                self._lbl_leather,
                                self._lbl_fur,
                                self._lbl_brocade,
                                self._lbl_books,
                                self._lbl_candles,
                                self._lbl_glasses,
                                self._lbl_dates,
                                self._lbl_milk,
                                self._lbl_carpets,
                                self._lbl_coffee,
                                self._lbl_pearl_necklaces,
                                self._lbl_parfum,
                                self._lbl_marzipan,
                ]
                self._class_entries = [
                                self._ent_beggar,
                                self._ent_peasant,
                                self._ent_citizen,
                                self._ent_patrician,
                                self._ent_nobleman,
                                self._ent_nomad,
                                self._ent_envoy,
                ]
                self._prod_entries = [
                                self._ent_fish,
                                self._ent_spices,
                                self._ent_bread,
                                self._ent_meat,
                                self._ent_cider,
                                self._ent_beer,
                                self._ent_wine,
                                self._ent_linen,
                                self._ent_leather,
                                self._ent_fur,
                                self._ent_brocade,
                                self._ent_books,
                                self._ent_candles,
                                self._ent_glasses,
                                self._ent_dates,
                                self._ent_milk,
                                self._ent_carpets,
                                self._ent_coffee,
                                self._ent_pearl_necklaces,
                                self._ent_parfum,
                                self._ent_marzipan,
                ]


                self.master.bind('<Key>', self.callback_self_generic_key)
                for ent in self._class_entries:
                        ent.insert(0, '0')
                        ent.bind('<FocusIn>', self.callback_entry_focus_in)
                        ent.bind('<FocusOut>', self.callback_entry_focus_out)
                        ent.bind('<Return>', self.callback_entry_focus_out)

                for ent in self._prod_entries:
                        ent.configure(state='readonly', takefocus=False)
                class_c.grid(row=0, column=0, sticky='NESW')
                prod_c.grid(row=1, column=0, sticky='NESW')

                for lbl, cnt in zip(self._class_labels, range(len(self._class_labels))):
                        lbl.grid(row=0, column=cnt)

                for ent, cnt in zip(self._class_entries, range(len(self._class_entries))):
                        ent.grid(row=1, column=cnt)

                for lbl, cnt in zip(self._prod_labels, range(len(self._prod_labels))):
                        lbl.grid(row=0, column=cnt)

                for ent, cnt in zip(self._prod_entries, range(len(self._prod_entries))):
                        ent.configure(width=5)
                        ent.grid(row=1, column=cnt)


                self._production_chains = [
                                production.FISH,
                                production.SPICES,
                                production.BREAD,
                                production.MEAT,
                                production.CIDER,
                                production.BEER,
                                production.WINE,
                                production.LINEN,
                                production.LEATHER,
                                production.FUR,
                                production.BROCADE,
                                production.BOOKS,
                                production.CANDLES,
                                production.GLASSES,
                                production.DATES,
                                production.MILK,
                                production.CARPET,
                                production.COFFEE,
                                production.PEARL_NECKLACE,
                                production.PARFUM,
                                production.MARZIPAN,
                ]

        def focus(self):
                self.master.focus()

        def callback_self_generic_key(self, evt=None):
                print(evt)
                if evt.keysym == 'Escape':
                        self.focus()

        def callback_entry_focus_in(self, evt=None):
                evt.widget.selection_range(0, tk.END)

        def callback_entry_focus_out(self, evt=None):
                print(evt)
                try:
                        int(evt.widget.get())
                except ValueError:
                        evt.widget.delete(0, tk.END)
                        evt.widget.insert(0, '0')
                self.callback_upd_values(evt)

        def callback_upd_values(self, evt=None):
                inhabs = [
                                (production.InhabitantClass.BEGGAR, int(self._ent_beggar.get())),
                                (production.InhabitantClass.PEASANT, int(self._ent_peasant.get())),
                                (production.InhabitantClass.CITIZEN, int(self._ent_citizen.get())),
                                (production.InhabitantClass.PATRICIAN, int(self._ent_patrician.get())),
                                (production.InhabitantClass.NOBLEMAN, int(self._ent_nobleman.get())),
                                (production.InhabitantClass.NOMAD, int(self._ent_nomad.get())),
                                (production.InhabitantClass.ENVOY, int(self._ent_envoy.get())),
                ]
                for i in range(0, len(self._prod_entries)):
                        val = self._production_chains[i].get_prod_building_percent(inhabs)
                        if val < 0:
                                continue
                        val *= 100
                        val = math.ceil(val)
                        val /= 100
                        self._prod_entries[i].configure(state=tk.NORMAL)
                        self._prod_entries[i].delete(0, tk.END)
                        self._prod_entries[i].insert(0, '%0.2f' % val)
                        self._prod_entries[i].configure(state='readonly')


if __name__ == '__main__':
        master = tk.Tk()
        app = App(master)
        app.mainloop()


