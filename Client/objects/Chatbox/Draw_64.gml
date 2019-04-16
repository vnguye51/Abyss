draw_self()
draw_set_font(font0)

for(var i=0;i<ds_list_size(messages);i++){
	draw_text(x+2,y+2+10*i,messages[| i])
}