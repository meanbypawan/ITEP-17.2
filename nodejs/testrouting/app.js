import express from "express";
import bodyParser from "body-parser";
const app = express();

app.set("view engie","ejs");

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

// Get :- http://localhost:3000/home
app.get("/home",(request,response)=>{
   return response.render("home.ejs");
});
app.get("/about",(request,response,next)=>{
   return response.render("about.ejs");
});
app.get("/contact",(request,response,next)=>{
    return response.render("contact.ejs");
});
app.get("/add",(request,response,next)=>{
    return response.render("add.ejs");
});
app.post("/add",(request,response,next)=>{
    let a = request.body.first_number * 1;
    let b = request.body.second_number * 1;
    let result = a + b;
    //console.log("/add executed....");
    response.write("Addition : "+result);
    response.end();
});
app.listen(3000,()=>{
    console.log("Server Started....");
});