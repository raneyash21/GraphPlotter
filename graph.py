import os
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


class SimpleFunctionPlotter:

    def __init__(self, master):
        self.master = master
        master.title("Student Graph Plotter")

        # Top: single expression entry (like a search bar)
        top = ttk.Frame(master)
        top.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        master.columnconfigure(0, weight=1)

        ttk.Label(top, text="Type function in x:").pack(side="left", padx=(0,6))
        self.expr_var = tk.StringVar(value="sin(x)")
        self.entry = ttk.Entry(top, textvariable=self.expr_var, width=60)
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.bind("<Return>", lambda e: self.on_plot())

        # Domain controls (small)
        domain = ttk.Frame(master)
        domain.grid(row=1, column=0, padx=10, pady=6, sticky="w")
        ttk.Label(domain, text="x start").grid(row=0, column=0, padx=4)
        ttk.Label(domain, text="x end").grid(row=0, column=1, padx=4)
        ttk.Label(domain, text="points").grid(row=0, column=2, padx=4)
        self.xstart = tk.StringVar(value="-10")
        self.xend = tk.StringVar(value="10")
        self.points = tk.StringVar(value="500")
        ttk.Entry(domain, textvariable=self.xstart, width=8).grid(row=1, column=0, padx=4)
        ttk.Entry(domain, textvariable=self.xend, width=8).grid(row=1, column=1, padx=4)
        ttk.Entry(domain, textvariable=self.points, width=6).grid(row=1, column=2, padx=4)

        # Buttons
        btns = ttk.Frame(master)
        btns.grid(row=2, column=0, padx=10, pady=8, sticky="w")
        ttk.Button(btns, text="Plot", command=self.on_plot).pack(side="left", padx=6)
        ttk.Button(btns, text="Clear plots", command=self.on_clear).pack(side="left", padx=6)
        ttk.Button(btns, text="Examples", command=self.insert_example).pack(side="left", padx=6)

        # Examples combobox
        example_frame = ttk.Frame(master)
        example_frame.grid(row=3, column=0, padx=10, pady=4, sticky="w")
        ttk.Label(example_frame, text="Quick examples:").pack(side="left", padx=4)
        self.examples = ttk.Combobox(example_frame, values=[
            "sin(x)",
            "cos(x)",
            "tan(x)",
            "x**2",
            "x**3 - 2*x + 3",
            "sin(x) + 0.5*x**2",
            "exp(-x**2)",
            "np.sinc(x)"  # advanced example (np available)
        ], width=48)
        self.examples.pack(side="left", padx=4)
        self.examples.bind("<<ComboboxSelected>>", lambda e: self.expr_var.set(self.examples.get()))

        # Help note
        ttk.Label(master, text="Enter expression using variable x. Allowed functions: sin, cos, tan, exp, log, sqrt, abs, pi, e, np. Press Enter to plot.").grid(row=4, column=0, padx=10, pady=6, sticky="w")

    def insert_example(self):
        val = self.examples.get()
        if val:
            self.expr_var.set(val)

    def on_clear(self):
        plt.close("all")

    def safe_eval(self, expr: str, x: np.ndarray):
        safe = {
            "sin": np.sin, "cos": np.cos, "tan": np.tan,
            "arcsin": np.arcsin, "arccos": np.arccos, "arctan": np.arctan,
            "exp": np.exp, "log": np.log, "sqrt": np.sqrt, "abs": np.abs,
            "pi": np.pi, "e": np.e, "np": np
        }
        safe["x"] = x
        try:
            # restrict builtins
            y = eval(expr, {"__builtins__": None}, safe)
        except Exception as err:
            raise ValueError(f"Error evaluating expression: {err}")
        return y

    def on_plot(self):
        # domain parsing
        try:
            start = float(self.xstart.get())
            end = float(self.xend.get())
            pts = int(self.points.get())
            if pts <= 1 or start == end:
                raise ValueError("points must be >1 and start != end")
        except Exception as e:
            messagebox.showerror("Domain error", f"Bad domain or points: {e}")
            return

        x = np.linspace(start, end, pts)
        expr = self.expr_var.get().strip()
        if not expr:
            messagebox.showerror("Input error", "Type an expression to plot.")
            return

        try:
            y = self.safe_eval(expr, x)
            y = np.asarray(y, dtype=float)
            if y.shape != x.shape:
                # allow scalar result
                if y.shape == ():
                    y = np.full_like(x, float(y))
                else:
                    raise ValueError("Evaluated result shape does not match x.")
        except Exception as err:
            messagebox.showerror("Evaluation error", str(err))
            return

        plt.figure(figsize=(8,5))
        plt.plot(x, y, color="tab:blue")
        plt.title(f"y = {expr}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.tight_layout()
        plt.show()


def main():
    root = tk.Tk()
    root.geometry("760x240")
    app = SimpleFunctionPlotter(root)
    root.mainloop()


if __name__ == "__main__":
    main()