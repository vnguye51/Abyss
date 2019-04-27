drag = false
x_offset = 0
y_offset = 0
x_pos = 25
y_pos = 25
bar_width = 220
bar_height = 8

inventory_items = ds_list_create()
for(var i=0;i<5;i++){
	var item = instance_create_depth(0,0,depth-1,InventoryItemObj)
	item.x_offset = 2+20*i
	item.y_offset = 182
	item.sprite = InventoryItemSprite
	ds_list_add(inventory_items,item)
}
