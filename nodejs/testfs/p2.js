import fs from "fs";
import PromptSync from "prompt-sync";
const prompt = PromptSync();

let text = prompt("Enter some text");
fs.appendFile("./data.txt","\n"+text,err=>{
    err ? console.log(err) : console.log("operation success");
});