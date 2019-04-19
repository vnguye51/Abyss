display_set_gui_maximize(1,1,0,window_get_height()-98)

draw_sprite(ChatboxSprite,0,4,0)
draw_set_font(font0)

for(var i=0;i<ds_list_size(messages);i++){
	draw_text(6,2+10*i,messages[| i])
}

if(WindowsController.chatting){
	draw_sprite(ChatInputSprite,0,5,80)
	if(blinker){
		draw_text(6,82,keyboard_string + "|")
	}
	else{
		draw_text(6,82,keyboard_string)
	}
}
