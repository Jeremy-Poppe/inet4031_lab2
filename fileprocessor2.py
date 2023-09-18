import sys

for line in Lines:
    user = line.split(":")
    if("#" in user[0]):
        print()
    else:
        print("The user " + user[0] + " has a password of " + user[1] + " and has a userid " + user[2] + " and groupid " + user[3])






  

