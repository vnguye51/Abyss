if not is_undefined(ds_map_find_value(items,item_id)){
	var item_info = items[? item_id]
	x = item_info[? "x"]
	y = item_info[? "y"]
}
else{
	//Destroy instance and clean up references
	ds_map_delete(items,item_id)
	instance_destroy(self)
}

