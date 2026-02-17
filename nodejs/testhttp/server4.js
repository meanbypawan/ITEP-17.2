import http from "http";
import fs from "fs";
http.createServer((request,response)=>{
    console.log(request.url);
    if(request.url == "/home" || request.url == "/"){
      let homePage =  fs.readFileSync("./public/home.html");
      response.write(homePage);
      response.end();
    }
    else if(request.url == "/about"){
      let aboutPage = fs.readFileSync("./public/about.html");
      response.write(aboutPage);
      response.end();
    }
    else if(request.url == "/contact"){
      let contactPage = fs.readFileSync("./public/contact.html");
      response.write(contactPage);
      response.end();
    }
    else if(request.url.match("\.css$")){
        let filePath = "./public/"+request.url;
        let cssResponse = fs.createReadStream(filePath);
        cssResponse.pipe(response);
    }
    else if(request.url.match("\.jpeg")){
        let filePath = "./public/"+request.url;
        let imageResponse = fs.createReadStream(filePath);
        imageResponse.pipe(response);
    }
})
.listen(3000,()=>{
    console.log("Server Runnit At http://localhost:3000");
})