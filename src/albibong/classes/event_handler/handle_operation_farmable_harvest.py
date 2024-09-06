from albibong.classes.world_data import WorldData


def handle_operation_farmable_harvest(world_data: WorldData, parameters):
    if type(world_data.current_map).__name__ == "Island":
        for i in range(len(parameters[0])):
            world_data.current_map.add_crop(
                unique_name=parameters[0][i], quantity=parameters[1][i]
            )


def handle_operation_farmable_get_product(world_data: WorldData, parameters):
    if type(world_data.current_map).__name__ == "Island":
        for i in range(len(parameters[0])):
            world_data.current_map.add_animal(
                unique_name=parameters[0][i], quantity=parameters[1][i]
            )
