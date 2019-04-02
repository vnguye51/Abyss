globalvar players;
globalvar client_id;
socket = network_create_socket(network_socket_tcp);
show_debug_message("creating socket")
client_id = -1
var server = network_connect_raw(socket , "127.0.0.1", 8080);
if server < 0
    {
	show_debug_message("fail to connect")
    //No connection! Failsafe codes here...
    }
else
    {
    show_debug_message("CONNECTED")
    }
	
ping = -1
result = -1

	
buffer = buffer_create(1024, buffer_fixed, 1);
alarm[0] = room_speed
key_inputs = ds_map_create()
ds_map_add(key_inputs,"left",0)
ds_map_add(key_inputs,"right",0)
ds_map_add(key_inputs,"up",0)
ds_map_add(key_inputs,"down",0)
ds_map_add(key_inputs,"space",0)


//player_pos = ds_map_create()
//ds_map_add(player_pos,"x",0)
//ds_map_add(player_pos,"y",0)
