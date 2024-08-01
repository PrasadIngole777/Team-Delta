
#### Day 19: Customizing Plots with Titles, Labels, and Legends

**1. Titles and Labels**

- **Adding Titles**:
  - Use `plt.title()` to set a title for the plot.
  - Example:
    ```python
    plt.plot(x, y)
    plt.title('Quadratic Function')
    plt.show()
    ```

- **Axis Labels**:
  - Use `plt.xlabel()` and `plt.ylabel()` to set the x and y-axis labels.
  - Example:
    ```python
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()
    ```

**2. Legends**

- **Adding Legends**:
  - Use `plt.legend()` to add a legend to the plot.
  - Example:
    ```python
    plt.plot(x, y, label='y = x^2')
    plt.plot(x, [i**3 for i in x], label='y = x^3')
    plt.legend()
    plt.show()
    ```

- **Customizing Legends**:
  - Position (`loc`), frame, and ')
    plt.plot(x, [i**3 for i in x], label='y = x^3')
    plt.legend(loc='upper left', fontsize='large', frameon=False)
    plt.show()
    ```

**3. Annotations**

- **Adding Annotations**:
  - Use `plt.annotate()` to add text annotations at specific points.
  - Example:
    ```python
    plt.plot(x, y)
    plt.annotate('Maximum', xy=(4, 16), xytext=(2, 15), arrowprops=dict(facecolor='black', shrink=0.05))
    plt.show()
    ```
 
