from flask import Flask, render_template
import tkinter as tk
#import ImageTk
import random

app = Flask(__name__)

class UWBPositionUI:
    def __init__(self, root):
        self.root = root
        self.root.title("UWB Position Tracking")

        # Annahme: Initialpositionen der UWB-Module
        self.anchor_positions = [(50, 50), (200, 50), (50, 200)]
        self.tag_position = (100, 100)

        # Canvas für die Darstellung mit Bild als Hintergrund
        self.canvas = tk.Canvas(root, width=300, height=300, bg='white')
        self.canvas.pack()

        # Bild als Hintergrund einfügen
        # self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)

        # Zeichne Ankerpunkte
        for x, y in self.anchor_positions:
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='blue')

        # Zeichne Tag-Position
        self.tag_dot = self.canvas.create_oval(self.tag_position[0] - 5, self.tag_position[1] - 5,
                                                self.tag_position[0] + 5, self.tag_position[1] + 5, fill='red')

        # Starte die automatische Aktualisierung
        self.update_positions()

    def update_positions(self):
        # Annahme: Aktualisierte Positionen der UWB-Module erhalten
        # Hier könntest du deine tatsächlichen Live-Daten einfügen
        new_tag_position = (random.randint(0, 300), random.randint(0, 300))

        # Aktualisiere Tag-Position auf der UI
        self.canvas.coords(self.tag_dot, new_tag_position[0] - 5, new_tag_position[1] - 5,
                            new_tag_position[0] + 5, new_tag_position[1] + 5)

        # Speichere die aktualisierte Position für zukünftige Referenzen
        self.tag_position = new_tag_position

        # Setze einen Timer für die nächste Aktualisierung (hier alle 1000 Millisekunden / 1 Sekunde)
        self.root.after(1000, self.update_positions)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lab1.html')
def lab1():
    root = tk.Tk()
    app = UWBPositionUI(root)
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    root.withdraw()  # Verstecke das Tkinter-Fenster
    return render_template('lab1.html')

if __name__ == '__main__':
    app.run(debug=True)
