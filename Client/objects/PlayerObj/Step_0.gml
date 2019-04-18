if not is_undefined(ds_map_find_value(players,player_id)){
	var char_info = players[? player_id]
	x = char_info[? "x"]
	y = char_info[? "y"]
	image_index = char_info[? "frame"]
}
else{
	//Destroy instance and clean up references
	ds_map_delete(players,player_id)
	instance_destroy(self)
}
