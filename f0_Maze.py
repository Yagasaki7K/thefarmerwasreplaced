# Update to Added Drones
# Clear before start
# Minimal world seed

clear()

def TransformToMaze():
    plant(Entities.Bush)
    n_substance = get_world_size() * num_unlocked(Unlocks.Mazes)
    use_item(Items.Weird_Substance, n_substance)
    set_world_size(3)

def drone_function():
    move(North)
    harvestMaze()

def harvestMaze():
    while True:
        if get_entity_type() != Entities.Hedge:
            TransformToMaze()
            
        if get_entity_type() == Entities.Treasure:
            harvest()
        
        visited = []  # Persistente para rastrear posições
        move_history = []  # Rastreia últimos 3 movimentos
        
        spawn_drone(drone_function)
        max_drones()
        if get_entity_type() == Entities.Hedge:
            index = 0
            directions = [North, East, South, West]
            max_steps = get_world_size() * get_world_size() * 2
            steps = 0
            while get_entity_type() != Entities.Treasure and steps < max_steps:
                pos = (get_pos_x(), get_pos_y())
                # Verifica repetição de 3 movimentos
                if len(move_history) >= 6 and move_history[-6::2] == move_history[-3::]:  # Mesmas 3 últimas posições
                    # Reinicia: move para (0,0) e muda direção inicial
                    x = get_pos_x()
                    y = get_pos_y()
                    while x > 0:
                        move(West)
                        x = x - 1
                    while y > 0:
                        move(South)
                        y = y - 1
                    index = (index + 1) % 4  # Nova direção inicial
                    visited = []  # Reseta histórico
                    move_history = []
                if pos not in visited:
                    visited.append(pos)
                move_history.append(pos)
                right_index = (index + 1) % 4
                if move(directions[right_index]):
                    index = right_index
                elif move(directions[index]):
                    pass
                else:
                    index = (index - 1) % 4
                steps = steps + 1
            if get_entity_type() == Entities.Treasure:
                harvest()
                next_pos = measure()
                if next_pos:
                    x, y = next_pos
                    while get_pos_x() != x or get_pos_y() != y:
                        if get_pos_x() < x:
                            move(East)
                        elif get_pos_x() > x:
                            move(West)
                        if get_pos_y() < y:
                            move(North)
                        elif get_pos_y() > y:
                            move(South)
        
        y = get_pos_y()
        
        if y == get_world_size() - 1:
            move(East)
            
harvestMaze()
