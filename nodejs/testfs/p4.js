import fs from "fs";
/*
  Asychronoue :-
    readFile()
    writeFile()
    appendFile()
  Synchronous :-
    readFileSync()
    writeFileSync()
    appendFileSync()  
*/
console.log("At the start...");
try{
 let data = fs.readFileSync("./dat.txt",'utf8');// wait
 console.log(data);
}
catch(err){
    console.log(err.name);
    console.log(err.message);
}
 console.log("At the end...");