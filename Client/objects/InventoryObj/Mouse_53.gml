if(PointInBox(window_mouse_get_x(),window_mouse_get_y(),x_pos,y_pos,220,8)){
	drag = true
	x_offset = window_mouse_get_x() - x_pos
	y_offset = window_mouse_get_y() - y_pos
}