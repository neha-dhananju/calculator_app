import tkinter as tk

# Step 1: Create the main app window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")  # Optional: set window size
root.resizable(False, False)  # Prevent resizing

# Step 2: Create the entry widget (display box)
entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# Step 3: Run the main event loop
root.mainloop()


