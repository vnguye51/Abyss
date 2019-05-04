drag = false
x_offset = 0
y_offset = 0
x_pos = WindowsController.inventory_pos[0]
y_pos = WindowsController.inventory_pos[1]
width = 220
height = 300
bar_width = 220
bar_height = 8
curr_item_index = -1
inventory_items = ds_list_create()
for(var i=0;i<5;i++){
	var item = instance_create_depth(0,0,depth-1,InventoryItemObj)
	item.x = x_pos + 2+20*i
	item.y = y_pos + 182
	item.origin = [2+20*i,182]
	item.sprite = InventoryItemSprite
	ds_list_add(inventory_items,item)
}
