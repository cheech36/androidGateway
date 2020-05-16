// https://www.freecodecamp.org/news/here-is-the-most-popular-ways-to-make-an-http-request-in-javascript-954ce8c95aaa/

// 19:49
function steer(direction)
{
var xhr = new XMLHttpRequest();
var url = 'http://192.168.1.70:9090/drive'
xhr.open("POST", url, true)
xhr.setRequestHeader("Content-Type", "application/json");
var data = JSON.stringify({"Operation":direction})
xhr.send(data)
}