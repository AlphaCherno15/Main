def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move_foward():
    while front_is_clear() is True and right_is_clear() == True:
        move()
    while front_is_clear() is True and right_is_clear() != True:
        if at_goal() == False:
            if front_is_clear() is True:
                move()
            #else:
                #turn_left
        else:
            break
    if front_is_clear() != True and at_goal() == False:
        if right_is_clear() == True:
            turn_right()
            move()
        else:
            turn_left()
    if front_is_clear() is True and right_is_clear() == True and at_goal() == False:
       turn_right()
       move()
while at_goal() == False:
    move_foward()
