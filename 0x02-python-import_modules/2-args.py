#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 argumets.")
    elif count == 1:
        print("1 argumnet:")
    else:
        print("{} argumnets:".format(count))
    for i in range(count):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
