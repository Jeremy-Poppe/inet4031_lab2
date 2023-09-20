import sys

for line in sys.stdin:
    if '#' == line.rstrip:
        break
    else:
        print("The user " + line.find(":") + " has a password of " + line.find(":") + " and has a userid " + line.find(":") + " and groupid " + line.find(":"))

    
    
    





  

