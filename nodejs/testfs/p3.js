import fs from "fs";

console.log("At the start...");
fs.readFile("./data.txt",(err,result)=>{
    err ? console.log(err) : console.log(result.toString());
});
console.log("At the end...");