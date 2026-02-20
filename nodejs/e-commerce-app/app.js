import express from "express";
import IndexRouter from "./routes/index.route.js";
import UserRouter from "./routes/user.route.js";
import bodyParser from "body-parser";
const app = express();
app.set("view engine","ejs");

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

app.use("/user",UserRouter);
app.use("/",IndexRouter);

app.listen(3000,()=>{
    console.log("Server Running...");
});




