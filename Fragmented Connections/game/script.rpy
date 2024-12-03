# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define jeremy = Character("Jeremy")


# The game starts here.

label start:


    jeremy "Hey, this is just a prototype of our minigame."

    jeremy "We added a timing minigame here where you need to hit the green bar."

    jeremy "No dialogues yet since we are currently focusing on the mechanics/minigames of our game."

    menu:
        "minigame timing test":
            jump start_minigame
        "Quit":
            return

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    # This ends the game.

    return
