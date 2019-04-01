/// Client Script: HandlePacketClient

var buffer = argument[0];

var raw_data = buffer_read( buffer, buffer_string );
var data = json_decode(raw_data)
show_debug_message("Received packet: " + raw_data);


PlayerObj.player_pos[? "x"] = data[? "x"]
PlayerObj.player_pos[? "y"] = data[? "y"]
ds_map_destroy(data)
