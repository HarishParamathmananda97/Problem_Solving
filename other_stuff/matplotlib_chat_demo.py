import pandas as pd
import matplotlib.pyplot as plt

# Sample trading data
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'Price': [100, 105, 110, 115, 120],
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Plot the trading data
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Price'], marker='o', color='b', linestyle='-')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Trading Data')

# Display the plot
plt.grid(True)
plt.show()

original_dict = {'old_key1': 'value1', 'old_key2': 'value2', 'old_key3': 'value3', 'old_key4': 'value4', 'old_key5': 'value5'}

# Create a new dictionary with the renamed keys and values
original_dict = {('new_key1' if key == 'old_key1' else 'new_key2' if key == 'old_key2' else 'new_key3' if key == 'old_key3' else 'new_key4' if key == 'old_key4' else 'new_key5' if key == 'old_key5' else key): value for key, value in original_dict.items()}

original_dict.update((k, original_dict.pop(k)) for k in ('old_key1', 'old_key2', 'old_key3', 'old_key4', 'old_key5'))

print(original_dict)

od = {('First_Name' if key  == 'name' else 'B_Age' if key == 'Age' else key): value for key, value in od.items()}
