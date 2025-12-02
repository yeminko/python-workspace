# **kvargs will create a dictionary
def build_profile(name, age, **other):
    other['name'] = name
    other['age'] = age
    return other


profile = build_profile('John', 29, gender='Male',
                        salary=1500, address='Yangon')
print(profile)
