# Update Script for 15x15

def correct_ground_for(crop):
    if crop in (Entities.Tree, Entities.Grass):
        return Grounds.Grassland
    return Grounds.Soil


def handle_tile(crop, replant_dead=False):
    # comment this harvest() if you want a big pumpkin
    harvest()
    if Items.Weird_Substance:
        use_item(Items.Weird_Substance)
        
    if get_entity_type() != Entities.Pumpkin:
        harvest()
        plant(Entities.Pumpkin)

    correct_ground = correct_ground_for(crop)
    if get_ground_type() != correct_ground:
        till()

    if replant_dead and Entities.Dead_Pumpkin:
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
    if get_entity_type() == Entities.Treasure:
        harvest()

    elif y in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14):
        if can_harvest() or Entities.Dead_Pumpkin:
            handle_tile(Entities.Pumpkin)
        move_next()


    elif y == 15:
        if can_harvest() or Entities.Dead_Pumpkin:
            handle_tile(Entities.Pumpkin)
        move(East)
        move(North)
        
