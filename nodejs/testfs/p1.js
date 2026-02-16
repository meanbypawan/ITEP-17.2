import fs from "fs";
import PromptSync from "prompt-sync";
const prompt = PromptSync();

console.log("At the start...");
let text = prompt("Enter some data");

fs.writeFile("./data.txt",text,(err)=>{
    err ? console.log(err) : console.log("Operation success..");
});
console.log("At the end...");