# expectation of first success is 1/p
# this script serves as a practical confirmation
# https://www.cut-the-knot.org/Probability/LengthToFirstSuccess.shtml
import random
import statistics

# change this to test different probabilities
chance_of_success = 0.1

# returns number of attempts
def roll_until_success():
    count = 1
    while random.random() > chance_of_success:
        count += 1
    return count

def main():
    num_attempts = 10000
    attempts = [roll_until_success() for _ in range(num_attempts)]
    print("expected attempts: " + str(1.0/chance_of_success))
    print("average attempts: " + str(statistics.mean(attempts)))

if __name__ == '__main__':
    main()
