import fs from "fs";
const readStream = fs.createReadStream("data.txt");
const writeStream = fs.createWriteStream("result.txt");
readStream.pipe(writeStream);
/*
fs.readFile("data.txt",(err,data)=>{
    if(!err){
        fs.writeFile("result.txt",data,(err)=>{
            err ? console.log(err) : console.log("Operation success");
        });
    }
    else
        console.log(err); 
});
*/