transform jaruzelski_center:
    xalign 0.5
    yalign 0.3


image jaruzelski = At("images/NPC/Jaruzel/jaruzelski.png", jaruzelski_center)
image static = At("images/NPC/Jaruzel/static.png", jaruzelski_center)

label day_one:
    stop music fadeout 1.0
    stop sound
    mc "You came to after a sleepless blur, stretched across two chairs stitched together, your curled up body covered with someone’s coat."
    "What roused you wasn’t morning light, but the restless shuffle of adults, rising with heavy heads and clouded eyes."
    "The church fête waits for tomorrow, yet the alcohol and laughter started spilling well from early Friday afternoon."

    show bg house 1 with dissolve 

    uncle "Nothing’s playing."

    mc "You heard a groan escaping your uncle’s lips."

    uncle "This stupid old box. Why’s it all black?" 

    show uncle with vpunch

    uncle "Hey, kid, you know this tech-no-lo-gee stuff better than I do"

    mc "You pushed yourself up, rubbing the sleep out of your eyes, and started fiddling with the knobs"
    
    hide uncle

    mc "Maybe the antennae is crooked or something…"

    show static

    "You pressed every button you could find, then, in your childish frustration, gave the thing a sharp smack"
    "Your uncle stared at you for a moment before he joined in, slapping it around like he was tenderizing a piece of meat after a fight with auntie."
    "You barely noticed your mom setting two cups of chicory coffee on the low table, the steam curling into the stale air."

    hide static
    show mom at right

    mom "Strange… Maybe it’s something to do with the weather. Spare the poor thing, will you? Let’s try the old fashioned way…"

    mc "She smiled faintly and turned to the radio, spinning the dial in search of the right frequency."
    "Static came in waves, roaring, hissing, screaming. For a moment, you thought you could make out words, but they dissolved back into the noise."
    "Then, all at once, the radio caught something – and at the same moment, the television flickered to life on its own."
    "The dim screen filled with the stern face of a balding general, his lips moving just out of sync with the sound coming from the radio."
    "The broadcast overlapped itself, one version echoing slightly behind the other, as if the world had found two ways to say the same terrible thing."
    
    hide mom
    show jaruzelski 

    tv "--day, I address you as a soldier and as the head of the Polish government. I address you on matters of the highest importance."
    "Our homeland has found itself on the edge of an abyss. The legacy of many generations, the Polish home raised from the ashes, is falling into ruin."
    "The structures of the state have ceased to function. The challenge before us is beyond anyone’s ability to resolve."
    "In six days, the world as we know it will come to an end. This is not a crisis we can avert. It is an event we must meet with composure."
    "What matters now is dignity, order, and solidarity. Official announcements will be made each morning and evening. You are advised to stay informed, but not to spread rumors."
    "We recognise that not everyone will want to act. That is acceptable. 
    If your choice is to close your blinds and sleep through the last week, it is as valid as any other."
    "There will be no official judgment."

    mc "The announcement drags on, covering bureaucracy, patriotism, and outlining how things are expected to proceed from this point onward."
    "You listen until your coffee goes cold."
    "The world is supposed to tilt. "
    "Your hands know how to do the tilt." 
    "They practice it on small things; closing windows, turning keys. But nothing tilts. The town keeps its shape. It annoys you to no end."

    hide jaruzelski
    show uncle

    "Your uncle stares at you for a moment before shrugging."

    uncle "Guess I’d better grab my things. Who knows if I’ll be able to get past the town’s borders if I sit around on my arse any longer, har har! Take care, will ya?"

    hide uncle 
    show uncle at left
    show mom at right

    mc "He pulled on his pants while Mom handed him his coat, pressing a quick kiss to his cheek. At the doorstep they lingered, trading goodbyes and half-sentences for far longer than needed, one foot out, one foot in, the same as always."
    "Behind them, the radio droned on, the announcement looping again and again as the TV showed the general’s obnoxious face in tandem."

    hide uncle
    hide mom

    show mom

    play sound church_bell volume 0.1 
    
    mom "Morning mass starts soon…"
    
    menu:
        "I’m going back to bed.":
        
            jump ending_1

        "I’m going to get dressed.":
            hide mom
            stop sound
            mc "You put on your best church clothes, only to bury them under a thick, fluffy coat"
            "The snow outside leaves no room for fashion or self-expression"
            "When your mother isn’t looking, you reach for a baseball cap instead of the wool hat she’s always nagging you to wear and quickly leave the house before she notices."

            jump church

    return