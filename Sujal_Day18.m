

#### Day 18-20: Data Visualization with Matplotlib

Matplotlib is a powerful plotting library in Python used for creating static, interactive, and animated visualizations. It's widely used for data analysis and scientific research. These three days will focus on mastering the basics of Matplotlib, customizing plots, creating subplots, exploring advanced techniques, and developing interactive plots.

#### Day 18: Basics of Plotting with Matplotlib

**1. Introduction to Matplotlib**

- **What is Matplotlib?**: A comprehensive library for creating static, animated, and interactive visualizations in Python.
- **Installation**:
  ```sh
  pip install matplotlib
  ```
- **Basic Components**:
  - **Figure**: The overall window or page where the plot is drawn.
  - **Axes**: The individual plot or graph, which can have multiple axes within a figure.
  - **Axis**: The x-axis and y-axis in a plot.

**2. Basic Plotting**

- **Creating a Simple Plot**:
  - Use `plt.plot()` to plot lines and `plt.show()` to display the plot.
  - Example:
    ```python
    import matplotlib.pyplot as plt

    x = [0, 1, 2, 3, 4]
    y = [0, 1, 4, 9, 16]

    plt.plot(x, y)
    plt.show()
    ```

- **Plotting Styles**:
  - Line styles (`'-'`, `'--'`, `'-.'`, `':'`), marker styles (`'o'`, `'s'`, `'D'`, etc.), and colors (`'b'`, `'g'`, `'r'`, etc.).
  - Example:
    ```python
    plt.plot(x, y, 'ro-')  # Red color, circle markers, solid line
    plt.show()
    ```

- **Multiple Plots**:
  - Plotting multiple lines in the same plot.
  - Example:
    ```python
    plt.plot(x, y, 'r-', label='y = x^2')
    plt.plot(x, [i**3 for i in x], 'b--', label='y = x^3')
    plt.legend()
    plt.show()
    ```

**3. Scatter Plots**

- **Creating a Scatter Plot**:
  - Use `plt.scatter()` for scatter plots.
  - Example:
    ```python
    plt.scatter(x, y)
    plt.show()
    ```

- **Customizing Scatter Plots**:
  - Size (`s`), color (`c`), and alpha (transparency).
  - Example:
    ```python
    plt.scatter(x, y, s=[20, 50, 100, 200, 300], c='red', alpha=0.5)
    plt.show()
    ```
 
