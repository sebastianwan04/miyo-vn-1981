label intro:
    play music steve_roden_airria
    show screen player_input_disable
    show screen intro
    pause 13
    hide screen intro
    show screen day_countdown("12th December, 1981") with Dissolve(0.25)
    play sound date_transition volume 0.5
    pause 2
    hide screen day_countdown with dissolve
    pause 0.5
    hide screen player_input_disable
    jump day_one