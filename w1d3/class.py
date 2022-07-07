class Phone:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def info(self):
        print(f"color: {self.color}")
        print(f"weightweight: {self.weight}")
        return self

    def call(self, number):
        print(f"making a call yo {number}")
        return self
    
    def ring(self):
        print("ringringirgnrignrignirging")
        return self

    def hang_up(self):
        print("hanging uppp")
        return self
    

class CellPhone(Phone):
    def __init__(self, color, weight):
        super().__init__(color, weight)
        self.type = "Cell Phone"

    def info(self):
        super().info()
        print(f"type: {self.type}")
        return self

    def text(self, number, msg):
        print(f"sending {number} message : {msg}")
        return self

class FlipCellPhone(CellPhone):
    def __init__(self, color, weight):
        super().__init__(color, weight)
        self.flip_status = "closed"

    def info(self):
        super().info()
        print(f"Status: {self.flip_status}")
        return self

    def flipped_closed(self):
        self.flip_status = "closed"
        return self

    def flipped_open(self):
        self.flip_status = "open"
        return self
        
    def call(self, number):
        if self.flip_status == "closed":
            print("Must open phone to make a call")
        else:
            super().call(number)
        return self

# phone1 = FlipCellPhone("blue", 5)
# phone2 = CellPhone("black", 3)
phone3 = FlipCellPhone("gray", 6)


# phone1.info().call(5615752355).text(5552223333, "Yo waddup dawg")
# phone2.info().call(5552223333).text(5552223333, "Yo waddup dawg")
phone3.info().call(5552223333).text(5552223333, "Yo waddup dawg")