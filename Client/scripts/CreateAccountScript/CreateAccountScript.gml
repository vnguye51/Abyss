
ds_list_add(LoginClientObj.messages,LoginClientObj.create_message)
ds_list_mark_as_map(LoginClientObj.messages,ds_list_size(LoginClientObj.messages)-1)
var output_data = json_encode(LoginClientObj.packet_wrapper)
buffer_write( LoginSocketObj.buffer, buffer_string, output_data);
network_send_raw( LoginSocketObj.socket, LoginSocketObj.buffer, buffer_tell(LoginSocketObj.buffer) );
buffer_seek( LoginSocketObj.buffer, buffer_seek_start, 0 );
ds_list_clear(LoginClientObj.messages)
create_message = ds_map_create()
create_message[? "id"] = 1
create_message[? "username"] = LoginClientObj.username
create_message[? "password"] = LoginClientObj.password