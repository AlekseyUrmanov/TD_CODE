import Tkinter as tk
import random

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def button1_clicked():
    print("Button 1 clicked")

def button2_clicked():
    print("Button 2 clicked")


def update_label(event=None):
    # Get the user input from the Entry widget
    new_text = entry_var.get()

    try:
        new_text = int(new_text)
    except ValueError:
        new_text = 0

    entry.delete(0, 'end')

    # Update the StringVar, which will automatically update the label
    label_var.set("Order Quantity: {}".format(new_text))
    root.focus_set()



def update_display():
    # Simulated profit/loss and open position count
    profit_loss_value = random.uniform(-1000, 1000)
    open_positions_count = random.randint(0, 10)

    # Update the text display areas
    profit_loss_text.delete("1.0", tk.END)
    profit_loss_text.insert(tk.END, "Profit/Loss: ${}".format(round(profit_loss_value,2)))

    open_positions_text.delete("1.0", tk.END)
    open_positions_text.insert(tk.END, "Open Positions: {}".format(open_positions_count))

    # Schedule the next update after a few seconds (adjust as needed)
    root.after(1000, update_display)






# Create the main window
root = tk.Tk()
root.title("Explicit 3x3 Grid")
root.geometry('400x400')

# Create a Frame to group the buttons
button_frame = tk.Frame(root)

order_quantity_frame = tk.Frame(root)


pl_position_frame = tk.Frame(root)



# Create buttons within the Frame
button1 = tk.Button(button_frame, text="Sell Bid", command=button1_clicked)

button2 = tk.Button(button_frame, text="Buy Ask", command=button2_clicked)


label_var = tk.StringVar()
label = tk.Label(order_quantity_frame, textvariable=label_var)
oq_label = tk.Label(order_quantity_frame, text='Enter Order Quantity')

entry_var = tk.StringVar()
entry = tk.Entry(order_quantity_frame, textvariable=entry_var)


profit_loss_text = tk.Text(pl_position_frame, height=2, width=30)
open_positions_text = tk.Text(pl_position_frame, height=2, width=20)


profit_loss_text.pack(pady = 10)
open_positions_text.pack(pady = 10)



# Pack the buttons within the Frame
button1.pack(side=tk.LEFT, padx=10)
button2.pack(side=tk.LEFT, padx=10)

oq_label.pack(pady=2)
entry.pack(pady=2)
label.pack(pady=2)


entry.bind("<Return>", update_label)






# Define a 3x3 grid and place the frame in the center
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)

button_frame.grid(row=1, column=1, padx=10, pady=10)
order_quantity_frame.grid(row=1, column=2, padx=10, pady=10)
pl_position_frame.grid(row = 2, column = 2, padx =  20, pady = 10)



# Create Text widgets for profit/loss and open positions



# Schedule the initial updates
root.after(0, update_display)


# Start the Tkinter event loop
root.mainloop()
