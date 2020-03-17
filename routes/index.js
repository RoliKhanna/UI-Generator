var express = require('express');
var router = express.Router();
var fs = require('fs');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

// render route for getting data from converter/json files, and render
router.get('/render', function(req, res){

  // Reading from JSON file
  // Maybe there should be a different route for this
  var content = fs.readFileSync("./converter/template_1.json");
  console.log("Here's the content from the JSON file: ", JSON.parse(content));
  // Render the newly retrieved html
  // let html = json2html.transform([{'s':'json2html'},{'s':'is'},{'s':'awesome'}],{'<>':'li','html':'${s}'});
  let html = json2html.transform([{'s':'json2html'},{'s':'is'},{'s':'awesome'}], content);
  res.render(html); // I think?

});

// send some data to generate json files for rendering
router.post('/generate', function(req, res, next){

  var params = {id = req.id, type = req.type} ;
  // call python function to generate UI
  // async call
  res.send("Success!");

});

module.exports = router;
