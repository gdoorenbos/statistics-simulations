import random

'''
Explanation of phenomenon:
Contestant picks one of three doors. Behind one door is a prize, and the other two are empty.
After the contestant makes a selection, the host reveals a losing door that is not the contestant's choice.
The contestant may then decide to keep their original selection or change their selection to the other remaining door.
This script demonstrates that the contestant has a 66% chance of winning if they change their selection.
The contestant only has a 33% chance of winning if they keep their original selection.

When the host picks the door to reveal, the door must:
* not be the door the contestant chose
* not be the winning door

The original selection has two possible outcomes:
* winning door: 1/3 = 33%
* losing door: 2/3 = 66%

The final outcome has the same probabilities if the contestant sticks with their original choice.

However, these probabilities are inverted if the contestant changes their choice. Here's why:
When a losing door is removed, only two remain: a winning door and a losing door.
If the contestant changes their choice, it flips whether they win or lose. If a losing door was initially chosen, the contestant
will end up with a winning door, and vice versa. Since the initial probability of choosing a losing door is 66%, the odds of
winning are therefor 66% when the contestant changes their choice after a losing door is revealed.

https://en.wikipedia.org/wiki/Monty_Hall_problem
'''

# returns number of wins
def run_trials(num_trials, keep_first_selection):
    return sum([run_trial(keep_first_selection) for _ in range(num_trials)])

# returns true if won, false if lost
def run_trial(keep_first_selection):
    winning_door = random.randint(0, 2)
    chosen_door = random.randint(0, 2)

    # swap selection if requested
    if not keep_first_selection:
        revealable_doors = [door for door in range(3) if door != winning_door and door != chosen_door]
        revealed_door = revealable_doors[random.randint(0, len(revealable_doors) - 1)]
        [chosen_door] = [door for door in range(3) if door != chosen_door and door != revealed_door]

    # reveal chosen door
    return chosen_door == winning_door

def print_results(win_count, num_trials):
    print("num trials: " + str(num_trials))
    print("win count: " + str(win_count))
    print("win %%: %.02f" % (win_count/num_trials * 100))

def main():
    num_loops = 100000

    win_count = run_trials(num_loops, keep_first_selection=True)
    print("keeping first choice:")
    print_results(win_count, num_loops)
    print("")

    win_count = run_trials(num_loops, keep_first_selection=False)
    print("changing choice after reveal:")
    print_results(win_count, num_loops)

if __name__ == '__main__':
    main()