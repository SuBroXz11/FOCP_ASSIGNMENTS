#  Write a program that takes a bunch of command-line arguments, and then prints
#  out the shortest. If there is more than one of the shortest length, any will do.
#  Hint: Don't overthink this. A good way to find the shortest is just to sort them.

import sys
def find_shortest_argument():
    args = sys.argv[1:]  # Exclude the script name
    if not args:
        print("No arguments provided.")
        return

    shortest_arg = min(args, key=len)
    print(f"The shortest argument is: {shortest_arg}")

if __name__ == "__main__":
    find_shortest_argument()
