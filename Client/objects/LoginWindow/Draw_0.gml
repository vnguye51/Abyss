draw_set_valign(fa_top)
draw_set_halign(fa_left)
draw_set_font(font0)
draw_self()

draw_text_color(x+4,y+22,"Username:",c_white,c_white,c_white,c_white,1)
draw_text_color(x+4,y+52,"Password:",c_white,c_white,c_white,c_white,1)

draw_set_halign(fa_middle)
draw_text(100,8+window_get_height()/2-40,LoginClientObj.response)