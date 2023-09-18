#!/bin/bash
              
              a=2
              b=2
              c=$((a + b))
              
              echo "Bash says: Hello, World!"
              echo "$a + $b = $c"

              myUsers=("User1", "User2", "User3")

              for x in ${myUsers[@]};
              do 
              echo $x
              done

