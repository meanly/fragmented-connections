# Define a new label for the pathfinding minigame
label campus_pathfinding:
    # Show introductory text
    "You need to navigate through campus to get to your next class."

    # Display the map screen
    call screen campus_map

    # Add a penalty for being late or any additional effects here
    $ player_late = False  # Example variable for late penalty
    
    if player_late:
        "You were late and missed some important class content!"
    
    return

# Define the campus map screen
screen campus_map:
    # Image representation of the campus with paths, obstacles, and collectibles
    imagemap:
        ground "campus_map.png"  # Background image of the campus map
        hotspot (50, 100, 100, 50) action Jump("path_1")  # Path 1
        hotspot (200, 150, 100, 50) action Jump("path_2")  # Path 2
        hotspot (350, 200, 100, 50) action Jump("path_3")  # Path 3
        hotspot (500, 250, 100, 50) action Jump("path_4")  # Path 4
        hotspot (600, 50, 100, 50) action Jump("path_5")  # Path 5

# Define paths the player can take
label path_1:
    "You choose to move down Path 1. But wait, there's an obstacle!"
    
    # Check if the player successfully avoids the obstacle or collects something
    $ player_obstacle = renpy.random.choice([True, False])  # Random chance for an obstacle
    
    if player_obstacle:
        "There's a crowd blocking the way! You lose some time."
        $ player_late = True  # Mark the player as late
    else:
        "You successfully avoid the crowd and move ahead."

    return

label path_2:
    "You choose Path 2. There's a shortcut here, but it might be risky."
    
    # Random chance for a collectible or penalty
    $ player_collectible = renpy.random.choice([True, False])
    
    if player_collectible:
        "You find a book along the way! (+5 points)"
        # Add points or collectible effect here
        $ player_points += 5
    else:
        "No collectibles, but you're moving swiftly."

    return

label path_3:
    "You decide to take Path 3, but it's a busy hallway. You have to wait."
    
    $ player_wait_time = renpy.random.randint(1, 3)  # Random waiting time between 1 to 3 minutes
    
    "You wait for {player_wait_time} minutes, and lose some time."
    $ player_late = True  # Mark the player as late
    
    return

label path_4:
    "Path 4 seems clear. You’re making good progress!"
    
    # No obstacles, but the player could still lose points if time is tight
    $ player_tight_time = renpy.random.choice([True, False])
    
    if player_tight_time:
        "You’re running out of time! You hurry to class."
        $ player_late = True
    
    return

label path_5:
    "Path 5 is a quiet walk through the campus garden. You relax and enjoy the scenery."
    
    # Optional: Include a relaxing effect or bonus for taking a calm route
    $ player_points += 10  # For relaxing and gaining points

    return

# After completing the pathfinding
label end_campus_pathfinding:
    "You made it to your class!"
    
    if player_late:
        "You were late to class, but at least you’re here."
    else:
        "You arrived on time. Great job navigating campus!"

    # Show final points or status
    "Your final points: [player_points]"
    return
