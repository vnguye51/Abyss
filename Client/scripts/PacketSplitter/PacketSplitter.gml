var json_string = argument[0]
var res = ds_list_create()
var i = string_pos("}{",json_string)
while (i != 0){
	ds_list_add(res, string_copy(json_string,0,i))
	json_string = string_copy(json_string,i+1,9000)
	i = string_pos("}{",json_string)
	show_debug_message(json_string)
	show_debug_message(res[| ds_list_size(res)-1])
}
ds_list_add(res,json_string)
return res