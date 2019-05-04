if(curr_item_index != -1){
	var item = inventory_items[| curr_item_index]
	item.drag = false
	if(not PointInBox(window_mouse_get_x(),window_mouse_get_y(),x_pos,y_pos,width,height)){
		DropItem("gold")
	}
}