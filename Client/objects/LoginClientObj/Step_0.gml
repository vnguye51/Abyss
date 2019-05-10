login_message[? "username"] = UsernameInputObj.text
login_message[? "password"] = PasswordInputObj.text
create_message[? "username"] = UsernameInputObj.text
create_message[? "password"] = PasswordInputObj.text


if keyboard_check_pressed(vk_enter){
	LoginScript()
}

