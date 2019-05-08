persistent = true
socket = network_create_socket(network_socket_tcp);
buffer = buffer_create(2048, buffer_fixed, 1);
var server = network_connect_raw(socket , "127.0.0.1", 8081);
if server < 0{
	show_debug_message("fail to connect")
    //No connection! Failsafe codes here...
}
else{
    show_debug_message("CONNECTED")
}