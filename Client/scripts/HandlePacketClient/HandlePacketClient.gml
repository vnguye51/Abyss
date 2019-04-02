/// Client Script: HandlePacketClient


var buffer,raw_data,data
buffer = argument[0];
raw_data = buffer_read( buffer, buffer_string );
data = json_decode(raw_data)
show_debug_message("Received packet: " + raw_data);

switch (data[? "id"]) {
	case 0:
	//First connect
		show_debug_message("First connection")
		var message = data[? "message"]

		//Assign Client ID
		client_id = message[? "client_id"]
		
		//Instantiate all players
		players = message[? "players"]

		for (var i=0; i<ds_list_size(players); i += 1) {
			var player = players[|i]
			//If Other Player
			if (player[? "id"] != client_id) {
				var other_player = instance_create_depth(player[? "x"],player[? "y"],0,OtherPlayerObj)
				other_player.player_id = player[? "id"]
			}
			//If player
			else{
				show_debug_message("CREATING PLAYER CHARACTER")
				var player_char = instance_create_depth(player[? "x"],player[? "y"],0,PlayerObj)
			}
		}
		break
		
	case 1:
	//Update player positions 
	//Each PlayerObj updates its own positions in its step function
		show_debug_message("updating player positions")
		players = data[? "message"]
		break
}	

//show_debug_message(ClientObj.player_pos[? "x"] + "|" + ClientObj.player_pos[? "y"])
