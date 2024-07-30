1) Bar Charts :

       --> Bar charts are effective for visualizing survey data, especially when comparing categorical data.
   Creating Bar Charts
   
       --> To create a basic bar chart, use the bar() function in Matplotlib:
    Example :

           import matplotlib.pyplot as plt

           data = [20, 35, 40, 50, 45]
           labels = ["Python", "Java", "JavaScript", "C++", "C#"]

           plt.bar(labels, data)
           plt.show()

    Customizing Bar Charts : 
      
        --> Customize the appearance of bar charts by adjusting settings such as colors, widths, and spacing.

    Colors
    

            colors = ["#4C72B0", "#E77F67", "#78C679", "#1D953F", "#95B3D7"]

            plt.bar(labels, data, color=colors)
            plt.show()
   
    Widths and Spacing

         --> Change the width of bars and the space between them using width and align parameters:

             plt.bar(labels, data, width=0.7, align="edge")
             plt.show()
   Ouput :
   
   ![Screenshot 2024-07-30 123052](https://github.com/user-attachments/assets/fe9a0228-8d7e-45b3-a217-c0245433e7ec)

2) Pie Charts :

        --> A pie chart is a circular statistical graphic, which is divided into slices to illustrate numerical
            proportion.
   
        --> The size of each slice is proportional to the quantity it represents.
   
        -->Pie charts can be customized by adding:
   
               Title
   
               Data labels

   Example :

           import matplotlib.pyplot as plt

           fruits = ['Apples', 'Bananas', 'Cherries', 'Dates']
           quantities = [15, 30, 45, 10]

            plt.figure(figsize=(7, 7))
            plt.pie(quantities, labels=fruits, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])

            plt.title('Fruit Distribution in Basket')
            plt.show()

   Output :

    ![Screenshot 2024-07-30 123910](https://github.com/user-attachments/assets/cf524fca-7e75-480d-bd59-5a96a5d6ea5d)

   

       
