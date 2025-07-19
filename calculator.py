import tkinter as tk
import math

def click(event):
    current = str(entry.get())
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "√":
        try:
            result = math.sqrt(float(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "x^y":
        entry.insert(tk.END, "**")
    elif text == "ln":
        try:
            result = math.log(float(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "log":
        try:
            result = math.log10(float(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "sin":
        try:
            result = math.sin(math.radians(float(current)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "cos":
        try:
            result = math.cos(math.radians(float(current)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "tan":
        try:
            result = math.tan(math.radians(float(current)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "π":
        entry.insert(tk.END, str(math.pi))
    elif text == "e":
        entry.insert(tk.END, str(math.e))
    elif text == "x!":
        try:
            result = math.factorial(int(float(current)))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, text)

# Create main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")
root.resizable(False, False)

# Entry widget
entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(pady=20, ipadx=8, ipady=10, fill=tk.X, padx=10)

# Button frame
btn_frame = tk.Frame(root)
btn_frame.pack()

# Button labels
buttons = [
    ["7", "8", "9", "/", "C"],
    ["4", "5", "6", "*", "√"],
    ["1", "2", "3", "-", "x^y"],
    ["0", ".", "=", "+", "x!"],
    ["(", ")", "mod", "π", "e"],
    ["sin", "cos", "tan", "log", "ln"]
]

# Create and place buttons
for row in buttons:
    row_frame = tk.Frame(btn_frame)
    row_frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(row_frame, text=btn_text, font=("Arial", 14), relief=tk.RAISED, borderwidth=2)
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        btn.bind("<Button-1>", click)

# Start the GUI loop
root.mainloop()