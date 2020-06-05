# expectation of first success is 1/p
# this script serves as a practical confirmation
# https://www.cut-the-knot.org/Probability/LengthToFirstSuccess.shtml
import random
import statistics

# change this to test different probabilities
chance_of_success = 0.1

def main():
    attempts = []
    for _ in range(1000):
        # keep rolling until we succeed
        count = 1
        while random.random() > chance_of_success:
            count += 1
        attempts.append(count)

    print("expected attempts: " + str(1.0/chance_of_success))
    print("average attempts: " + str(statistics.mean(attempts)))

if __name__ == '__main__':
    main()
