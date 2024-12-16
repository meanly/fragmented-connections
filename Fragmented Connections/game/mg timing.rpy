init 15 python:
    fable_minigame_bar = 90
    fable_minigame_score = 0
    fable_you_press_button = 0
init:
    transform fable_point_move(frp):
        subpixel True
        rotate_pad True
        align(0.5,1.22)
        rotate frp

screen fable_2_minigame:
    add "minigame-timing/Fable_bar.png" align(0.5,0.5)
    add "minigame-timing/Fable_point.png" at fable_point_move(fable_minigame_bar)
    text "Instructions: Try to hit the green bar then press enter.\n" align(0.5,0.1)
    text "\nScore: [fable_minigame_score]" align(0.5,0.1)
    text "[fable_minigame_bar]\nBar Value" align(0.5,0.2)
    text "[fable_you_press_button]" align(0.5,0.3)

    # Add the quit button
    textbutton "Quit Mini-Game" action Jump("end_minigame") align(0.5, 0.9)

    if fable_minigame_bar >= -14 and fable_minigame_bar <= 14:
        key "K_SPACE":
            if fable_you_press_button == 0:
                if fable_minigame_score < 14:
                    action [SetVariable("fable_minigame_score", fable_minigame_score + 1), SetVariable("fable_you_press_button", fable_you_press_button + 1), Show("you_press_button_good")]
                else:
                    action Jump("end_minigame")
            elif fable_you_press_button == 1:
                action SetVariable("fable_minigame_score", fable_minigame_score + 0)
    else:
        key "K_SPACE" action [SetVariable("fable_minigame_score", 0), Show("you_press_button_bad")]

screen fable_timer_left:
    timer 0.0001 repeat True action [If(fable_minigame_bar >= -90, SetVariable("fable_minigame_bar", fable_minigame_bar - 2)),If(fable_minigame_bar == -90, Hide("fable_timer_left"), Show("fable_timer_right")), If(fable_minigame_bar == -90, SetVariable("fable_you_press_button", 0))]

screen fable_timer_right:
    timer 0.0001 repeat True action [If(fable_minigame_bar <= 90, SetVariable("fable_minigame_bar", fable_minigame_bar + 2)),If(fable_minigame_bar == 90, Hide("fable_timer_right"), Show("fable_timer_left")), If(fable_minigame_bar == 90, SetVariable("fable_you_press_button", 0))]

screen you_press_button_good:
    text "{color=#1e8e00}Excellent!{/color}" at fable_move_good
    timer 0.5 action Hide("you_press_button_good")

screen you_press_button_bad:
    #hbox at fable_move_bad:
    text "{color=#950000}woops..\nbad timing. try again!{/color}" at fable_move_bad
    timer 0.5 action Hide("you_press_button_bad")

transform fable_move_good:
    align(0.5,0.5)
    linear 0.05 zoom 1.3
    linear 0.5 zoom 1.0 alpha 0.0

transform fable_move_bad:
    align(0.5,0.5)
    linear 0.04 xalign 0.5
    linear 0.06 xalign 0.495
    linear 0.06 xalign 0.515
    linear 0.06 xalign 0.5
    linear 0.5 alpha 0.0

################################################################################
label start_minigame:
    show screen fable_timer_left
    call screen fable_2_minigame
################################################################################



label end_minigame: #End minigame. And jump continue game
    hide screen fable_2_minigame
    hide screen fable_timer_left
    hide screen fable_timer_right
    $ renpy.pause(0.3)
    mc "that was fun, but I need to focus."
    jump path_continue_listening #continue game
