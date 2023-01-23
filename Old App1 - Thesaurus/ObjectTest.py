# Project Echo Redux
import os

class Member:
    def __init__(self, first, last, email):
        self._first = first
        self._last = last
        self._email = email

    def ShowMember(self):
        print(f'{self._first} {self._last} - {self._email}')

    def GetMember(self):
        return f'{self._first},{self._last},{self._email}'

    def GetEmail(self):
        return self._email


class MemberList:

    def __init__(self, file=None):
        self.memList = []
        self.file = 'memberlist.txt'
        if file:
            self.file = file
        with open(self.file, 'r') as f:
            for line in f:
                first, last, email = line.split(',')
                email = email[:-1]
                new = Member(first, last, email)
                self.memList.append(new)


    def AddMember(self, first, last, email):
        for mem in self.memList:
            if email == mem.GetEmail():
                print("Member already exists!!")
                return
        new = Member(first, last, email)
        self.memList.append(new)

    def ShowMembers(self):
        if len(self.memList) > 0:
            for mem in self.memList:
                mem.ShowMember()
                # print(mem.GetMember())
        else:
            print('Add Members first!')

    def SaveMembers(self):
        if self.file:
            with open(self.file, 'w') as f:
                for mem in self.memList:
                    f.write(mem.GetMember()+'\n')

    def __del__(self):
        print("Saving Members...")
        self.SaveMembers()


def main():
    os.system('cmd /c "python.exe --version"')
    users = MemberList()
    users.ShowMembers()

    # users.AddMember('Wes', 'Motter', 'wes.motter@comcast.net')
    # users.AddMember('Marianne', 'Anderson', 'mari322@comcast.net')
    # users.AddMember('Darrell', 'Warner', 'darrell_warner@yahoo.com')
    # users.ShowMembers()
    # users.SaveMembers()


if __name__ == "__main__":
    main()
