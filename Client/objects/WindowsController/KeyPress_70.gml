if not chatting{
	if(friends){
		friends = false
		var i = 0
		while(i<ds_list_size(windows_stack)){
			if(windows_stack[| i] == friends_inst){
				ds_list_delete(windows_stack,i)
				break
			}
			else{
				i += 1
			}
		}
		while(i<ds_list_size(windows_stack)){
			var inst = windows_stack[| i]
			inst.depth = inst.depth + 2
			i += 1
		}
		instance_destroy(friends_inst)
	}
	else{
		friends_inst = instance_create_depth(0,0,-(ds_list_size(windows_stack)*2),FriendListObj)
		ds_list_add(windows_stack,friends_inst)
		friends = true
	}
}