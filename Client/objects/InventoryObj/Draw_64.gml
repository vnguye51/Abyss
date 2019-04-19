display_set_gui_maximize(1,1,0,0)

if (drag){
	WindowsController.inventory_pos = [window_mouse_get_x() - x_offset, window_mouse_get_y() - y_offset]
}

draw_sprite_ext(InventorySprite,0,WindowsController.inventory_pos[0],WindowsController.inventory_pos[1],1,1,0,c_white,1)
