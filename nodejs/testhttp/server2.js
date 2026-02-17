import http from "http";
http.createServer((request,response)=>{
    response.write("Hi Client...");
    response.end();
}).listen(3001,()=>{
    console.log("Server Started...");
})