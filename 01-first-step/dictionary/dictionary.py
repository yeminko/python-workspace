alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])

# Loop key-value pairs
for key, value in alien_0.items():
    print(f'\n Key: {key}')
    print(f'Value: {value}')

# Way 1: Loop key only
for key in alien_0.keys():
    print(f'Keys: {key}')

# Way 2: Loop key only (default will give only keys)
for key in alien_0:
    print(f'Keys: {key}')
