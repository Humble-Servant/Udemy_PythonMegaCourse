HT_List = []

with open('App1/HT.txt', 'r') as file:
    HT_List = file.readlines()

def percentage(ht):
    if len(ht)==0:
        return 0
    else:
        return (ht.count('H\n') / len(ht)) * 100

choice = ''

while choice != 'Exit':
    print(f'\nNum of Flips: {len(HT_List)}   Heads: {percentage(HT_List):.2f}%\n')

    choice = input('Enter H/T, Clear or Exit:')

    match choice:
        case 'H' | 'T':
            HT_List.append(choice + '\n')
            with open('App1/HT.txt', 'a') as file:
                file.write(HT_List[-1])

        case 'Clear':
            HT_List=[]
            with open('App1/HT.txt', 'w') as file:
                file.writelines(HT_List)
