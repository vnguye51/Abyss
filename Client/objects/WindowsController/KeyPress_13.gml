if(chatting == false){
	chatting = true
	keyboard_string = ""
}
else{
	chatting = false
	if (keyboard_string != ""){
		ClientObj.chat_message_packet[? "message"] = keyboard_string
		ds_list_add(ClientObj.messages,ClientObj.chat_message_packet)
		ds_list_mark_as_map(ClientObj.messages,ds_list_size(ClientObj.messages)-1)
		keyboard_string = ""
	}
}

