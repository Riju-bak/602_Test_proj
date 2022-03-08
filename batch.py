import numpy as np
import matplotlib.pyplot as plt


def Batch():
    t = np.linspace(0, 1, 100);
    plt.figure()
    plt.title("Batch REactor")
    plt.plot(t, t**3)
    plt.draw()