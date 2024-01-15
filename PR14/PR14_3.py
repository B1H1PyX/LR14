import matplotlib.pyplot as plt
details_count = {
    'Type 1': 150,
    'Type 2': 200,
    'Type 3': 120,
    'Type 4': 180,
    'Type 5': 250
}
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightpink', 'lightsalmon']
plt.figure(figsize=(8, 8))
plt.pie(details_count.values(), labels=details_count.keys(), autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Distribution of the number of parts of five types')
plt.show()
