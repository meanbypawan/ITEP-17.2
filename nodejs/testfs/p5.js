/*
  syntax :-
    if(condition)
     statem--1;
    else
     statement--2;    
*/
import fs from "fs";
import PromptSync from "prompt-sync";
console.log("At the start....");
const prompt = PromptSync();

let data = prompt("Enter some text");
try{
 fs.writeFileSync("xyz.txt",data);
}
catch(err){
    console.log(err.name);
    console.log(err.message);
}
console.log("At the end...");

