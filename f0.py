# A better version of main.py (12x12), and fixed every bugs and errors.
# Filtering a correct ground for the seed.
# Added Fertilizer
# Added Pumpkin 4x12

def correct_ground_for(crop):
    if crop in (Entities.Tree, Entities.Grass):
        return Grounds.Grassland
    return Grounds.Soil


def handle_tile(crop, replant_dead=False):
    if can_harvest():
        harvest()

    correct_ground = correct_ground_for(crop)
    if get_ground_type() != correct_ground:
        till()

    if replant_dead and Entities.Dead_Pumpkin:
        plant(crop)
    else:
        plant(crop)

    if Items.Water != 0:
        use_item(Items.Water)
        
    if Items.Fertilizer != 0:
        use_item(Items.Fertilizer)

def move_next():
    move(North)

while True:
    y = get_pos_y()
    if get_entity_type() == Entities.Treasure:
        harvest()

    if y in (9, 10):
        handle_tile(Entities.Carrot)
        move_next()
        unlock(Unlocks.Speed)

    elif y in (0, 1, 2, 3):
        if can_harvest() or Entities.Dead_Pumpkin:
            handle_tile(Entities.Pumpkin)
        move_next()

    elif y == 4:
        handle_tile(Entities.Grass)
        move_next()

    elif y in (5, 6):
        if can_harvest():
            handle_tile(Entities.Tree)
        move_next()

    elif y in (7, 8):
        handle_tile(Entities.Cactus)
        move_next()

    elif y == 11:
        handle_tile(Entities.Sunflower)
        move(East)
        move(North)
        
