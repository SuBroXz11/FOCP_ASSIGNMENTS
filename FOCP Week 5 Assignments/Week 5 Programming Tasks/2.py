# Write a program that, when run from the command line, reports how many
# arguments were provided. (Remember that the program name itself is not an
# argument).

import sys
def check_args():
    args=sys.argv
    num_args = len(args) - 1
    print(f"the number is args is {num_args}")
check_args()