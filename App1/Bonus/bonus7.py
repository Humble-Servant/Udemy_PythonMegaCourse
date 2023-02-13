filenames = ['1.doc', '1.report', '1.presentation']

new_filenames = [f"{file.replace('.', '-')}.txt" for file in filenames]
print()
print(new_filenames)
print()