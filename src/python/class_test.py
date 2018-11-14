class Base():
    common = "I am Common Base";

    def __init__(self, Sample):
        print("I am in Base Init with " + Sample)

    def method(self):
        print("Base Method")
        return 20



class Child(Base):

    def __init__(self, Sample):
        Base.__init__(self, 'Call Init Via Child')
        print("I am Child Init with" + Sample)


    def method(self):
        print("Check Child")

    def __len__(self):
        return 1



# child = Child("KOKO")
# print(child.method())
# print(len(child))
#
# del child

class check():
    member = "I am In Class"

    def method(self, value):
        print(self.member + value)


def notFound():
    print("not Found")

checkObj = check()
# checkObj.method("PAPA")

getattr(checkObj, "method", "NOTklJSKJS")(" Papa")




