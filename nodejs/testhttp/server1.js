import http from "http";
// request :-- IncomingMessage
// response :-  ServerResponse

const server = http.createServer((request,response)=>{
    response.write("Hello Client....");
    response.end();
});
server.listen(3000,()=>{
    console.log("Server Started...");
});