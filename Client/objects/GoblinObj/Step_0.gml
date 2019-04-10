if not is_undefined(ds_map_find_value(enemies,enemy_id)){
	var char_info = enemies[? enemy_id]
	x = char_info[? "x"]
	y = char_info[? "y"]
	image_index = char_info[? "frame"]
}
else{
	//Destroy instance and clean up references
	ds_map_delete(enemies,enemy_id)
	instance_destroy(self)
}

