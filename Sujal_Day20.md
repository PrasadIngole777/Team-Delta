
#### Day 20: Subplots, Advanced Plotting Techniques, and Interactive Plots

**1. Subplots**

- **Creating Subplots**:
  - Use `plt.subplot()` or `plt.subplots()` to create multiple plots within a single figure.
  - Example:
    ```python
    fig, ax = plt.subplots(2, 2)
    ax[0, 0].plot(x, y)
    ax[0, 1].plot(x, [i**3 for i in x])
    ax[1, 0].scatter(x, y)
    ax[1, 1].bar(x, y)
    plt.show()
    ```

- **Customizing Subplots**:
  - Adjust spacing with `plt.tight_layout()` or `fig.subplots_adjust()`.
  - Example:
    ```python
    fig, ax = plt.subplots(2, 2)
    fig.tight_layout(pad=3.0)
    ```

**2. Advanced Plotting Techniques**

- **Bar Plots**:
  - Use `plt.bar()` for bar charts.
  - Example:
    ```python
    categories = ['A', 'B', 'C']
    values = [5, 7, 3]
    plt.bar(categories, values)
    plt.show()
    ```

- **Histograms**:
  - Use `plt.hist()` for histograms.
  - Example:
    ```python
    data = np.random.randn(1000)
    plt.hist(data, bins=30, alpha=0.5)
    plt.show()
    ```

- **Pie Charts**:
  - Use `plt.pie()` for pie charts.
  - Example:
    ```python
    sizes = [15, 30, 45, 10]
    labels = ['A', 'B', 'C', 'D']
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.show()
    ```

**3. Interactive Plots**

- **Matplotlib Widgets**:
  - Use widgets like sliders, buttons, and check buttons to create interactive plots.
  - Example:
    ```python
    from matplotlib.widgets import Slider, Button

    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.25, bottom=0.25)
    t = np.arange(0.0, 1.0, 0.001)
    a0 = 5
    f0 = 3
    s = a0 * np.sin(2 * np.pi * f0 * t)
    l, = plt.plot(t, s, lw=2)
    axcolor = 'lightgoldenrodyellow'
    axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
    axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

    sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0)
    samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)

    def update(val):
        amp = samp.val
        freq = sfreq.val
        l.set_ydata(amp * np.sin(2 * np.pi * freq * t))
        fig.canvas.draw_idle()

    sfreq.on_changed(update)
    samp.on_changed(update)

    resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
    button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

    def reset(event):
        sfreq.reset()
        samp.reset()
    button.on_clicked(reset)

    plt.show()
    ```

 
