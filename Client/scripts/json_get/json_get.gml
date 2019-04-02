///json_get(jsondata, ...)
///Obtained from FrostyCat @ https://forum.yoyogames.com/index.php?threads/nested-json.43165/
{
var gotten = argument[0];
if (argument_count >= 2 && is_real(argument[1])) {
  gotten = gotten[? "default"];
}
for (var i = 1; i < argument_count; i++) {
  var k = argument[i];
  if (is_real(k)) {
    gotten = gotten[| k];
  } else if (is_string(k)) {
    gotten = gotten[? k];
  } else {
    show_error("Invalid argument " + string(i+1) + " to json_get().", true);
  }
}
return gotten;
}