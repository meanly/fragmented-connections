init python:
    # Function to generate a random price for the challenge
    import random

    def generate_price():
        return random.randint(20, 100)

    # Calculate total coins collected
    def calculate_coins(collected_coins):
        return sum(collected_coins)

    # Evaluate efficiency based on the number of coins used
    def evaluate_efficiency(target_price, collected_coins):
        total_coins_used = len(collected_coins)
        if calculate_coins(collected_coins) != target_price:
            return "Inefficient! Total collected does not match the target."
        elif total_coins_used == 1:
            return "Perfect! You used only one coin."
        elif total_coins_used <= 3:
            return "Efficient! You used {} coins.".format(total_coins_used)
        else:
            return "Inefficient! You used too many coins ({}).".format(total_coins_used)

label start_coincollect:
    # Set initial variables
    $ target_price = generate_price()
    $ collected_coins = []
    $ available_coins = [1, 5, 10, 20]  # Available coin denominations

    # Game interface
    screen coin_collect_screen:
        # Frame for title
        frame:
            xalign 0.5
            yalign 0.1
            text "Coin Collect Minigame" size 40

        # Frame for target and current total
        frame:
            xalign 0.5
            yalign 0.2
            text "Target Price: ₱{} \nCollected Total: ₱{}".format(
                target_price, calculate_coins(collected_coins)
            )

        # Frame for coin selection
        frame:
            xalign 0.5
            yalign 0.5
            vbox:
                for coin in available_coins:
                    button:
                        text f"Add ₱{coin}"
                        action If(
                            calculate_coins(collected_coins) + coin <= target_price,
                            [
                                Function(collected_coins.append, coin),
                                Function(renpy.restart_interaction)
                            ]
                        )

        # Frame for finish button
        frame:
            xalign 0.5
            yalign 0.8
            textbutton "Finish" action Return()

    # Show the screen
    call screen coin_collect_screen

    # Evaluate results
    $ total_collected = calculate_coins(collected_coins)
    $ efficiency_message = evaluate_efficiency(target_price, collected_coins)

    # Display the results
    call screen coin_result_screen

    return

screen coin_result_screen:
    # Display result information
    frame:
        xalign 0.5
        yalign 0.3
        text "Collected Total: ₱{}".format(calculate_coins(collected_coins)) size 30

    frame:
        xalign 0.5
        yalign 0.4
        text "Coins Used: {}".format(len(collected_coins)) size 30

    frame:
        xalign 0.5
        yalign 0.5
        text efficiency_message size 30

    frame:
        xalign 0.5
        yalign 0.7
        textbutton "Continue" action Return()
