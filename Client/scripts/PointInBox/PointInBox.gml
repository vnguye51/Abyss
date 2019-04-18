/// @description check if point in box
/// @param x1
/// @param y1
/// @param rect_x
/// @param rect_y
/// @param width
/// @param height

var x1 = argument[0]
var y1 = argument[1]
var rect_x = argument[2]
var rect_y = argument[3]
var width = argument[4]
var height = argument[5]
if (x1 < rect_x + width &&
   x1 > rect_x &&
   y1 < rect_y + height &&
   y1 > rect_y) {
   return true
}