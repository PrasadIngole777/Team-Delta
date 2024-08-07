# Animating Graphs and Plots using Matplotlib and Numpy 

import numpy as np
import matplotlib.pyplot as plt
from manim import *

class GraphAnimation(Scene):
    def construct(self):
        x = np.linspace(0, 2 * np.pi, 100)
        y = np.sin(x)

        fig, ax = plt.subplots()
        ax.plot(x, y)

        graph = VGroup(*[ax.plot([x[i], x[i]], [0, y[i]], color=BLUE) for i in range(len(x))])
        self.add(graph)

        def update_graph(obj, alpha):
            for i, line in enumerate(obj):
                line.become(ax.plot([x[i], x[i]], [0, y[i] * alpha], color=BLUE))

        self.play(UpdateFromAlphaFunc(graph, update_graph), run_time=2)




