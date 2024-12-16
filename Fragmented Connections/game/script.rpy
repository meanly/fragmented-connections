# Define characters
define mc = Character("[povname]")  # Main Character
define guard = Character("Kuya Guard")
define stranger = Character("Stranger")
define charles = Character("Charles")
define professor = Character("Miss Professor")
define classrep = Character("Ella")

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
    scene bg prologue mc room
    mc "“Heh, GG EZ.. That was a tough game.. Good thing we won though..”"
    mc "Hmmm.. He already logged off I guess?"
    mc "“sigh. Might as well call it a day then..”"
    mc "Man, did I actually just spend my whole vacation sitting in my room, playing this accursed video game with some randos on the internet and not feel bad about it?"
    mc "Heck, yeah, not like there’s anything else for me to do anyway. I mean, this has been my everyday routine since that virus forced everyone to stay indoors for almost two whole years and schools are forced to carry out classes online."
    mc "Although, they say we would revert back to having traditional classes inside the classrooms for this upcoming year."
    mc "“Why decide on this just as I am going into college??” “Last time I held a book was before the pandemic hit. Would I even survive class without asking my trusty friend ChatJPYT?”"
    mc "Calm down and stop talking to yourself!"
    mc "Let’s take this seriously. This is THE John Baptist University we’re talking about. That name itself has probably been heard by every Filipino in this day and age."
    mc "The students there are probably all the top of their classes. Why did I actually enroll here just because of a random message from someone I met online."
    mc "I still wonder what he meant by that."
    mc "“See you soon!”"
    scene bg chapone with fade
    pause(3.0) 
 
    # Act 1 Introduction
    scene bg gate
    mc "Finally arrived at school after that arduous commute and never-ending red lights!"
    show mc normal with dissolve
    mc "Note to self: Do NOT underestimate rush hour traffic."
    mc "“Good thing I left home early. I still have enough time to spend on my leisure before orientation starts.”"
    mc "First things first, let’s make sure we know where the classroom will be.."
    mc "I hope it's nearby."

    scene bg rotunda
    with  dissolve

    mc "Let’s see here…JFH302 huh…"
    mc "Where’s that? Guess I’ll just ask Kuya Guard here to not waste time and effort finding the place."

    show mc normal at right
    with moveinright
    pause(2.0)
    show guard normal at left
    with moveinleft
    mc "Excuse me po sir?"
    guard "Ahh yes hijo?"
    mc "May I ask where this classroom is?"
    guard "Ah! Just go to the building on your left and then that classroom is located on the 3rd floor."

    hide guard normal
    with moveoutleft
    mc "Thank you po, Kuya!"
    mc "Hmm.."
    mc "Now that I know where my room will be, it's time to kill some time."


    menu:
        "Go LEFT to JFH Building":
            jump path_to_jfh
        "Go MIDDLE to University Lane":
            jump path_to_univlane
        "Go RIGHT to ICT Buiilding":
            jump path_to_ict

# Path Decisions
label path_to_jfh:
    mc "Guess I’ll just head straight to the classroom."
    scene bg black with fade
    scene bg jfhoutside
    pause(3.0)
    jump third_floor_jfh

label path_to_univlane:
    scene bg ulane
    mc "Hmm.."
    mc "There's a cluster of people over there. I might want to avoid getting their attention. It'll be overwhelming to talk to that amount of people this early in the morning."
    mc "Let me just sit here, quietly and peacefull-"
    show friend_1
    with moveinleft
    stranger "Heya dude! Are ya here to join the Arts Club as well? The name's Charles, I'm a computer science freshman. May I seat next to you?"
    mc "H-hi, I'm ___, same department as you. Yeah you can sit he--"
    mc "“Woah! A comsci comrade? And he's joining the Arts club too? What great news to start the day!”"
    mc "Umm...sorry, I don't think I'm joining the Art Club."
    charles "Aww, bummer. It's fine though, its more fun to join a club that fits your interests!"
    charles "Oh where's your classroom gonna be? MIne's in JFH302. Dang, third floor's tough."
    mc "Oh, mine's there too."
    charles "Sweet! We're blockmates then! Glad to be making friends with ya already."
    mc "Yeah, same."
    charles "Come on, let's start walking up those flight of stairs. Our orientation should start soon the moment we reached the classroom."
    mc "Okay."
    "..."

    jump path_to_jfh  # Redirects to JFH302 path

label path_to_ict:
    scene bg ictbuilding
    mc "I’ll just check there later before my Intro to Programming class."
    mc "I don’t think I should waste time here before orientation."
    mc "Let’s just head to the classroom."
    jump path_to_jfh  # Redirects to JFH302 path

# Third Floor - JFH Building
label third_floor_jfh:
    scene bg jfhhallway
    with fade
    mc "Haa..Ha-..Ha.. Why is there no elevator here?! This sucks."

    play sound "footsteps.ogg"
    "{i}*Footsteps*{/i}"
    play sound "door_open.ogg"
    "{i}*door opens*{/i}"

    scene bg jfh301 with dissolve
    "{i}Professor Arrives{/i}"
    show miss_professor normal at center with dissolve
    "{i}...Lesson - Introduction to HELLO WORLD!...{/i}"
    "..."
    professor "Good morning, class! Today, we’re diving into the basics of programming in Python."
    professor "Python is a versatile and beginner-friendly language, perfect for developing everything from websites to artificial intelligence."
    professor "Let's start with the most basic building block of any programming language: printing text to the screen."
    mc "I'm bored..."
    menu:
        "continue listening to the discussion":
            jump path_continue_listening
        "play pen spinning mini-game":
            scene bg pen with dissolve
            jump timing_minigame
    return

label path_to_foodsquare:
    show class_rep at left
    with moveinleft

    classrep "Yo, wanna join us to eat at the food square?"
    menu:
        "YES":
            mc "U-huh, yeah okay I'm down."
        "NO":
            mc "Oh thanks. I'll join you next time.. I have something else to do first and.. I'm not that hungry yet."
            mc "{i}Blatant lies. What important thing is there to do other than eat lunch?{/i}"
    
    classrep "Call out to us when you got there, yeah? See ya."
    mc "Yeah, see ya."
    hide class_rep
    with moveoutleft
    mc "Guess I'll just wait for a bit before going to the food square. Hope they don't spot me though."
    jump food_square
    return

label food_square:
    # Scene with food square and classrep
    scene bg foodsquare1 with fade
    show class_rep at center
    with dissolve

    # Sound effects for ambiance
    play sound "chatter_and_sizzle.mp3"

    # Class Rep's opening dialogue
    classrep "Hey, looks like the food square is busy today. You getting anything?"
    classrep "I heard they’ve got some new dishes today. Are you gonna try them?"
    
    mc "Oh, definitely. The smell here is making me more hungry by the second."
    mc "Hmm.. There seems to be a queue over here. Must mean that they got the goodies, right? I'll just try it then."
    hide class_rep 
    with dissolve

    jump mg_knapsack
    return

label food_square_after_knapsack:
    scene bg foodsquare2 with fade
    show mc normal with dissolve
    mc "I'll savor every bite of this scrumptious meal."
    
    # Sound effects for eating
    play sound "nom_nom.mp3"
    mc "Man, that hits the spot!"
    
    mc "If I eat like this everyday, the financial damage would probably be astronomical!"
    
    # Comedic overfull reaction
    mc "Ughh, I'm so full... *burp* I want to just lie down and sleep."
    
    mc "I can't though. I still have my class for today and it's a laboratory class in the ICT building."

    show mc normal at right
    with moveinright

    show class_rep at left
    with moveinleft

    # Class Rep Interaction
    classrep "Haha, I knew you'd be full after that. Looks like you're ready for a nap!"
    
    mc "Yeah, I might need one. But I can't skip class."
    
    classrep "I hear you. By the way, I’ll be heading to the ICT building soon too. Care to join me on the walk there?"
    menu:
        "Sure, I'd like that.":
            mc "Yeah, sure! Let's go together."
        "Maybe next time.":
            mc "Thanks, but I'll pass this time. I've got something else to do, and... I'm still feeling full from lunch."
            classrep "You'll be fine! Let's walk together!"

    mc "Alright, guess it’s nice to have some company to help me walk off this meal."

    # Start Pathfinding Mini-Game or Activity
    mc "Alright, let's head out, but I bet it'll be a challenge to get through the crowds here!"

    # Insert mini-game or a pathfinding challenge
    jump pathfinding_mini_game  # Jump to the pathfinding mini-game

    return

label path_continue_listening:
    scene bg jfh301 with dissolve
    show miss_professor normal at center with dissolve
    professor "In Python, we use the 'print()' function to display messages or data. Here's an example:"
    professor "{i}print('Hello, world!'){/i}"
    professor "When you run this code, it will display the text 'Hello, world!' on the screen."
    professor "Break time! Do whatever you want for now. Let's continue our discussion in 20 minutes."
    hide miss_professor normal
    with moveoutleft
    show mc normal at right
    with moveinright

    # Interaction Options
    menu:
        "Practice your pen spinning skills":
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
            jump path_to_foodsquare
            return
    
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
    show bg food with fade
    mc "NOM NOm!"
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
