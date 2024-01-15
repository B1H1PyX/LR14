import matplotlib.pyplot as plt
years = [i for i in range(2000, 2020)]
ukraine_data = [807, 911, 1087, 1416, 1894, 2391, 3197, 4066, 2639, 3078, 3704, 4004, 4187, 3104, 2124, 2187, 2638, 3096, 3661, 3751]
usa_data = [37133, 37997, 39490, 41724, 44123, 46302, 48050, 48570, 47194, 48650, 50065, 51784, 53291, 55123, 56762, 57866, 59907, 62823, 65120, 63528]
plt.figure(figsize=(10, 6))
plt.plot(years, ukraine_data, label='Ukraine')
plt.plot(years, usa_data, label='USA')
plt.xlabel('Year')
plt.ylabel('GDP per capita')
plt.title('Dynamics of "GDP per capita" indicator')
plt.legend()
plt.show()
country_name = input("Enter the country name for the bar chart (Ukraine or USA): ")
selected_data = ukraine_data if country_name.lower() == 'ukraine' else usa_data
plt.figure(figsize=(8, 5))
plt.bar(years, selected_data, color='blue')
plt.xlabel('Ye
           
plt.ylabel('GDP per capita')
plt.title(f'Bar chart for {country_name}')
plt.show()