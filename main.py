# Used in 12x12 with errors in if of use_water and repetitive code.
while True:
        
    if (get_pos_y() == 0):
        harvest()
        
        if (get_ground_type() != Grounds.Soil):
            till()
                
        plant(Entities.Carrot)
        
        if (Items.Water != 0):
            use_item(Items.Water)
        
        move(North)
        
    if (get_pos_y() == 1):
        harvest()
        
        if (get_ground_type() != Grounds.Soil):
            till()
                
        plant(Entities.Carrot)
        
        if (Items.Water != 0):
            use_item(Items.Water)

        move(North)
        
    if (get_pos_y() == 2):
        if (can_harvest()):
            harvest()
            
            if (get_ground_type() != Grounds.Soil):
                till()
                
            plant(Entities.Pumpkin)

            if (Items.Water != 0):
                use_item(Items.Water)
                
            move(North)
        else:
            if (Entities.Dead_Pumpkin):
                plant(Entities.Pumpkin)
                
                if (Items.Water != 0):
                    use_item(Items.Water)
                    
                move(North)
            else:
                move(North)
        
    if (get_pos_y() == 3):
        if (can_harvest()):
            harvest()
            
            if (get_ground_type() != Grounds.Soil):
                till()
                
            plant(Entities.Pumpkin)
            
            if (Items.Water != 0):
                use_item(Items.Water)
                    
            move(North)
        else:
            if (Entities.Dead_Pumpkin):
                plant(Entities.Pumpkin)
                
                if (Items.Water != 0):
                    use_item(Items.Water)
                    
                move(North)
            else:
                move(North)
        
    if (get_pos_y() == 4):
        harvest()
        plant(Entities.Grass)
        
        if (Items.Water != 0):
            use_item(Items.Water)
            
        move(North)
       
    if (get_pos_y() == 5):
        if (can_harvest()):
            harvest()
            plant(Entities.Tree)
            
            if (Items.Water != 0):
                use_item(Items.Water)
                
            move(North)
        else:
            move(North)

    if (get_pos_y() == 6):
        if (can_harvest()):
            harvest()
            plant(Entities.Tree)
            
            if (Items.Water != 0):
                use_item(Items.Water)
                
            move(North)
        else:
            move(North)
        
    if (get_pos_y() == 7):
        harvest()

        if (get_ground_type() != Grounds.Soil):
            till()
                
        plant(Entities.Sunflower)
        
        if (Items.Water != 0):
            use_item(Items.Water)
            
        
        move(North)
        

    if (get_pos_y() == 8):
        harvest()
        
        if (get_ground_type() != Grounds.Soil):
            till()
                
        plant(Entities.Cactus)
       
        if (Items.Water != 0):
            use_item(Items.Water)
        
        move(North)
        
    if (get_pos_y() == 9):
        if (can_harvest()):
            harvest()
            
            if (get_ground_type() != Grounds.Soil):
                till()
                
            plant(Entities.Pumpkin)
            
            if (Items.Water != 0):
                use_item(Items.Water)
                    
            move(North)
        else:
            if (Entities.Dead_Pumpkin):
                plant(Entities.Pumpkin)
                
                if (Items.Water != 0):
                    use_item(Items.Water)
                    
                move(North)
            else:
                move(North)
                
    if (get_pos_y() == 10):
        if (can_harvest()):
            harvest()
            
            if (get_ground_type() != Grounds.Soil):
                till()
                
            plant(Entities.Pumpkin)
            
            if (Items.Water != 0):
                use_item(Items.Water)
                    
            move(North)
        else:
            if (Entities.Dead_Pumpkin):
                plant(Entities.Pumpkin)
                
                if (Items.Water != 0):
                    use_item(Items.Water)
                    
                move(North)
            else:
                move(North)
        
        
    if (get_pos_y() == 11):
        harvest()
        
        if (get_ground_type() == Grounds.Soil):
            till()
                
        plant(Entities.Grass)
        
        if (Items.Water != 0):
            use_item(Items.Water)
        
        move(East)
        move(North)
