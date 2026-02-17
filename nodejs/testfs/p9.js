/*
  f1.txt :-- It is f1 file data
  f2.txt :-- It is f2 file data
  -----------------------------
  result.txt
*/
import fs from "fs";
const readFileF1 = ()=>{
    return new Promise((resolve,reject)=>{
       fs.readFile("f1.txt","utf8",(err,data)=>{
        err ? reject(err) : resolve(data);
       });
    });
}
const readFileF2 = ()=>{
    return new Promise((resolve,reject)=>{
        fs.readFile("f2.txt","utf8",(err,data)=>{
            err ? reject(err): resolve(data);
        });
    });
}

Promise.all([readFileF1(),readFileF2()])
.then(results=>{
   fs.writeFile("result.txt",results[0]+"\n"+results[1],(err)=>{
    err ? console.log(err) : console.log("Operation success");
   });
}).catch(err=>{
    console.log(err);
});



