# A better version of main.py (12x12), and fixed every bugs and errors.
def handle_tile(crop, replant_dead=False):
    if can_harvest():
        harvest()

    if get_ground_type() != Grounds.Soil:
        till()

    if replant_dead and Entities.Dead_Pumpkin:
        plant(crop)
    else:
        plant(crop)

    if Items.Water != 0:
        use_item(Items.Water)


def move_next():
    move(North)


while True:
    y = get_pos_y()

    if y in (0, 1):
        handle_tile(Entities.Carrot)
        move_next()

    elif y in (2, 3, 9, 10):
        if can_harvest() or Entities.Dead_Pumpkin:
            handle_tile(Entities.Pumpkin)
        move_next()

    elif y == 4:
        harvest()
        plant(Entities.Grass)
        if Items.Water != 0:
            use_item(Items.Water)
        move_next()

    elif y in (5, 6):
        if can_harvest():
            handle_tile(Entities.Tree)
        move_next()

    elif y == 7:
        handle_tile(Entities.Sunflower)
        move_next()

    elif y == 8:
        handle_tile(Entities.Cactus)
        move_next()

    elif y == 11:
        harvest()
        if get_ground_type() != Grounds.Soil:
            till()
        plant(Entities.Grass)
        if Items.Water != 0:
            use_item(Items.Water)
        move(East)
        move(North)
        
