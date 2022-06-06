import random


def Roll ():
    usr_in = input("Press y to roll and n to quit ")
    while usr_in.lower() == "y":
        out = random.randint(1,6)   

        if out == 1:
            print("""
            [       ]
            [   0   ]
            [       ]
            """)
        elif out == 2:
             print("""
            [     0 ]
            [       ]
            [ 0     ]
            """)
        elif out == 3:
            print("""
            [     0 ]
            [   0   ]
            [ 0     ]
            """)
        elif out == 4:
             print("""
            [ 0   0 ]
            [       ]
            [ 0   0 ]
            """)
        elif out == 5:
              print("""
            [ 0   0 ]
            [   0   ]
            [ 0   0 ]
            """)
        elif out == 6:
             print("""
            [ 0   0 ]
            [ 0   0 ]
            [ 0   0 ]
            """)
        usr_in = "n"
        usr_in = input("Press y to roll and n to quit ")
        

Roll()




