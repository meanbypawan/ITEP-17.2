import express from "express";

// app is express applicationn instance.
const app = express();

app.use((request,response,next)=>{
    console.log("Hello...| app.use() executed.....");
    next();
});

app.get("/home",(request,response,next)=>{
    response.write("Home Page");
    response.end();
});

app.get("/about",(request,response,next)=>{
    response.write("About Page");
    response.end();
});

app.post("/register",(request,response,next)=>{
    response.write("Registration Success....");
    response.end();
});

app.listen(3000,()=>{console.log("Server Started....")});