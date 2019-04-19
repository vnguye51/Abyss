if not WindowsController.chatting{
	key_inputs[? "right"] = keyboard_check(vk_right);
	key_inputs[? "left"] = keyboard_check(vk_left);
	key_inputs[? "down"] = keyboard_check(vk_down);
	key_inputs[? "up"] = keyboard_check(vk_up)
	key_inputs[? "space_pressed"] = keyboard_check_pressed(vk_space);
	key_inputs[? "space"] = keyboard_check(vk_space)
	key_inputs[? "Z"] = keyboard_check(ord("Z"))
}
else{
	key_inputs[? "right"] = 0;
	key_inputs[? "left"] = 0;
	key_inputs[? "down"] = 0;
	key_inputs[? "up"] = 0
	key_inputs[? "space_pressed"] = 0
	key_inputs[? "space"] = 0
	key_inputs[? "Z"] = 0
}


ds_list_add(messages,key_inputs)
ds_list_mark_as_map(messages,ds_list_size(messages)-1)
var output_data = json_encode(packet_wrapper)
buffer_write( buffer, buffer_string, output_data);
result = network_send_raw( socket, buffer, buffer_tell(buffer) );
buffer_seek( buffer, buffer_seek_start, 0 );
ds_list_clear(messages)


//Set up empty inputs to put into buffer
key_inputs = ds_map_create()
key_inputs[? "message_id"] = 1

chat_message_packet = ds_map_create()
chat_message_packet[? "message_id"] = 2

alarm[0] = room_speed/30