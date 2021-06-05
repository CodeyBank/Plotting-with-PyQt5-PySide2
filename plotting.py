from tkinter import  *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("MathPlotLib")
root.iconbitmap(r'C:\Users\VIRGIN\PycharmProjects\my_python_projects\GUI\image_viewer\vimeo_icon_146250.ico')
root.geometry("400x400")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()


btn = Button(root, text="Plot", command=graph)
btn.pack()
root.mainloop()
