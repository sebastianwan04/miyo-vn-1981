label ending_1:

    $ renpy.force_autosave(take_screenshot=True, block=True)
    $ persistent.endings[0] = True

    show bg house 1
    show mom 

    mom "I’ll bring you dinner."

    hide mom
    hide bg house 1

    mc "And just like that, the world ends in silence."


    return