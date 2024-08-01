### Subplot
With the subplot() function you can draw multiple plots in one figure
Example:
```py
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()
```
Output:
![image](https://github.com/user-attachments/assets/52dce5ec-cc7c-47dd-b765-a9a0b293272b)


### Subplot Function:
~The subplot() function takes three arguments that describes the layout of the figure.
~The layout is organized in rows and columns, which are represented by the first and second argument.
~The third argument represents the index of the current plot.
```py
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x,y)

plt.show()
```
Result:
![image](https://github.com/user-attachments/assets/764d81d0-b9de-443d-ab2e-aa048cc3501b)


### Scatter Plot:
```py
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()
```
Output:
![image](https://github.com/user-attachments/assets/53803c02-b5df-4012-bc5f-cd917d7eeaa4)

### Bar Plot:
```py
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red")
plt.show()
```
Result:
![image](https://github.com/user-attachments/assets/641e5c54-39d8-4429-989d-38441cb3c771)

### Pie Plot:
```py
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show()
```
Result:
![image](https://github.com/user-attachments/assets/bfd83c93-e26e-4fa5-bc01-ae68ce6bb28c)

### Line Plot:
```py
import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()
```
Result:
![image](https://github.com/user-attachments/assets/1a4289ca-a0a0-4d61-9d62-f505307fc28d)
