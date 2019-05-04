depth = InventoryObj.depth -1
if(drag){
	x = window_mouse_get_x()-8
	y = window_mouse_get_y()-8
}
else{
	x = InventoryObj.x_pos + origin[0]
	y = InventoryObj.y_pos + origin[1]
}
