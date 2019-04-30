/// @description Insert description here
// You can write your code in this editor
if (ds_list_size(windows_stack) > 0){
	var obj = windows_stack[| ds_list_size(windows_stack)-1]
	obj.drag = false
}