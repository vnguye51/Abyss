
//Loop through all windows in stack. If one is clicked on break out of the loop after changing its offset
var i = 0
var j = 0
for(i=ds_list_size(windows_stack)-1;i >= 0;i--){
	var obj = windows_stack[| i]
	if(PointInBox(window_mouse_get_x(),window_mouse_get_y(),obj.x_pos,obj.y_pos,obj.bar_width,obj.bar_height)){
		obj.drag = true
		obj.x_offset = window_mouse_get_x() - obj.x_pos
		obj.y_offset = window_mouse_get_y() - obj.y_pos
		obj.depth = -10
		//Bring object to the front of stack
		ds_list_delete(windows_stack,i)
		ds_list_add(windows_stack,obj)
		for(var j=i;j<ds_list_size(windows_stack)-1;j++){
			var other_obj = windows_stack[| j]
			other_obj.depth = -10 + (ds_list_size(windows_stack)-j)*2
		}
		break
	}
}

