//Bibliothèques
var fs = require('fs');

var filePath = '../../simulation_reseau';

console.log("Watching file")

fs.watch(filePath, (eventType, fileName) => {
    console.log(eventType);
    console.log(fileName);
})