display_set_gui_maximize(1,1,0,0)

draw_set_valign(fa_middle)

draw_text(window_get_width()/2-80,window_get_height()/2-40,response)
if(target == 0){
	draw_text(window_get_width()/2-80,window_get_height()/2-10,"Username:" + username + blinker)
	draw_text(window_get_width()/2-80,window_get_height()/2+10,"Password:" + password)
}
else{
	draw_text(window_get_width()/2-80,window_get_height()/2-10,"Username:" + username)
	draw_text(window_get_width()/2-80,window_get_height()/2+10,"Password:" + password + blinker)
}
