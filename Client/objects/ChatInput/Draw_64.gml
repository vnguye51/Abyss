if(ClientObj.chatting){
	draw_self()
	draw_set_font(font0)
	if(blinker){
		draw_text(x+2,y+2,keyboard_string + "|")
	}
	else{
		draw_text(x+2,y+2,keyboard_string)
	}
}