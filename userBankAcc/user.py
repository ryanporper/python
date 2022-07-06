class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        
    def display_info(self):
        print('*'*40)
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        return self

    def enroll(self):
        print("**********Enroll Member**********")
        if self.is_rewards_member == True:
            print("You're already a member.")
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200
        print(f"Member: {self.is_rewards_member}")
        print(f"Points: {self.gold_card_points}")
        return self

    def spend_points(self, amount):
        print("**********Spend points**********")
        if self.gold_card_points < amount:
            print('You do not have enough points.')
            return
        else:
            self.gold_card_points -= amount

        print(f"Points: {self.gold_card_points}")
        return self

bill = User("Bill", "Bob", "yoyoy@gmail.com", "24")
johnny = User("Johnny", "Jane", "jj452@gmail.com", "36")

bill.display_info().enroll().spend_points(500)
johnny.display_info().enroll().spend_points(50)