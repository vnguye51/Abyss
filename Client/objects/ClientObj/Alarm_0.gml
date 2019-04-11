key_inputs[? "right"] = keyboard_check(vk_right);
key_inputs[? "left"] = keyboard_check(vk_left);
key_inputs[? "down"] = keyboard_check(vk_down);
key_inputs[? "up"] = keyboard_check(vk_up)
key_inputs[? "space_pressed"] = keyboard_check_pressed(vk_space);
key_inputs[? "space"] = keyboard_check(vk_space)

message_id = 1
var output_data = json_encode(key_inputs)

buffer_seek( buffer, buffer_seek_start, 0 );
buffer_write( buffer, buffer_string, output_data);

result = network_send_raw( socket, buffer, buffer_tell(buffer) );
alarm[0] = room_speed/30