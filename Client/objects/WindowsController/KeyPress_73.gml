if (not chatting){
	if(inventory){
		inventory = false
		var i = 0
		while(i<ds_list_size(windows_stack)){
			if(windows_stack[| i] == inventory_inst){
				ds_list_delete(windows_stack,i)
				break
			}
			else{
				i += 1
			}
		}
		inventory_pos = [inventory_inst.x_pos,inventory_inst.y_pos]
		instance_destroy(inventory_inst)
	}
	else{
		inventory_inst = instance_create_depth(0,0,-(ds_list_size(windows_stack)*2),InventoryObj)
		ds_list_add(windows_stack,inventory_inst)
		inventory = true
	}
}
for(var i = 0; i<ds_list_size(windows_stack);i++){
	var inst = windows_stack[| i]
	inst.depth = -10 + (ds_list_size(windows_stack)-i)*2
}