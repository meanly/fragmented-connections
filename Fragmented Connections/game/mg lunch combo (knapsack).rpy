init python:
    # Define the FoodItem class
    class FoodItem:
        def __init__(self, name, cost, value):
            self.name = name
            self.cost = cost
            self.value = value

    # Create the food menu
    food_items = [
        FoodItem("Burger", 15, 40),
        FoodItem("Pizza", 25, 50),
        FoodItem("Soda", 10, 20),
        FoodItem("Fries", 10, 15),
        FoodItem("Salad", 20, 30),
    ]

    # Calculate total cost and value of selected items
    def calculate_total(selected_items):
        total_cost = sum(item.cost for item in selected_items)
        total_value = sum(item.value for item in selected_items)
        return total_cost, total_value

    # Generate flavor text based on total value
    def generate_flavor_text(total_value):
        if total_value < 50:
            return "You feel slightly hungry and unsatisfied."
        elif 50 <= total_value < 100:
            return "You feel full and satisfied."
        else:
            return "You feel overly stuffed but happy."

label lunch_combo_minigame:
    # Budget and selected items
    $ budget = 50
    $ selected_items = []

    # Game interface
    screen lunch_combo_screen:
        # Frame for title
        frame:
            xalign 0.5
            yalign 0.1
            text "Lunch Combo Minigame" size 40

        # Frame for budget and totals
        frame:
            xalign 0.5
            yalign 0.2
            text "Budget: ₱{} \nTotal Cost: ₱{} \nTotal Value: {}".format(
                budget, calculate_total(selected_items)[0], calculate_total(selected_items)[1]
            )

        # Frame for selecting food items
        frame:
            xalign 0.5
            yalign 0.5
            vbox:
                # Display food items as buttons
                for item in food_items:
                    button:
                        text f"{item.name} (₱{item.cost}, {item.value} value)"
                        action If(
                            calculate_total(selected_items)[0] + item.cost <= budget,
                            [
                                Function(selected_items.append, item),
                                Function(renpy.restart_interaction)
                            ]
                        )

        # Frame for finish selection button
        frame:
            xalign 0.5
            yalign 0.8
            textbutton "Finish Selection" action Return()

    # Show the screen
    call screen lunch_combo_screen

    # Calculate totals
    $ total_cost, total_value = calculate_total(selected_items)
    $ flavor_text = generate_flavor_text(total_value)

    # Create formatted strings for the total cost and value
    $ total_display = "Total Cost: ₱{} \nTotal Value: {}".format(total_cost, total_value)
    $ flavor_display = "Flavor Text: {}".format(flavor_text)

    # Call the results screen to display totals
    call screen result_screen

screen result_screen:
    # Display result information on screen using frame
    frame:
        xalign 0.5
        yalign 0.2
        text total_display size 30

    frame:
        xalign 0.5
        yalign 0.4
        text flavor_display size 30

    frame:
        xalign 0.5
        yalign 0.6
        textbutton "Continue" action Return()

label result_screen_label:
    # This is where the result screen is called and displayed
    $ total_cost, total_value = calculate_total(selected_items)
    $ flavor_text = generate_flavor_text(total_value)

    $ total_display = "Total Cost: ₱{} \nTotal Value: {}".format(total_cost, total_value)
    $ flavor_display = "Flavor Text: {}".format(flavor_text)

    # Call the screen to display the results
    call screen result_screen

    jump food_square_after_knapsack

    return
