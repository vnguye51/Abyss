/// Client Script: HandlePacketClient


var buffer,raw_data,decoded_data
buffer = argument[0];
raw_data = buffer_read( buffer, buffer_string );
decoded_data = json_decode(raw_data)
decoded_data = decoded_data[? "default"]


for(var i=0; i<ds_list_size(decoded_data); i++){
	var data = decoded_data[| i]
	switch (data[? "id"]) {
		case 0:
		//First connect
			show_debug_message("First connection")
			var message = data[? "message"]

			//Assign Client ID
			client_id = string(message[? "client_id"])
		
			//Instantiate all players
			//players = message[? "players"]
			//var key = ds_map_find_first(players)
			//for (var i=0; i<ds_map_size(players); i++) {
			//	var player_info = players[? key]
			//	//If Other Player
			//	if (key != string(client_id)) {
			//		var other_player = instance_create_depth(player_info[? "x"],player_info[? "y"],0,OtherPlayerObj)
			//		other_player.player_id = key
			//		//Store the reference of the newly created player on the map
			//		PlayerObjMap[? key] = other_player
			//		show_debug_message(json_encode(PlayerObjMap))
			//	}
			//	//If player
			//	else{
			//		show_debug_message("CREATING PLAYER CHARACTER")
			//		var player_char = instance_create_depth(player_info[? "x"],player_info[? "y"],0,PlayerObj)
			//	}
			//	key = ds_map_find_next(players,key)
			//}
			
			//Instantiate all enemies
			//enemies = message[? "enemies"]
			//key = ds_map_find_first(enemies)
			//for (var i=0; i<ds_map_size(enemies); i++) {
			//	var enemy_info = enemies[? key]
			//	var enemy = instance_create_depth(enemy_info[? "x"],enemy_info[? "y"],0,asset_get_index(enemy_info[? "name"]))
			//	enemy.enemy_id = key
			//	EnemyObjMap[? key] = enemy
			//	key = ds_map_find_next(enemies,key)
			//}

			
			
			//Instantiate all items
			items = message[? "items"]
			key = ds_map_find_first(items)
			for (var i=0; i<ds_map_size(items); i++) {
				var item_info = items[? key]
				var item = instance_create_depth(item_info[? "x"],item_info[? "y"],0,asset_get_index(item_info[? "name"]))
				item.item_id = key
				ItemObjMap[? key] = item
				key = ds_map_find_next(items,key)
			}
			
			break
			
			
		//case 1:	
		////A new player connected
		//	show_debug_message("A new player connected")
		//	var message = data[? "message"]
		//	var new_player = instance_create_depth(message[? "x"],message[? "y"],0,OtherPlayerObj)
		//	new_player.player_id = string(message[? "new_player_id"])
		//	PlayerObjMap[? new_player.player_id] = new_player
		//	break 
		
		//case 2:
		////A player disconnected
		//	show_debug_message("A player disconnected")
		//	var message = data[? "message"]
		//	var disc_player_id = string(message[? "player_id"])
		//	var disc_player = players[? disc_player_id] 
		//	show_debug_message(disc_player_id)
		//	show_debug_message(json_encode(PlayerObjMap))
		//	instance_destroy(PlayerObjMap[? disc_player_id])
		//	ds_map_delete(PlayerObjMap,disc_player_id)
		//	break
			
		case 3:
		//Update player positions 
		//Each PlayerObj updates its own positions in its step function
			//show_debug_message("updating player positions")
			var message = data[? "message"]
			players = message[? "player_data"]
			key = ds_map_find_first(players)
			for (var i=0; i<ds_map_size(players); i++) {
				var player_info = players[? key]
				if(is_undefined(PlayerObjMap[? key])){
					if (key != string(client_id)) {
						var other_player = instance_create_depth(player_info[? "x"],player_info[? "y"],0,OtherPlayerObj)
						PlayerObjMap[? key] = other_player
						other_player.player_id = key
					}
					else{
						var player = instance_create_depth(player_info[? "x"],player_info[? "y"],0,PlayerObj)
						PlayerObjMap[? key] = player
						player.player_id = key
					}
				}
				key = ds_map_find_next(players,key)
			}
			
			
			enemies = message[? "enemy_data"]
			key = ds_map_find_first(enemies)
			for (var i=0; i<ds_map_size(enemies); i++) {
				var enemy_info = enemies[? key]
				if(is_undefined(EnemyObjMap[? key])){
					var enemy = instance_create_depth(enemy_info[? "x"],enemy_info[? "y"],0,asset_get_index(enemy_info[? "name"]))
					EnemyObjMap[? key] = enemy
					enemy.enemy_id = key
				}
				key = ds_map_find_next(enemies,key)
			}
			
			items = message[? "item_data"]
			key = ds_map_find_first(items)
			for (var i=0; i<ds_map_size(items); i++) {
				var item_info = items[? key]
				if(is_undefined(ItemObjMap[? key])){
					var item = instance_create_depth(item_info[? "x"],item_info[? "y"],0,asset_get_index(item_info[? "name"]))
					ItemObjMap[? key] = item
					item.item_id = key
				}
				key = ds_map_find_next(items,key)
			}
			
			
			attacks = message[? "attack_data"]
			break
			
		case 4:
			var message = data[? "message"]
			ds_list_add(ChatObj.messages,message)
			if(ds_list_size(ChatObj.messages) > 7 ){
				ds_list_delete(ChatObj.messages,0)
			}
			break
	}	
}
