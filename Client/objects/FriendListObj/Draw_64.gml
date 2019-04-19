display_set_gui_maximize(1,1,0,0)

if (drag){
	WindowsController.friends_pos = [window_mouse_get_x() - x_offset, window_mouse_get_y() - y_offset]
}
draw_sprite_ext(sprite,0,WindowsController.friends_pos[0],WindowsController.friends_pos[1],1,1,0,c_white,1)


