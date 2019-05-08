/// Client Script: HandlePacketClient


var buffer,raw_data,decoded_data
buffer = argument[0];
raw_data = buffer_read( buffer, buffer_string );
decoded_data = json_decode(raw_data)
decoded_data = decoded_data[? "default"]


for(var i=0; i<ds_list_size(decoded_data); i++){
	var data = decoded_data[| i]
	switch (data[? "id"]) {
		case 0:
		//Login
			room_goto(ChooseCharacterRoom)
			break
		case 1:
			LoginClientObj.response = "Login Failed."
			break
	}	
}
