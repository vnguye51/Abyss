
//Draw players
if (players){
	var key = ds_map_find_first(players)
	for(var i = 0; i<ds_map_size(players);i++){
		var player_info = players[? key]
		if (key == client_id){
			draw_sprite(PlayerSprite,player_info[? "frame"],player_info[? "x"],player_info[? "y"],)
			var items = player_info[? "items"]
			draw_text(200,200,"Gold: " + string(items[? "Gold"]))
		}
		else{
			draw_sprite(OtherPlayerSprite,player_info[? "frame"],player_info[? "x"],player_info[? "y"],)
		}
		key = ds_map_find_next(players,key)
	}
	
}
//Draw attacks and projectiles
if (attacks){
	var key = ds_map_find_first(attacks)
	for(var i=0;i<ds_map_size(attacks);i++){
		var attack_info = attacks[? key]
		if (attack_info[? "frame"]) >= 0 {
			draw_sprite(asset_get_index(attack_info[? "name"] + "Sprite"),attack_info[? "frame"],attack_info[? "x"],attack_info[? "y"])
			key = ds_map_find_next(attacks,key)
		}
	}
}

