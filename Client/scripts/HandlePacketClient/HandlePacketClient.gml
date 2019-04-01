/// Client Script: HandlePacketClient



var buffer = argument[0];
var raw_data = buffer_read( buffer, buffer_string );
var data = json_decode(raw_data)
show_debug_message("Received packet: " + raw_data);

switch (data[? "id"]) {
	case 0:
		//First connect
		show_debug_message("First connection")
		var message 
		message = data[? "message"]
		ClientObj.client_id = message[? "client_id"]
		break
	case 1:
		show_debug_message("updating player positions")
		var message, all_player_data, player_data
		message = data[? "message"]
		{
			var i
			for (i = 0; i<ds_list_size(message); i+= 1) {
				if (i == ClientObj.client_id) {
					player_data = message[| i]
					break
				}
			}
			show_debug_message(json_encode(player_data))
			ClientObj.player_pos[? "x"] = player_data[? "x"]
			ClientObj.player_pos[? "y"] = player_data[? "y"]
		}	
		break
}	

//show_debug_message(ClientObj.player_pos[? "x"] + "|" + ClientObj.player_pos[? "y"])
ds_map_destroy(data)
