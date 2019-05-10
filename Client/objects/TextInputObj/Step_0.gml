if(selected){
	text = keyboard_string
}
if(keyboard_check_pressed(vk_tab) and selected and next != noone){
	next.passed = true
	selected = false
}

if(passed){
	passed = false
	selected = true
	keyboard_string = text
}