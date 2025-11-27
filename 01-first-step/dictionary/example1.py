friends = ['john', 'phil', 'sarah']

favorite_languages = {
    'john': 'java',
    'phil': 'python'
}

for friend in friends:
    print(f'\nHi {friend}!')

    favorite_language = favorite_languages.get(friend)

    if favorite_language:
        print(f'Your favorite language is {favorite_language}')
    else:
        print("Oh! you don't have any favorite!")
