def age(year_of_birth, current_year=2023):
    return (current_year - year_of_birth)

yob = int(input("What is your year of birth: "))
print(age(yob))
