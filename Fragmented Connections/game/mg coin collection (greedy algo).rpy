init python:
    # Function to generate a random price for the challenge
    import random

    def generate_price():
        return random.randint(20, 100)

    # Calculate total coins collected
    def calculate_coins(collected_coins):
        return sum(collected_coins)

    # Calculate the optimal number of coins to reach the target price
    def calculate_optimal_coins(target_price, available_coins):
        remaining = target_price
        optimal_coins = []
        # Use the greedy algorithm: prioritize higher denominations
        for coin in sorted(available_coins, reverse=True):
            while remaining >= coin:
                optimal_coins.append(coin)
                remaining -= coin
        return optimal_coins

    # Evaluate efficiency based on the number of coins used
    def evaluate_efficiency(target_price, collected_coins, available_coins):
        total_collected = calculate_coins(collected_coins)
        total_coins_used = len(collected_coins)
        optimal_coins = calculate_optimal_coins(target_price, available_coins)
        optimal_coins_used = len(optimal_coins)

        if total_collected != target_price:
            return "Inefficient! Total collected does not match the target."
        elif total_coins_used > optimal_coins_used:
            return "Inefficient! You used {} coins, but the optimal way only uses {} coins.".format(
                total_coins_used, optimal_coins_used
            )
        elif total_coins_used == optimal_coins_used:
            return "Efficient! You matched the optimal way with {} coins.".format(optimal_coins_used)
        else:
            return "Amazing! You used fewer coins than the optimal solution ({} coins)!".format(optimal_coins_used)

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
    $ optimal_coins = calculate_optimal_coins(target_price, available_coins)
    $ efficiency_message = evaluate_efficiency(target_price, collected_coins, available_coins)

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
        text "Optimal Coins Used: {} ({})".format(
            len(optimal_coins), ", ".join("₱{}".format(c) for c in optimal_coins)
        ) size 30

    frame:
        xalign 0.5
        yalign 0.6
        text efficiency_message size 30

    frame:
        xalign 0.5
        yalign 0.7
        textbutton "Continue" action Return()
