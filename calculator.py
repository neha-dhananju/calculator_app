import tkinter as tk

# Step 1: Create the main app window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")  # Optional: set window size
root.resizable(False, False)  # Prevent resizing

# Step 2: Create the entry widget (display box)
entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

btn_7=tk.entry(root, text="7", width=5, height=2, font=("Arial", 16))
btn_7.grid(row=1, column=0, padx=5, pady=5)

btn_8=tk.entry(root , text="8" , width=5 , height=2 , font=('Arial',16))
btn_8.grid(row=1 , column=1 ,padx=5,pady=5)

btn_9=tk.entry(root , text="9" , width=5 , height=2 , font=('Arial',16))
btn_9.grid(row=1 , column=2 ,padx=5,pady=5)

btn_div=tk.entry(root , text="/" , width=5 , height=2 , font=('Arial',16))
btn_div.grid(row=1 , column=3 ,padx=5,pady=5)

# Step 3: Run the main event loop
root.mainloop()


