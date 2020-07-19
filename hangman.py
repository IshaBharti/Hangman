import random 
print("*****welcome to hangman*****")
name = input("What is your name? ") 
words = ['loyal', 'friends', 'navgurukul', 'programming', 
        'python', 'Hangman', 'player', 'condition', 
        'reverse', 'water', 'board', 'welcome'] 
word = random.choice(words) 
print("Guess the characters") 
guesses = '' 
lives= 5
while lives > 0: 
    failed = 0
    for i in word: 
        if i in guesses: 
            print(i) 
            
        else: 
            print("_") 
            
            
            failed = failed + 1
    if failed == 0: 
      print("The word is: ", word) 
      break
    
    
    guess_word = input("guess a character:") 
    
    
    guesses += guess_word
    

    if guess_word not in word: 
        
        lives = lives - 1
        
    
        print("Wrong") 
        

        print("You have", + lives, 'more guesses') 
        
        
        if lives == 0: 
            print("You Loose")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
