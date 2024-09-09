import random
from words import word_list
display_guess=""#global variable

#function for selecting random word 
def get_word():
    word=random.choice(word_list)
    
    return word.upper()
stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
def show(word,tries,guess):
   global display_guess
   if(tries==0):
     
      random_letter=random.choice(word)
      pos=word.find(random_letter)
      word_as_list= list(display_guess)
      word_as_list[pos]=random_letter
      display_guess="".join(word_as_list)
      print(display_guess)
      # display_guess[pos]=random_letter
      

      # this where we add a guess  
   else:  
     
      # random_letter=random.choice(word)
      pos=word.find(guess)
      word_as_list= list(display_guess)
      word_as_list[pos]=guess
      display_guess="".join(word_as_list)
      print(display_guess)
      # print(display_guess)
      

def play(word):
   tries=0
   print(word)#this part should be removed after complition of code 
   
   global display_guess
   guessd_letter=[]
   length_=len(word)
   display_guess="_"*length_
   chance=6
   show(word,tries,"_")
   while(chance):
      tries=tries+1
      guess=input("guess the a letter \n").upper()
      if guess not in guessd_letter:
         if guess in word:
            guessd_letter.append(guess)#this is where we add the guess of to the word 
            
            # pos=word.find(guess)#here we find the guessed elements place 
            show(word,tries,guess)            
               
               
         else:
            print("the letter is not in the word ")
            chance-=1
         
      else:
         print("you have already tried it ")
      print("                                             ",stages[chance]) 
      if(len(guessd_letter)==len(word)):
         break
   print("GAME OVER")
   return
   
    
    







def main():
      word = get_word()
      play(word)
      print(" ")
      while input("Play Again? (Y/N) ").upper() == "Y":
         word = get_word()
         play(word)




if __name__ == "__main__":
    main()