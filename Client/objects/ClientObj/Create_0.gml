globalvar client_id;
globalvar PlayerObjMap;
globalvar EnemyObjMap;
globalvar ItemObjMap;
globalvar players;
globalvar enemies;
globalvar attacks;
globalvar items;

players = 0
enemies = 0
attacks = 0
items = 0

EnemyObjMap = ds_map_create()
PlayerObjMap = ds_map_create();
ItemObjMap = ds_map_create();

socket = network_create_socket(network_socket_tcp);
window_set_size(800,480)
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

chatting = false
inventory = false

buffer = buffer_create(2048, buffer_fixed, 1);
alarm[0] = room_speed

packet_wrapper = ds_map_create()
messages = ds_list_create()
ds_map_add_list(packet_wrapper,"messages",messages)

key_inputs = ds_map_create()
key_inputs[? "message_id"] = 1

ds_map_add(key_inputs,"left",0)
ds_map_add(key_inputs,"right",0)
ds_map_add(key_inputs,"up",0)
ds_map_add(key_inputs,"down",0)
ds_map_add(key_inputs,"space",0)
