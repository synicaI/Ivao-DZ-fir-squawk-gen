
import tkinter as tk
from tkinter import ttk
import random
import math
from datetime import datetime

APP_NAME = "DAAA - ALGER FIR SQUAWK GENERATOR MADE BY 735475"

THEME_BG = "#020617"
ACCENT_GREEN = "#00ff99"

BANALIZED_CODES = ["7000"]


SQUAWK_MAP = {

    "DAAG": {
        "DEP": [(4201,4277)],
        "ARR": [(4401,4437)],
        "APP": [(4440,4477)],
        "VFR": [(1601,1677)]
    },

    "DAAS": {
        "DEP": [(4201,4277)],
        "ARR": [(4401,4437)],
        "APP": [(4440,4477)],
        "VFR": [(2601,2677)]
    },

    "DAAE": {
        "DEP": [(4201,4277)],
        "ARR": [(4401,4437)],
        "APP": [(4440,4477)],
        "VFR": [(3201,3277)]
    },

    "SECTOR ALGER": {
        "OVERFLIGHT": [(4201,4277)],
        "TRANSIT": [(4401,4437)]
    },

    "SECTOR EAST": {
        "OVERFLIGHT": [(4201,4277)],
        "TRANSIT": [(4401,4437)]
    },

    "SECTOR WEST": {
        "OVERFLIGHT": [(4201,4277)],
        "TRANSIT": [(4401,4437)]
    },

    "SECTOR SAHARA": {
        "OVERFLIGHT": [(4201,4277)],
        "TRANSIT": [(4401,4437)]
    },

    "LOCAL": {
        "LOCAL FLIGHT": [(0,0),(60,67)]
    }
}



class ATCEngine:

    def __init__(self):

        self.active_flights = {}

    def get_available_code(self, airport, mission):

        ranges = SQUAWK_MAP.get(airport, {}).get(mission, [])

        all_codes = []

        for r in ranges:
            for c in range(r[0], r[1] + 1):
                all_codes.append(f"{c:04d}")

        used = [v["sqk"] for v in self.active_flights.values()]

        free = [c for c in all_codes if c not in used]

        if free:
            return random.choice(free)

        return None

    def add_flight(self, cs, ac, ap, mission):

        code = self.get_available_code(ap, mission)

        if code:

            self.active_flights[cs] = {

                "cs": cs,
                "ac": ac,
                "ap": ap,
                "type": mission,
                "sqk": code,
                "time": datetime.now().strftime("%H:%M")
            }

            return code

        return None



class RadarApp:

    def __init__(self, root):

        self.root = root
        self.engine = ATCEngine()

        root.title(APP_NAME)
        root.geometry("1300x900")
        root.configure(bg=THEME_BG)

        self.create_widgets()

        self.animate_radar()
        self.update_clock()

    def create_widgets(self):

        header = tk.Frame(self.root,bg="#010409")
        header.pack(fill="x")

        tk.Label(
            header,
            text="📡 DAAA ALGER FIR CONTROL",
            fg="#38bdf8",
            bg="#010409",
            font=("Impact",18)
        ).pack(side="left",padx=20)

        self.clock = tk.Label(
            header,
            fg=ACCENT_GREEN,
            bg="#010409",
            font=("Consolas",14)
        )

        self.clock.pack(side="right",padx=20)

        body = tk.Frame(self.root,bg=THEME_BG)
        body.pack(fill="both",expand=True,padx=10,pady=10)

        left = tk.Frame(body,bg=THEME_BG,width=400)
        left.pack(side="left",fill="y")

        self.canvas = tk.Canvas(
            left,
            width=380,
            height=350,
            bg="#000814"
        )

        self.canvas.pack(pady=10)

        box = tk.Frame(left,bg="#0f172a",padx=20,pady=20)
        box.pack(fill="x")

        self.cs=tk.StringVar()
        self.ac=tk.StringVar()
        self.ap=tk.StringVar()
        self.mi=tk.StringVar()

        tk.Label(box,text="CALLSIGN",bg="#0f172a",fg="white").pack(anchor="w")
        tk.Entry(box,textvariable=self.cs).pack(fill="x")

        tk.Label(box,text="AIRCRAFT",bg="#0f172a",fg="white").pack(anchor="w")
        tk.Entry(box,textvariable=self.ac).pack(fill="x")

        tk.Label(box,text="AIRPORT / SECTOR",bg="#0f172a",fg="white").pack(anchor="w")

        self.ap_cb = ttk.Combobox(
            box,
            textvariable=self.ap,
            values=list(SQUAWK_MAP.keys()),
            state="readonly"
        )

        self.ap_cb.pack(fill="x")

        self.mi_cb = ttk.Combobox(box,textvariable=self.mi)

        self.mi_cb.pack(fill="x")

        self.ap_cb.bind("<<ComboboxSelected>>",self.sync_missions)

        tk.Button(
            box,
            text="ACTIVATE FLIGHT",
            command=self.add_flight,
            bg="#38bdf8"
        ).pack(fill="x",pady=10)

        self.sqk=tk.Label(
            left,
            text="----",
            font=("Consolas",60),
            fg=ACCENT_GREEN,
            bg=THEME_BG
        )

        self.sqk.pack()

        right=tk.Frame(body,bg=THEME_BG)
        right.pack(side="right",fill="both",expand=True)

        cols=("CS","AC","SQK","AP","TYPE","TIME")

        self.tree=ttk.Treeview(
            right,
            columns=cols,
            show="headings"
        )

        for c in cols:
            self.tree.heading(c,text=c)

        self.tree.pack(fill="both",expand=True)

    def sync_missions(self,e):

        airport=self.ap.get()

        missions=list(SQUAWK_MAP.get(airport,{}).keys())

        self.mi_cb["values"]=missions

    def add_flight(self):

        code=self.engine.add_flight(
            self.cs.get(),
            self.ac.get(),
            self.ap.get(),
            self.mi.get()
        )

        if code:

            self.sqk.config(text=code)

            self.refresh()

    def refresh(self):

        for i in self.tree.get_children():
            self.tree.delete(i)

        for f in self.engine.active_flights.values():

            self.tree.insert("", "end", values=(

                f["cs"],
                f["ac"],
                f["sqk"],
                f["ap"],
                f["type"],
                f["time"]
            ))

    def update_clock(self):

        self.clock.config(
            text=datetime.now().strftime("%H:%M:%S UTC")
        )

        self.root.after(1000,self.update_clock)

    def animate_radar(self):

        cx=190
        cy=175
        angle=0

        def step():

            nonlocal angle

            self.canvas.delete("all")

            for r in [40,80,120,160]:

                self.canvas.create_oval(
                    cx-r,cy-r,cx+r,cy+r,
                    outline="#00ffaa"
                )

            self.canvas.create_line(cx,0,cx,350,fill="#004f4f")
            self.canvas.create_line(0,cy,380,cy,fill="#004f4f")

            x=cx+170*math.cos(math.radians(angle))
            y=cy+170*math.sin(math.radians(angle))

            self.canvas.create_line(
                cx,cy,x,y,
                fill="#00ff99",
                width=2
            )

            self.canvas.create_text(
                cx,cy+10,
                text="ALGER RADAR",
                fill="#22c55e"
            )

            angle=(angle+4)%360

            self.root.after(40,step)

        step()



root=tk.Tk()

app=RadarApp(root)

root.mainloop()

