from tkinter import Tk, Label

window = Tk()
window.title("Digital CLock")
window.geometry("600x300")
window.configure(bg="blue")

Label = Label(window, font=("Arial Black",78,"bold"), bg="blue", fg="white")
Label.pack(pady=100)

window.mainloop()