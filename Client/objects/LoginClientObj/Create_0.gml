/// @description Insert description here
// You can write your code in this editor
alarm[0] = 15

response = ""

packet_wrapper = ds_map_create()
messages = ds_list_create()


create_message = ds_map_create()
create_message[? "id"] = 1
create_message[? "username"] = ""
create_message[? "password"] = ""

login_message = ds_map_create()
login_message[? "id"] = 2
login_message[? "username"] = ""
login_message[? "password"] = ""



ds_map_add_list(packet_wrapper,"messages",messages)