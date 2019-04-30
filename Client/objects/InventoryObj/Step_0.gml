if (drag){
	x_pos = window_mouse_get_x() - x_offset 
	y_pos = window_mouse_get_y() - y_offset
	for(var i=0;i<ds_list_size(inventory_items);i++){
		var item = inventory_items[| i]
		item.x = x_pos + 2+20*i
		item.y = y_pos + 182
	}
}