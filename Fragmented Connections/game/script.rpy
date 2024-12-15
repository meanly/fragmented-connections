# Define characters
define mc = Character("[povname]")  # Main Character
define guard = Character("Kuya Guard")

label ask_name:
    # Ask for the player's name
    $ povname = renpy.input("What is your name?", length=32).strip()

    # If no name is provided, assign a default name
    if not povname:
        $ povname = "Calyx"
        narrator "You didn't input any name. Your default name will be: [povname]."

    return

transform custom_position:
    xpos 1  # Horizontal position (0.0 = far left, 1.0 = far right)
    ypos 1  # Vertical position (0.0 = top, 1.0 = bottom)
    zoom 5  # Scale the size of the image (1.0 = original size)

label start:
    # Ask the player's name before the game starts
    call ask_name from _call_ask_name

    mc "My name is [povname]."

    # Act 1 Introduction
    scene bg gate
    mc "Finally arrived at school after that arduous commute and never-ending red lights!"
    show mc normal 
    mc "Note to self: Do NOT underestimate rush hour traffic."

    scene bg rotunda
    mc "At least I’m not late for the first day of classes."
    show mc normal
    mc "And I still have a good amount of time to kill before the orientation starts."
    mc "Let’s first check where the classroom is."

    mc "\"JFH302…\""
    mc "Where’s that? Guess I’ll just ask Kuya Guard here to not waste time and effort finding the place."

    show guard normal at custom_position
    guard "\"JFH302?\""
    guard "It’s in the building to your left on the third floor."
    guard "Straight ahead are the ‘Kubos’, which students generally use as a rest area."
    guard "To the right is the ICT building, where your laboratory classes will take place."

    scene bg rotunda
    show mc normal 
    mc "Thank you po, Kuya!"
    mc "Hmm.."

    menu:
        "Go LEFT to JFH302":
            jump path_to_jfh
        "Go MIDDLE to Univ-Lane":
            jump path_to_univlane
        "Go RIGHT to ICT":
            jump path_to_ict

# Path Decisions
label path_to_jfh:
    mc "Guess I’ll just head straight to the classroom."
    scene bg black with fade
    jump third_floor_jfh

label path_to_univlane:
    scene bg ulane
    mc "There’s an unusual amount of students gathering at one of those kubo."
    mc "I think they’re members of organizations trying to scout members? I think I’ll avoid that for now."
    mc "But I don’t think this is where I’m supposed to be right now."
    mc "I’ll head to the classroom instead."
    jump path_to_jfh  # Redirects to JFH302 path

label path_to_ict:
    scene bg ictbuilding
    mc "I’ll just check there later before my Intro to Programming class."
    mc "I don’t think I should waste time here before orientation."
    mc "Let’s just head to the classroom."
    jump path_to_jfh  # Redirects to JFH302 path

# Third Floor - JFH Building
label third_floor_jfh:
    scene bg jfh_third_floor
    mc "Haa..Ha-..Ha.. Why is there no elevator here?! This sucks."

    play sound "footsteps.ogg"
    mc "*Footsteps*"
    play sound "door_open.ogg"
    mc "*door opens*"

    scene bg classroom
    mc "Ahh – yes, come to me sweet coldness of the aircon."
    mc "Some classmates are already here."
    mc "I’ll just sit in the back and freshen up a bit near the aircon."

    play sound "chair_sit.ogg"
    mc "*upuan sound pag-upo*"
    mc "..."

    # Interaction Options
    menu:
        "Interact with a classmate":
            jump interact_classmate
        "Let's kill some time":
            mc "Where's the professor? I'm too bored!"
            show mc normal
            mc "Guess I'll try to practicing my pen spinning."
            scene bg pen
            hide mc with fade
            jump timing_minigame
        "lunch combo (knapsack)":
            jump mg_knapsack
        "pathfinding (shortest path)":
            jump mg_shortestpath
        "coin collection (greedy problem)":
            jump mg_greedy
        "debugging race (divide&conquer)":
            jump mg_divideconquer
        "Do nothing":
            mc "..."
            return

# Interaction Placeholder
label interact_classmate:
    mc "This interaction made your relationship with this person improve."
    return

# Minigame Placeholder
label timing_minigame:
    mc "Let’s test out this minigame."
    jump start_minigame
    
    return

label mg_knapsack:
    mc "Let’s test out this minigame."
    jump lunch_combo_minigame
    
    return

label mg_shortestpath:
    mc "Let’s test out this minigame."
    jump campus_pathfinding
    
    return

label mg_greedy:
    mc "Let’s test out this minigame."
    jump start_coincollect
    
    return

label mg_divideconquer:
    mc "Let’s test out this minigame."
    jump start_debugging_race
    
    return