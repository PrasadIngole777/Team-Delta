### Adding Titles:
```
plt.title(): Sets the title of the plot
plt.title() can take a string argument, which is the title of the plot
Example: plt.title('Line Plot Example')
```
### Labeling Axes:
```
plt.xlabel(): Sets the label for the x-axis
plt.ylabel(): Sets the label for the y-axis
Both functions take a string argument, which is the label for the axis
Example: plt.xlabel('X-axis') and plt.ylabel('Y-axis')
```
### Legends:
Legends help identify different data series in the plot. Use the label parameter in your plotting functions and call plt.legend() to display the legend.
```py
plt.plot(x, y, label='y = x^2')  # Line plot with a label
plt.plot(x, [i**0.5 for i in y], label='y = sqrt(x)')  # Another line plot with a label
plt.legend()  # Show legend
plt.show()
```

