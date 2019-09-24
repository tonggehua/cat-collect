import random

class Cat:
    def __init__(self, name="Nyanko", age=1, hair_color="Black"):
        self.name = name
        self.age = age
        self.hair_color = hair_color

    def ask(self, question):
        answers = ["The cat doesn't care.","The cat purrs.","The cat walks away.","The cat sleeps."]
        return answers[random.randint(0,3)]



def make_default_cat():
    cat = Cat(name="",age=5,hair_color='bw')
    return cat

def meow(num):
    output = ""
    if num == 1:
        output = "Persian"
    elif num == 2:
        output = "American Short-hair"
    elif num == 3:
        output = "Japanese Bobtail"

    return output

def rally_cats(n):
    print("Cats have been rallied!")
    for u in range(n):
        print(str(u+1) + " cat(s)...")

    report = "We rally cats."
    return report


def cat_logic(p,q):
    truth = ((p and q) or (not p and not q))

    return truth

def definitely_no_lemons():
    fruits = ['apples','melons','pears','kiwis']
    return fruits[random.randint[0,3]]





