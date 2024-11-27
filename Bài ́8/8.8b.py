print("sinh viên Nguyễn Văn Mạnh")
print("MSSV 235752021610091")


from tkinter import *


def display_selected():
    selected_value = v.get()
    print(f"Selected value: {selected_value}")


root = Tk()
root.title("Welcome")
root.geometry("300x100")


v = IntVar()
v.set(1)  # Default selection

# Create radio buttons
radio1 = Radiobutton(root, text="First", variable=v, value=1)
radio2 = Radiobutton(root, text="Second", variable=v, value=2)
radio3 = Radiobutton(root, text="Third", variable=v, value=3)

# Pack radio buttons
radio1.pack(side=LEFT, padx=5)
radio2.pack(side=LEFT, padx=5)
radio3.pack(side=LEFT, padx=5)

# Create "Click Me" button
button = Button(root, text="Click Me", command=display_selected)
button.pack(side=LEFT, padx=10)

# Run the main loop
root.mainloop()

