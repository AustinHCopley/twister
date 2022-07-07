import random as rand

class Twister():
    colors = ["red", "yellow", "green", "blue"]
    bodyparts = ["Right hand", "Left hand", "Right foot", "Left foot"]
    
    def __init__(self, turn):
        self.turn = turn
    
    @classmethod
    def spin(cls):
        color = rand.choice(cls.colors)
        bodypart = rand.choice(cls.bodyparts)
        return bodypart, color

    def addTurn(self):
        self.turn += 1

    def skipTurn(self):
        self.turn -= 1

    def toStr(self, bodypart, color):
        print("  Round", str(self.turn) + ":", bodypart, "-->",  color, "\n")


def main():
    
    twister = Twister(0)
    skip = ""
    userIn = input("<< Press enter to spin. Enter \".\" to skip prev turn. Enter anything else to quit. >> ")

    while True:

        bodypart, color = twister.spin()
        twister.addTurn()
        twister.toStr(bodypart, color)
        prompt = "<< P" + skip + "ress enter to spin again. >> "
        userIn = input(prompt)

        # if input is '.', re-spin for the same turn/person
        if userIn == ".":
            twister.skipTurn()
            skip = "revious turn skipped, p"
            
        elif userIn != "":
            break

        else:
            skip = ""


if __name__ == "__main__":
    main()
    
