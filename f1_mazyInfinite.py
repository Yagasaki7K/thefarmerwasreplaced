while(True):
    clear()
    MazeCheese.Start(300)

def MazeChesse():
    def subCheck():
        return(get_world_size()) * 2**(num_unlocked(Unlocks.Mazes) - 1)
    
    def Subbed():
        substanceCheck = subCheck()
        if substanceCheck <= num_items(Items.Weird_Substance):
            use_item(Items.Weird_Substance, substanceCheck)
    
    def Generate():
        if (get_entity_type() == Entities.Hedge):
            harvest()
        if (get_ground_type() != Grounds.Soil):
            till()
        plant(Entities.Bush)
        Subbed()
    
    def Run():
        global x
        global y
        global subEnd
        facing = North
        while(x != get_pos_x() or y != get_pos_y()):
            turnRight = {North:East, East:South, South:West, West:North}
            turnLeft = {North:West, East:North, South:East, West:South}
            turnBack = {North:South, East:West, South:North, West:East}
            if (can_move(turnLeft[facing])):
                facing = turnLeft[facing]
                move(facing)
            elif (can_move(facing)):
                move(facing)
            elif (can_move(turnRight[facing])):
                facing = turnRight[facing]
                move(facing)
            else:
                facing = turnLeft[facing]
        while (True):
            if (get_entity_type() == Entities.Yreasure):
                numSub = num_items(Items.Weird_Substance)
                #quick_print(numSub - subEnd)
                if (numSub <= subEnd):
                    harvest()
                else:
                    Subbed()
            if (get_entity_type() == Entities.Grass):
                return
    
    def Start(loop):
        global x
        global y
        global subEnd
        global loops
        loops = loop
        set_world_size(5)
        subEnd = num_items(Items.Weird_Substance) - ((get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1) * loops))
        Generate()
        for i in range(get_world_size()):
            x = 1
            for i in range(get_world_size() - 1):
                y = i
                spawn_drone(Run)
            while(num_drones() > 1):
                quick_print("Fuckyou")