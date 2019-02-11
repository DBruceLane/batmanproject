import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


with plt.xkcd():

    # Fixing random state for reproducibility
    np.random.seed(19680801)


    fig, ax = plt.subplots()
    x = []
    y = []
    i=0

    def update(i):
       ax.cla()
       x.append(i)
       y.append(np.random.randint(0,10))
       ax.plot(x, y)


    ani = animation.FuncAnimation(fig, update, interval=1000)
    plt.show()
