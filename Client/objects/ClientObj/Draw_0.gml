if (attacks){
	var key = ds_map_find_first(attacks)
	for(var i=0;i<ds_map_size(attacks);i++){
		var attack_info = attacks[? key]
		draw_sprite(AttackSprite,-1,attack_info[? "x"],attack_info[? "y"])
		key = ds_map_find_next(attacks,key)
	}
}