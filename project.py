## HANG MAN GAME

def main():
    number_mistakes = 0
    word = str(input("Please give me a word: ")).replace(" ", "").lower()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    letter_board = []
    for i in range(len(word)):
        letter_board.append(" - ")
    print(letter_board)
    used = ""
    while True:
        print(used)
        print("\n\n")
        letter = str(input("Give me a letter or word: ")).replace(" ", "").lower()
        if check_word(word, letter) == True:
            print("Congratulations you won")
            break

        elif letter in word:
            check_letter(word, letter, letter_board)
            if " - " not in letter_board:
                print("Congratulations you won")
                break
            else:
                continue
        else:
            used += letter
            mistake(number_mistakes)
            print(letter_board)
            number_mistakes +=1
            if number_mistakes == 10:
                print("Game over\n\n")
                print(word)
                break


def check_word(word, letter):
    if letter == word:
        return True
    else:
        return False

def check_letter(word, letter, letter_board):
    for x in range(len(word)):
        letter1 = word[x]
        if letter == letter1:
            letter_board[x] = letter
    print(letter_board)
    return letter_board

def mistake(number_mistakes):
    if number_mistakes == 0:
        print("---")
    elif number_mistakes ==1:
        print(" | ")
        print(" | ")
        print(" | ")
        print("---")
    elif number_mistakes == 2:
        print(" ---------")
        print(" | ")
        print(" | ")
        print(" | ")
        print("---")
    elif number_mistakes == 3:
        print(" ---------")
        print(" |       |")
        print(" | ")
        print(" | ")
        print("---")
    elif number_mistakes == 4:
        print(" ---------")
        print(" |       |")
        print(" |       0")
        print(" | ")
        print("---")
    elif number_mistakes == 5:
        print(" ---------")
        print(" |       |")
        print(" |       0")
        print(" |       |")
        print("---")
    elif number_mistakes == 6:
        print(" ---------")
        print(" |       |")
        print(" |       0")
        print(" |     --|")
        print("---")
    elif number_mistakes == 7:
        print(" ---------")
        print(" |       |")
        print(" |       0")
        print(" |     --|--")
        print("---")
    elif number_mistakes == 8:
        print(" ---------")
        print(" |       |")
        print(" |       0")
        print(" |     --|--")
        print("---     ( ")
    elif number_mistakes == 9:
        print(" ---------")
        print(" |       |")
        print(" |       0")
        print(" |     --|--")
        print("---     ( )")

if __name__ == "__main__":
    main()

#print(" ---------")
#print(" |       |")
#print(" |       0")
#print(" |     --|--")
#print("---     ( )")