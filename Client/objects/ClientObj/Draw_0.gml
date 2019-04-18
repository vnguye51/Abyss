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

