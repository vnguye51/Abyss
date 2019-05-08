if keyboard_check(vk_anykey){
	if(target == 0){
		username = keyboard_string
	}
	else{
		password = keyboard_string
	}
}


if keyboard_check_pressed(vk_tab){
	if(target == 1){
		target = 0
		keyboard_string = username
	}
	else{
		target = 1
		keyboard_string = password
	}
}

login_message[? "username"] = username
login_message[? "password"] = password
create_message[? "username"] = username
create_message[? "password"] = password


if keyboard_check_pressed(vk_enter){
	LoginScript()
}

