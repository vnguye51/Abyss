if(inventory){
	instance_destroy(InventoryObj)
	inventory = false
}
else{
	instance_create_depth(0,0,-1,InventoryObj)
	inventory = true
}