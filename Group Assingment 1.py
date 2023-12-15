import pandas as pd
import matplotlib.pyplot as plt

# data of food and beverange
df1 = pd.read_excel(r"C:/Users/User/Dropbox/PC/Documents/SEM 5/sqit 3073/grp assingmnet 1/3.5.3.xlsx",sheet_name="Sheet2",
                     index_col=0,
                     header=0,
                     usecols="A:G", 
                     skiprows=1)
df1 = df1.astype(int)
columns_to_convert_df1 = [
                      'Sweetened condensed milk (tonnes)',
                      'Canned fish, frozen shrimps/prawns (tonnes)',
                      'Refined sugar (tonnes)',
                      'Prepared animal feeds (tonnes)',
                      'Biscuits (tonnes)',
                      'Soft drinks and carbonated beverages (litres)']

df1[columns_to_convert_df1] = df1[columns_to_convert_df1].astype(int)

# data of tranport equipment
df2 = pd.read_excel(r"C:/Users/User/Dropbox/PC/Documents/SEM 5/sqit 3073/grp assingmnet 1/3.5.3.xlsx",sheet_name="Sheet2",
                     index_col=0,
                     header=0,
                     usecols="A,AL,AM,AN", 
                     skiprows=1)
df2 = df2.astype(int)
columns_to_convert_df2 = [
                      'Passengers cars (units)',
                      'Commercial vehicles (units)',
                      'Motorcycles and Scooters (units)']
                    
df2[columns_to_convert_df2] = df2[columns_to_convert_df2].astype(int)

# data of Petroleum and gas products
df3= pd.read_excel(r"C:/Users/User/Dropbox/PC/Documents/SEM 5/sqit 3073/grp assingmnet 1/3.5.3.xlsx",sheet_name="Sheet2",
                     index_col=0,
                     header=0,
                     usecols="A,R,S", 
                     skiprows=1)
df3=df3.astype(int)
columns_to_convert_df3=['Kerosene (tonnes) ','Liquefied petroleum gas (tonnes) ']   
df3[columns_to_convert_df3]=df3[columns_to_convert_df3].astype(int)                                    


print(df1)
print(df2)
print(df3)

#Bar chart for food and beverange
bar_width = 0.15
colors = ['red', 'blue', 'pink', 'green', 'purple', 'orange']


for i, product in enumerate(columns_to_convert_df1):
    
    plt.bar(df1.index + i * bar_width, df1[product], label=product, color=colors[i], width=bar_width)



plt.xlabel("Period",color="black")
plt.ylabel("Food and beverange (hundred thousand)", color="black")
plt.title("Production of Selected Manufactured Products ")
plt.legend(loc="center", bbox_to_anchor=(0.95,0.95), prop={"weight":"regular", "size":"10"})
plt.grid(False)

#line graph for tranport equipment
plt.figure(figsize=(10,5))
plt.plot(df2.index, df2[('Passengers cars (units)')], label="Passengers cars", color="red", marker="*")
plt.plot(df2.index, df2[('Commercial vehicles (units)')], label="Commercial vehicles",color="blue", marker="*")
plt.plot(df2.index, df2[('Motorcycles and Scooters (units)')], label="Motorcycles and Scooters", color="yellow", marker="*")

plt.xlabel("Period",color="black")
plt.ylabel("Transport Equipment (units) ", color="black")

plt.title("Production of Selected Manufactured Products")
plt.legend(loc="center", bbox_to_anchor=(1,0.5), prop={"weight":"regular", "size":"10"})
plt.grid(True)

# Pie chart for Petroleum and gas products
total_production_df3 = df3[columns_to_convert_df3].sum()

plt.figure(figsize=(10, 6))
plt.pie(total_production_df3, labels=total_production_df3.index, autopct='%1.1f%%', startangle=140)

plt.xlabel("Period", color="black")
plt.ylabel("Petroleum and gas products (tonnes) ", color="black")

plt.title("Production of Selected Manufactured Products")
plt.legend(loc="center", bbox_to_anchor=(1.25, 0.5), prop={"weight": "regular", "size": "10"})
plt.grid(False)

plt.show()




