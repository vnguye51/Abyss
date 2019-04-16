/// @description Insert description here
// You can write your code in this editor
if(chatting == false){
	chatting = true
	keyboard_string = ""
}
else{
	chatting = false
	chat_message_packet[? "message"] = keyboard_string
	ds_list_add(messages,chat_message_packet)
	ds_list_mark_as_map(messages,ds_list_size(messages)-1)
	keyboard_string = ""
}