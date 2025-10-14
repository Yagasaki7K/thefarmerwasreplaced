# A better version of main.py (12x12), and fixed every bugs and errors.
# Filtering a correct ground for the seed.
# Added Fertilizer
# Added Pumpkin 4x12
# Update Farming for 15x15
# Fix some issues with dead pumpkins
# Removed Treasure - It belongs to another script now

def correct_ground_for(crop):
    if crop in (Entities.Tree, Entities.Grass):
        return Grounds.Grassland
    return Grounds.Soil


def handle_tile(crop, replant_dead=False):
    if Items.Weird_Substance:
        use_item(Items.Weird_Substance)
        
    if can_harvest():
        harvest()

    correct_ground = correct_ground_for(crop)
    if get_ground_type() != correct_ground:
        till()

    if Entities.Dead_Pumpkin:
        plant(crop)
    else:
        plant(crop)

    if Items.Water:
        use_item(Items.Water)
        
    if Items.Fertilizer:
        use_item(Items.Fertilizer)

def move_next():
    move(North)

while True:
    y = get_pos_y()

    if y in (9, 10, 14):
        handle_tile(Entities.Carrot)
        move_next()

    elif y in (0, 1, 2, 3):
        if can_harvest() or Entities.Dead_Pumpkin:
            handle_tile(Entities.Pumpkin)
        move_next()

    elif y in (4, 11):
        handle_tile(Entities.Grass)
        move_next()

    elif y in (5, 6, 12):
        handle_tile(Entities.Tree)
        move_next()

    elif y in (7, 8, 13):
        handle_tile(Entities.Cactus)
        move_next()

    elif y == 15:
        handle_tile(Entities.Sunflower)
        move(East)
        move(North)
        
