import tkinter as tk

# Step 1: Create the main app window
root = tk.Tk()
root.title("Calculator")
root.geometry("380x400")  # Optional: set window size
root.resizable(False, False)  # Prevent resizing

# Step 2: Create the entry widget (display box)
entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=35,ipady=30)


def button_click(char):
    entry.insert(tk.END, char)

def clear_entry():
    entry.delete(0, tk.END)

def calculate_result():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")



# Step 3: Add first row button
btn_7=tk.Button(root, text="7", width=5, height=2, font=("Arial", 16),command=lambda: button_click("7"))
btn_7.grid(row=1, column=0, padx=5, pady=5)

btn_8=tk.Button(root , text="8" , width=5 , height=2 , font=('Arial',16),command=lambda: button_click("8"))
btn_8.grid(row=1 , column=1 ,padx=5,pady=5)

btn_9=tk.Button(root , text="9" , width=5 , height=2 , font=('Arial',16),command=lambda: button_click("9"))
btn_9.grid(row=1 , column=2 ,padx=5,pady=5)

btn_div=tk.Button(root , text="/" , width=5 , height=2 , font=('Arial',16),command=lambda: button_click("/"))
btn_div.grid(row=1 , column=3 ,padx=5,pady=5)


# Step 4: Add second row of buttons
btn_4 = tk.Button(root, text="4", width=5, height=2, font=("Arial", 16),command=lambda: button_click("4"))
btn_4.grid(row=2, column=0, padx=5, pady=5)

btn_5 = tk.Button(root, text="5", width=5, height=2, font=("Arial", 16),command=lambda: button_click("5"))
btn_5.grid(row=2, column=1, padx=5, pady=5)

btn_6 = tk.Button(root, text="6", width=5, height=2, font=("Arial", 16),command=lambda: button_click("6"))
btn_6.grid(row=2, column=2, padx=5, pady=5)

btn_mul = tk.Button(root, text="*", width=5, height=2, font=("Arial", 16),command=lambda: button_click("*"))
btn_mul.grid(row=2, column=3, padx=5, pady=5)

# Step 5: Add third row of buttons
btn_1 = tk.Button(root, text="1", width=5, height=2, font=("Arial", 16),command=lambda: button_click("1"))
btn_1.grid(row=3, column=0, padx=5, pady=5)

btn_2 = tk.Button(root, text="2", width=5, height=2, font=("Arial", 16),command=lambda: button_click("2"))
btn_2.grid(row=3, column=1, padx=5, pady=5)

btn_3 = tk.Button(root, text="3", width=5, height=2, font=("Arial", 16),command=lambda: button_click("3"))
btn_3.grid(row=3, column=2, padx=5, pady=5)

btn_sub = tk.Button(root, text="-", width=5, height=2, font=("Arial", 16),command=lambda: button_click("-"))
btn_sub.grid(row=3, column=3, padx=5, pady=5)


# Step 6: Add fourth row of buttons
btn_0 = tk.Button(root, text="0", width=5, height=2, font=("Arial", 16),command=lambda: button_click("0"))
btn_0.grid(row=4, column=0, padx=5, pady=5)

btn_C = tk.Button(root, text="C", width=5, height=2, font=("Arial", 16),command=clear_entry)
btn_C.grid(row=4, column=1, padx=5, pady=5)

btn_eq = tk.Button(root, text="=", width=5, height=2, font=("Arial", 16),command=calculate_result)
btn_eq.grid(row=4, column=2, padx=5, pady=5)

btn_add = tk.Button(root, text="+", width=5, height=2, font=("Arial", 16),command=lambda: button_click("+"))
btn_add.grid(row=4, column=3, padx=5, pady=5)



# Step 7: Run the main event loop
root.mainloop()


