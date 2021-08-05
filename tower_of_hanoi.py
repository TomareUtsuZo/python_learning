"""
This is Carl Eranio's implementation of, Towers of Hanoi.
I am quite satisfied with my class (Tower) implementation, and feel it is clean, except what I would change for
a reimplementation (Allow the game to be expanded). I should go back, and create the ability to define more disks.
I am proud of the increased readability (self-commenting code), of my code.
I feel I should create a library that implements the function, input_incorrectness_test().
It took me aproximately 12 hours, across 20, to code this, on 2021-08-05
"""


class Tower():
    def __init__(self, name):
        self.disks = []
        self.name = name
        self.Assign_disks_at_start(name)

    def Draw_a_tower(self, what_on_tower):
        # what_on_tower = self.disks
        the_tower = [[],[],[],[],[],[], f'      {self.name}      ']
        the_disks = ['     | |     ',
                     '    @| 1@    ',
                     '   @@| 2@@   ',
                     '  @@@| 3@@@  ',
                     ' @@@@| 4@@@@ ',
                     '@@@@@| 5@@@@@']
        for i in range(6):
            the_tower[i] = the_disks[what_on_tower[i]]
        return the_tower

    def Assign_disks_at_start(self, name):
        if name == 'A':
            self.disks = [0, 1, 2, 3, 4, 5]
        else:
            self.disks = [0, 0, 0, 0, 0, 0]

    def Take_top_disk_off(self):
        to_send = None
        for i in range(6):
            if self.disks[i] != 0:
                to_send = self.disks[i]
                self.disks[i] = 0
                break
        return to_send

    def Put_disk_on(self,disk):
        HAS_NO_DISK = 0
        could_fit = False
        for i in range(5):
            next_disk = i + 1
            if self.disks[next_disk] != HAS_NO_DISK:
                if self.disks[next_disk] > disk:
                    self.disks[i] = disk
                    could_fit = True
                    break
        if self.disks[5] == HAS_NO_DISK:
            self.disks[5] = disk
            could_fit = True
        return could_fit


def draw_towers():
    to_draw = []
    for tower in towers:
        to_draw.append(tower.Draw_a_tower(tower.disks))
    for lvl in range(7):
        for tower in range(3):
            print(to_draw[tower][lvl], end='')
        print('')


def get_players_move_order():
    all_correct_ans = ['QUIT', 'AB', 'AC', 'BA', 'BC', 'CA', 'CB']
    base_msg = 'Enter the letters of "from" and "to" towers, or QUIT.\n'\
                                                   '(e.g., AB to moves a disk from tower A to tower B.)'
    print(base_msg)
    user_move_request = input()
    user_incorrect, error_msg = input_incorrectness_test(user_move_request, all_correct_ans)
    if not user_incorrect and (user_move_request.lower() != 'quit'):
        user_correct, error_msg = does_it_follow_the_rules(user_move_request)
        user_incorrect = not user_correct

    while user_incorrect:
        print(f'{error_msg}\n{base_msg}')
        user_move_request = input("?")
        user_incorrect, error_msg = input_incorrectness_test(user_move_request, all_correct_ans)

    return user_move_request


def does_it_follow_the_rules(user_input):
    key = ['A', 'B', 'C']
    return_msg = None
    from_tower = key.index(user_input[0].upper())
    to_tower = key.index(user_input[1].upper())
    disk_to_move = towers[from_tower].Take_top_disk_off()
    if disk_to_move != None:
        it_worked = towers[to_tower].Put_disk_on(disk_to_move)
    else:
        it_worked = False
        return_msg = "There were no disks on that tower."
    if not it_worked and disk_to_move != None:
        towers[from_tower].Put_disk_on(disk_to_move)
        return_msg = "That doesn't fit on there."
    return it_worked, return_msg


def input_incorrectness_test(user_input, range_of_answers, case_matters=False):
    """
    This function returns True if user_input NOT in range_of_answers.
    """
    error_msg = "That wasn't a correct input. Try two letters."
    user_incorrect = True
    if case_matters == False:
        user_input = user_input.lower()
        for i in range(len(range_of_answers)):
            range_of_answers[i] = range_of_answers[i].lower()
    if user_input in range_of_answers:
        user_incorrect = False
    return user_incorrect, error_msg


def test_for_win_condition():
    win = False
    tower_complete = [0, 1, 2, 3, 4, 5]
    if towers[1].disks == tower_complete or towers[2].disks == tower_complete:
        win = True
    return win


towers = [Tower('A'), Tower('B'), Tower('C')]
while True:
    draw_towers()
    time_to_quit = get_players_move_order()
    if time_to_quit.lower() == 'quit':
        print("Have a nice day!")
        break
    if test_for_win_condition():
        print("You win! Good job!")
        break
