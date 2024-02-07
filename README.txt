    # Hangman with visuals
    #### Video Demo:  https://youtu.be/PXWmrVmfmU4
    #### Overview:

    The Hangman Game is a simple Python project that brings the classic word-guessing game to the console. 
    This README.md file serves as documentation for the project, explaining its purpose, functionality, and the structure of the code.

    ## Project Structure

    The project consists of a single Python script, `hangman_game.py`, which contains the implementation of the Hangman game. 
    Below is a breakdown of the key components within the script:

    - **main():** This function serves as the entry point for the game. It initializes the game by taking a word input from the user, 
    sets up the initial letter board, and then enters into a loop where the player can guess letters or the entire word.

    - **check_word(word, letter):** A helper function that checks if the guessed word is correct. 
    It returns a boolean value indicating whether the guessed word matches the target word.

    - **check_letter(word, letter, letter_board):** Another helper function that updates the letter board based on the correct guesses.
    It iterates through the target word, updating the corresponding positions on the letter board.

    - **mistake(number_mistakes):** This function prints part of the hangman figure based on the number of mistakes made by the player. 
    It visualizes the progress of the game.

    ## Gameplay

    The game starts by prompting the user to input a word to be guessed. The word is then converted to lowercase and stripped of spaces. 
    The player is presented with a series of dashes representing the letters of the word. 
    The game continues in a loop until the player either correctly guesses the word or exceeds the maximum allowed mistakes.

    The player can input individual letters or guess the entire word. Correct letter guesses update the letter board, 
    while incorrect guesses lead to the gradual drawing of the hangman figure. The game ends when the player successfully 
    guesses the word or when the hangman figure is completed.

    ## Design Choices

    ### User Interaction

    The game utilizes the console for user interaction, keeping the implementation simple and accessible. 
    The user is prompted to input the word to be guessed and can provide guesses throughout the game.

    ### Visual Representation

    The hangman figure is displayed visually to provide a clear indication of the player's progress. The figure is drawn incrementally 
    based on the number of mistakes made.

    ### Function Decomposition

    The code is structured with multiple functions, each serving a specific purpose. This enhances readability, maintainability, 
    and allows for easier testing and debugging.

    ### Game Loop

    The game utilizes a while loop to continuously prompt the user for guesses until the game is won or lost. 
    This design ensures an interactive and engaging experience for the player.

    ## Conclusion

    The Hangman Game project provides a simple yet entertaining implementation of the classic word-guessing game. 
    The README.md file serves as comprehensive documentation, covering the project's structure, functionality, and design choices. 
    Whether you're a user looking to play the game or a developer interested in the code, this README.md provides all the necessary 
    information to understand and engage with the project. Enjoy playing Hangman!
