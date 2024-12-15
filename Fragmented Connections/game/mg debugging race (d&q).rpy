init python:
    import time

    # Buggy code snippets with sections (more complex examples)
    code_snippets = [
        {
            "buggy_code": "pritn('Hello World')", 
            "sections": [
                {"code": "pritn", "is_buggy": True, "choices": ["print", "pritn", "pint"], "correct_fix": 0},
                {"code": "('Hello World')", "is_buggy": False, "choices": ["('Hello World')", "('Hello world'))", "('hello Worldd)"], "correct_fix": 0}
            ],
            "correct_combined_code": "print('Hello World')"
        },
        {
            "buggy_code": "def add(num1, num2): retun num1 + num2",
            "sections": [
                {"code": "def", "is_buggy": False, "choices": ["def", "function", "method"], "correct_fix": 0},
                {"code": "add", "is_buggy": False, "choices": ["add", "sum", "addition"], "correct_fix": 0},
                {"code": "(", "is_buggy": False, "choices": ["(", "<", "{"], "correct_fix": 0},
                {"code": "retun", "is_buggy": True, "choices": ["return", "retun", "retn"], "correct_fix": 0},
                {"code": "num1 + num2", "is_buggy": False, "choices": ["num1 + num2", "num1 - num2", "num1 * num2"], "correct_fix": 0}
            ],
            "correct_combined_code": "def add(num1, num2): return num1 + num2"
        },
        {
            "buggy_code": "for i in range(10 print(i))",
            "sections": [
                {"code": "for", "is_buggy": False, "choices": ["for", "each", "while"], "correct_fix": 0},
                {"code": "i in range(10", "is_buggy": False, "choices": ["i in range(10", "i in range(0, 10)", "for i in range()"], "correct_fix": 1},
                {"code": "print(i))", "is_buggy": True, "choices": ["print(i)", "print(i))", "print(i)))"], "correct_fix": 0}
            ],
            "correct_combined_code": "for i in range(10): print(i)"
        },
        {
            "buggy_code": "def calc_total(price, tax): total = price * tax + 10 totalreturn total",
            "sections": [
                {"code": "def", "is_buggy": False, "choices": ["def", "function", "method"], "correct_fix": 0},
                {"code": "calc_total", "is_buggy": False, "choices": ["calc_total", "calculate_total", "total_calculate"], "correct_fix": 0},
                {"code": "price, tax", "is_buggy": False, "choices": ["price, tax", "amount, tax", "price, tax, discount"], "correct_fix": 0},
                {"code": "total = price * tax + 10", "is_buggy": False, "choices": ["total = price * tax + 10", "total = price + tax", "total = price * tax"], "correct_fix": 0},
                {"code": "totalreturn", "is_buggy": True, "choices": ["return total", "totalreturn", "return calc_total"], "correct_fix": 0}
            ],
            "correct_combined_code": "def calc_total(price, tax): total = price * tax + 10 return total"
        }
    ]

    # Shuffle snippets for randomness (optional)
    import random
    random.shuffle(code_snippets)

    # Debugging function to check selected snippets
    def debug_snippets(selected_snippets):
        score = sum(1 for snippet in selected_snippets if snippet["is_buggy"] == False)
        return score


# Label to initiate the mini-game
label start_debugging_race:
    $ selected_snippets = []  # Player's selections
    $ total_score = 0  # Track player's debugging accuracy
    $ timer_start = time.time()  # Start timer

    "Welcome to the Debugging Race!"
    "Find and fix as many bugs as you can within the time limit."

    # Call the mini-game screen
    call screen debugging_screen

    # Timer logic to automatically end the game
    $ time_taken = time.time() - timer_start
    if time_taken > 30:
        "Time's up! You found [total_score] bugs in [time_taken:.2f] seconds."
    else:
        if total_score > 2:
            "You found [total_score] bugs in [time_taken:.2f] seconds! Impressive work!"
        else:
            "You found only [total_score] bugs in [time_taken:.2f] seconds. Better luck next time."

    return


# Debugging Race Screen
screen debugging_screen:
    tag debugging_game

    # Timer at the top of the screen
    frame:
        align (0.5, 0.1)
        text "Timer: [30 - (time.time() - timer_start)]s"  # Display remaining time

    # Instructions
    vbox:
        align (0.5, 0.2)
        spacing 10
        text "Click on the buggy lines of code to fix them!"

    # Display code snippets
    vbox:
        align (0.5, 0.5)
        spacing 15
        for i, snippet in enumerate(code_snippets):
            textbutton snippet["buggy_code"] action If(
                not snippet["buggy_code"] in selected_snippets,
                [
                    SetVariable("selected_snippets", selected_snippets + [snippet["buggy_code"]]),
                    Call("divide_and_fix", snippet)
                ]
            )


# Divide and fix the buggy code
label divide_and_fix(snippet):
    $ section_index = 0
    $ fixed_sections = []

    # Show full buggy line before the player starts fixing it
    $ full_code = snippet["buggy_code"]
    "Here's the full buggy line: [full_code]"

    # Divide the buggy code into sections and show them one by one
    while section_index < len(snippet["sections"]):
        $ current_section = snippet["sections"][section_index]
        $ correct_choice = current_section["correct_fix"]
        $ choices = current_section["choices"]
        $ current_code = "".join([s["code"] for s in snippet["sections"][:section_index]])

        # Show the section that needs fixing, with context
        $ divided_code = current_code + current_section["code"] + "".join([s["code"] for s in snippet["sections"][section_index + 1:]])
        "Current section to fix: [current_section['code']]"
        "Current code with context: [divided_code]"

        # Present the choices for the current section
        menu:
            "How would you fix this section? The section to fix is: [current_section['code']]"
            "Option 1: [choices[0]]":
                $ selected_choice = 0
            "Option 2: [choices[1]]":
                $ selected_choice = 1
            "Option 3: [choices[2]]":
                $ selected_choice = 2

        # Check if the player selected the correct fix
        if selected_choice == correct_choice:
            $ fixed_sections.append(choices[selected_choice])
            "Correct fix! You've fixed this section."
            $ section_index += 1
        else:
            "Oops, that's not the right fix. Try again!"

    # After all sections are fixed, combine them into the correct code
    $ final_code = "".join(fixed_sections)
    if final_code == snippet["correct_combined_code"]:
        $ total_score += 1
        "Great job! You've fixed the whole line of code: [final_code]."
    else:
        "Something went wrong, try again."

    return
