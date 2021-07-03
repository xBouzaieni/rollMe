import random
import time 

def menu():
    print('\n\t ¦ˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉ¦')
    print(  '\t ¦  R. Roll the dice!  ¦')
    print(  '\t ¦        Q. Quit!     ¦')
    print(  '\t ¦ˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍ¦')

def quit() : 
    print('\n\t     ¦ˉˉˉˉˉˉˉˉˉˉˉˉˉ¦'  )
    print(  '\t     ¦  COME BACK  ¦'  )
    print(  '\t     ¦    AGAIN    ¦'  )
    print(  '\t     ¦ˍˍˍˍˍˍˍˍˍˍˍˍˍ¦\n')    
def roll_dice():
    reply = ''
    while reply != 'Q' :
        menu()
        reply = input("\n\t    --> ").upper()
        dice = random.randint(1, 6)
        if dice == 1 and reply == 'R' :
            print('\n')
            print('\t\t¦ˉˉˉˉˉˉˉˉˉ¦'  )
            print('\t\t¦         ¦'  )
            print('\t\t¦    ʘ    ¦'  )
            print('\t\t¦         ¦'  )
            print('\t\t¦ˍˍˍˍˍˍˍˍˍ¦\n')
            time.sleep(2)
        elif dice == 2 and reply == 'R':
            print('\n')
            print('\t\t¦ˉˉˉˉˉˉˉˉˉ¦'  )
            print('\t\t¦  ʘ      ¦'  )
            print('\t\t¦         ¦'  )
            print('\t\t¦      ʘ  ¦'  )
            print('\t\t¦ˍˍˍˍˍˍˍˍˍ¦\n')
            time.sleep(2)
        elif dice == 3 and reply == 'R':
            print('\n')
            print('\t\t¦ˉˉˉˉˉˉˉˉˉ¦'  )
            print('\t\t¦  ʘ      ¦'  )
            print('\t\t¦    ʘ    ¦'  )
            print('\t\t¦       ʘ ¦'  )
            print('\t\t¦ˍˍˍˍˍˍˍˍˍ¦\n')
            time.sleep(2)
        elif dice == 4 and reply == 'R':
            print('\n')
            print('\t\t¦ˉˉˉˉˉˉˉˉˉ¦'  )
            print('\t\t¦  ʘ   ʘ  ¦'  )
            print('\t\t¦         ¦'  )
            print('\t\t¦  ʘ   ʘ  ¦'  )
            print('\t\t¦ˍˍˍˍˍˍˍˍˍ¦\n')
            time.sleep(2)
        elif dice == 5 and reply == 'R':
            print('\n')
            print('\t\t¦ˉˉˉˉˉˉˉˉˉ¦'  )
            print('\t\t¦  ʘ   ʘ  ¦'  )
            print('\t\t¦    ʘ    ¦'  )
            print('\t\t¦  ʘ   ʘ  ¦'  )
            print('\t\t¦ˍˍˍˍˍˍˍˍˍ¦\n')
            time.sleep(2)
        elif dice == 6 and reply == 'R':
            print('\n')
            print('\t\t¦ˉˉˉˉˉˉˉˉˉ¦'  )
            print('\t\t¦  ʘ   ʘ  ¦'  )
            print('\t\t¦  ʘ   ʘ  ¦'  ) 
            print('\t\t¦  ʘ   ʘ  ¦'  )
            print('\t\t¦ˍˍˍˍˍˍˍˍˍ¦\n')
            time.sleep(2)
        else :
            dice = 0
            quit()
            break

   
roll_dice()