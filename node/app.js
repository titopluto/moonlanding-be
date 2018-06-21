var express = require('express');
var app = express();
var cors = require("cors");
var PORT = 8001;
var path = require('path');

var startServer = function (app) {
	var server = app.listen(PORT || 8002);
	console.log("server started" + PORT);
};

app.use(cors());
app.use("/", express.static('./content'));



startServer(app);