import http from "http";

http.createServer((request,response)=>{
   // http://localhost:3000
   console.log(request); 
   if(request.url == "/home" && request.method == "GET")
     response.write("Home Page");

   else if(request.url == "/about" && request.method == "GET")
     response.write("About Page");
   
   else if(request.url == "/contact" && request.method == "GET")
     response.write("Contact Page");
   
   response.end();   
}).listen(3000,()=>{
    console.log("Server Started....");
});