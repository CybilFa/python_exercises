def eat_ghost(has_pellet_active, touch_ghost):
    if has_pellet_active and touch_ghost:
        return True
    return False

print('Whether pacman has eaten ghost', eat_ghost(False, True))


def score(touch_pellet, touch_dot):
    if touch_pellet or touch_dot:
        return True
    return False

print("Whether the pacman is touching a dot or a ghost",score(True, True))

def lose(has_pellet_active, touch_ghost):
    if not has_pellet_active and touch_ghost:
        return True
    return False

print("Whther a pacman is touching a ghost or does not has power pellet active", lose(False, True))

def win(has_eaten_dots, has_pellet_active, touch_ghost):
    if has_eaten_dots and not lose(has_pellet_active, touch_ghost):
        return True
    return False

print('If pacman has eaten all dots and not lose based on part 3', win(False, True, False))
