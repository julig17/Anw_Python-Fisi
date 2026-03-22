import tkinter as tk
import time

# -----------------------------
# Hauptfenster erstellen
# -----------------------------
root = tk.Tk()
root.title("Digitale Uhr")
root.geometry("400x200")
root.resizable(False, False)

# -----------------------------
# Label für die Uhrzeit
# -----------------------------
clock_label = tk.Label(
    root,
    font=("Arial", 40),
    fg="lime",
    bg="black"
)
clock_label.pack(expand=True, fill="both")

# -----------------------------
# Uhr-Update-Funktion
# -----------------------------
def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    
    # Scheduler: ruft die Funktion nach 1000 ms erneut auf
    root.after(1000, update_clock)

# -----------------------------
# Start der Uhr
# -----------------------------
update_clock()

# -----------------------------
# Event-Loop starten
# -----------------------------
root.mainloop()