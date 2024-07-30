3) Scatter Plots :

       --> A scatter plot is a type of plot or mathematical diagram using Cartesian coordinates to display values
           for typically two variables for a set of data.

 Customizing Scatter Plots :

  Changing the size and color of the points: 
      
        --> This can be done to visually differentiate between different groups or categories within the data.

  Adding a trend line or regression line: 

        --> This can help to show the general direction and relationship between the variables.
        
  Adding axis labels and a title: 
      
        --> This makes the plot easier to understand by providing context for the data being displayed.

Example :

       import matplotlib.pyplot as plt

      hours_studied = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      scores_obtained = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

      plt.figure(figsize=(8, 5))
      plt.scatter(hours_studied, scores_obtained, color='blue', marker='o', s=100)
  
      plt.title('Hours Studied vs. Scores Obtained')
      plt.xlabel('Hours Studied')
      plt.ylabel('Scores Obtained')


      plt.grid(True)

      plt.show()

  Output :
  
  ![Screenshot 2024-07-30 125821](https://github.com/user-attachments/assets/3df64b7e-6f38-4015-bdad-e82b2f1dc6cd)


  4) Subplots :

    --> To create subplots, we use the plt.subplots() function, which returns a figure object and an array of Axes 
        objects. The function takes the following arguments:

        nrows: Number of rows in the grid of subplots.
        
        ncols: Number of columns in the grid of subplots.
        
        figsize: Size of the figure (width, height) in inches.
        
        sharex: If True, the x-axis will be shared among all subplots.
        
        sharey: If True, the y-axis will be shared among all subplots.

  For eg :

        fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))
        
        This creates a figure with 2x2 grid of subplots, and returns a figure object fig and an array of Axes 
        objects axs with shape (2, 2).

Example of Subplot :

        import matplotlib.pyplot as plt

        x = [1, 2, 3, 4, 5]
        y1 = [1, 4, 9, 16, 25]  
        y2 = [25, 16, 9, 4, 1]  

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

        ax1.plot(x, y1, marker='o', color='blue', linestyle='-', linewidth=2, markersize=8)
        ax1.set_title('Line Plot')
        ax1.set_xlabel('X-axis')
        ax1.set_ylabel('Y-axis')
        ax1.grid(True)

        ax2.bar(x, y2, color='green', alpha=0.7, width=0.5)
        ax2.set_title('Bar Plot')
        ax2.set_xlabel('X-axis')
        ax2.set_ylabel('Y-axis')

        plt.tight_layout()

        plt.show()

Output : 
![Screenshot 2024-07-30 130449](https://github.com/user-attachments/assets/cd97706b-6aaf-45a5-91a2-177100ee40cb)



