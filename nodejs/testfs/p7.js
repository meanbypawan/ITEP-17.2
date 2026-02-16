import fs from "fs";
import PromptSync from "prompt-sync";
const writeStream = fs.createWriteStream("abc.txt");
const prompt = PromptSync();

let text = prompt("Enter some text");
writeStream.write(text);
writeStream.end();

writeStream.on("finish",()=>{
    console.log("Write operation success");
});

writeStream.on("error",(err)=>{
    console.log(err);
});
