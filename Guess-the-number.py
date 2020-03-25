import random
while True:
    try:
        print('(NOTE:- HIGHER THE NUMBER THE DIFFUCULT THE GAME)\nEnter the range of numbers u want to guess from 1 to -- ',end='')
        ran = int(input())
        Com_gen_num = random.randint(1, ran)
        chances = 1
        your_num = None
        while your_num != Com_gen_num:
            your_num = input('ENTER YOU GUESS NUMBER >> ')
            if your_num.isdigit():
                your_num = int(your_num)
            else:
                print('invalid number, try again')
                continue
            if your_num == Com_gen_num:
                print("Great, You guessed right. you took ",chances,'chances')
            else:
                if your_num > Com_gen_num:
                     print('Your guess is high, try again')
                else:
                     print('Your guess is low, try again')
                chances += 1
        break
    except(TypeError, ValueError):
        print('Invalid Number, try again')
            
        
        
                    
                    
            
        
    
    
