# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define mary = Character("Marianna", color="ffffff")
define r = Character("Ryoshu", color="ffffff")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg zima

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mary faintsmile

    # These display lines of dialogue.

    mary "The sky is upside down."

    show mary at right

    show ryoshu at left 

    r "It's me Ryoshu from Limbus Company"

    # This ends the game.

    # nowy, zajebisty komentarz

    return
