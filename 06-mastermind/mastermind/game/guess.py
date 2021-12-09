import random

class Guess:
    def __init__(self):
        self.answer_key = ["*","*","*","*"]
        self.user_guess = 0000
        self.end_game = False

    def get_random_number(self):
        random_num = random.randint(1000, 9999)
        return random_num

    def get_user_guess(self):
        user_guess = int(input("What is your guess? "))
        while(user_guess > 9999 or user_guess < 1000):
            user_guess = int(input("Invalid input!\nWhat is your guess? "))
        self.user_guess = user_guess

    def set_user_key(self, key_num):
        answer_key_list = ["*","*","*","*"]
        #change key number and user guess number into string lists
        key_num_string = str(key_num)
        user_guess_string = str(self.user_guess)
        key_num_list = []
        user_guess_list = []
        for let in key_num_string:
            key_num_list.append(let)
        for let in user_guess_string:
            user_guess_list.append(let)
        
        #make comparision to find answer symbol key
        for i in range(len(key_num_string)):

            #count number of times one of user's numbers is in answer
            is_in_number = key_num_string.count(user_guess_list[i])

            #If user number is same as the answer number position
            if key_num_list[i] == user_guess_list[i]:
                answer_key_list[i] = "X"

            #if user number is in the answer
            elif is_in_number > 0:
                answer_key_list[i] = "O"

            #if number is not in the answer
            else:
                answer_key_list[i] = "*"
        self.answer_key = answer_key_list

    def player_wins(self):
        if self.answer_key == ["X","X","X","X"]:
            self.end_game = True