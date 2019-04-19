if(PointInBox(window_mouse_get_x(),window_mouse_get_y(),WindowsController.friends_pos[0],WindowsController.friends_pos[1],220,8)){
	drag = true
	x_offset = window_mouse_get_x() - WindowsController.friends_pos[0]
	y_offset = window_mouse_get_y() - WindowsController.friends_pos[1]
}