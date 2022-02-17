import tkinter
FONT_SIZE = 12
FONT_TYPE = "Arial"

# Function to convert miles to kilometers
def convert():
    num_miles = int(input.get())
    num_km = round(num_miles*1.609, 2)
    final_km_label.config(text=num_km)


# Window
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=10, pady=10)

# Label - Miles
miles_label = tkinter.Label(text="Miles", font=(FONT_TYPE, FONT_SIZE))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

# Label - Km
km_label = tkinter.Label(text="Km", font=(FONT_TYPE, FONT_SIZE))
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

# Label - is equal to
equal_label = tkinter.Label(text="is equal to", font=(FONT_TYPE, FONT_SIZE))
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)

# Label - final Km
final_km_label = tkinter.Label(text="0", font=(FONT_TYPE, FONT_SIZE))
final_km_label.grid(column=1, row=1)
final_km_label.config(padx=10, pady=10)

# Button
button = tkinter.Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

# Entry
input = tkinter.Entry(width=10)
print(input.get())
input.grid(column=1, row=0)





window.mainloop()