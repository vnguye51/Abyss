if not is_undefined(ds_map_find_value(enemies,enemy_id)){
	var char_info = enemies[? enemy_id]
	if (char_info[? "vfx"] == 0) {
	}
	else{
		shader_set(flash_shader)
	}
}


draw_self();
shader_reset()