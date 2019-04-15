if not is_undefined(ds_map_find_value(items,item_id)){
	var char_info = items[? item_id]
	x = char_info[? "x"]
	y = char_info[? "y"]
}
else{
	//Destroy instance and clean up references
	ds_map_delete(items,item_id)
	instance_destroy(self)
}

