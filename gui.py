import calculation as star_calc
import matplotlib.pyplot as plt

data_dict=star_calc.mass_calc()

sorted_key=sorted(data_dict)
sorted_key_mass=[]

for i in sorted_key:
    sorted_key_mass.append(data_dict[i])

print(sorted_key_mass)

# x axis values 
x = sorted_key 
# corresponding y axis values 
y = sorted_key_mass 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('Mv') 
# naming the y axis 
plt.ylabel('Mass') 
  
# giving a title to my graph 
plt.title('Mv vs Mass') 
  
# function to show the plot 
plt.show() 
