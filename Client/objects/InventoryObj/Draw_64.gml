display_set_gui_maximize(1,1,0,0)

if (drag){
	x_pos = window_mouse_get_x() - x_offset 
	y_pos = window_mouse_get_y() - y_offset
}

draw_sprite_ext(InventorySprite,0,x_pos,y_pos,1,1,0,c_white,1)
