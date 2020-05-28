var express = require('express');
var router = express.Router();
var fs = require('fs');
var Promise = require('promise');
var jsdom = require("jsdom");
var JSDOM = jsdom.JSDOM;

global.document = new JSDOM("./public/index.html").window.document;

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

// render route for getting data from converter/json files, and render
function render(){

  // Reading from JSON file
  // Maybe there should be a different route for this
  var template = fs.readFileSync("./converter/template.json");
  var data = fs.readFileSync("./converter/dummy_data.json");
  console.log("Here's the content from the JSON file: ", JSON.parse(content));
  // Render the newly retrieved html
  // let html = json2html.transform([{'s':'json2html'},{'s':'is'},{'s':'awesome'}],{'<>':'li','html':'${s}'});
  let html = json2html.transform(data, content);

  return html;
}

// send some data to generate json files for rendering
function generate(){

  console.log("We're now dealing with generating a new UI.");
  // call python function to generate UI
  // async call to generate UI

  return 0;

}

// const button = global.document.getElementById("MyButton");
// const iframe = global.document.getElementById("MyIframe");
//
// console.log("button: ", button)
//
// button.onclick = async function(e) {
//   console.log('button was clicked');
//
//   const valueA = await generate();
//   const newHTML = await render();
//
//   iframe.src = newHTML;
//
// }

module.exports = router;
