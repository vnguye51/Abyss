
if(PointInBox(window_mouse_get_x(),window_mouse_get_y(),x_pos,y_pos+180,x_pos+220,y_pos+300)){
	item_x = floor((window_mouse_get_x()-x_pos)/20)
	item_y = floor((window_mouse_get_y()-(y_pos+180))/20)
	
	curr_item_index = item_x+item_y*11
	var item = inventory_items[| curr_item_index]
	item.drag = true
}
else{
	curr_item_index = -1
}

