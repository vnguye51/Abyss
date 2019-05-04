/// @description send request to drop item from inventory
/// @param item_string
ds_map_clear(ClientObj.item_drop_packet)
ClientObj.item_drop_packet[? "message_id"] = 3
ClientObj.item_drop_packet[? "item"] = argument[0]
ds_list_add(ClientObj.messages,ClientObj.item_drop_packet)
ds_list_mark_as_map(ClientObj.messages,ds_list_size(ClientObj.messages)-1)
