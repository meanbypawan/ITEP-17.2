import fs from "fs";

let readStream = fs.createReadStream("data.txt");
console.log("At the start....");
let data = "";
readStream.on("data",(chunk)=>{
    data = data + chunk;
});

readStream.on("end",()=>{
    console.log(data);
});

readStream.on("error",(err)=>{
    console.log(err);
});
console.log("At the end....");