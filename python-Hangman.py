#a.b.c.d.e
import random

def play_game_with_enumerate():
    word_list = ['alpha', 'matzov', 'topaz', 'programming', 'computers', 'full stack']
    secret_word = random.choice(word_list)
    display_list = ["_"] * len(secret_word)
    guessed_letters = set()
    life = 8
    print(" ".join(display_list))

    while life > 0 and "_" in display_list:
        signal = input("enetr your number").lower()
        if len(signal) != 1 or not signal.isalpha():
            print("eror add lonely ")
        if signal in guessed_letters:
            print(f" already done'{signal}'.try again.")

        guessed_letters.add(signal)

        if signal in secret_word:
            print(f"good choice'{signal}'exists.")
    
            for index, letter in enumerate(secret_word):
                if letter == signal:
                    display_list[index] = signal
        else:
            life -= 1
            print(f"sori, '{signal}'Not in a word.There are more left {life}lifes.")

        print(" ".join(display_list))

    if "_" not in display_list:
        print(f"You win. The word was'{secret_word}'.")
    else:
        print(f"You lost. The word was'{secret_word}'.")

play_game_with_enumerate()


        

       


