import express from "express";
import CategoryRouter from "./routes/category.route.js";
import bodyParser from "body-parser";
const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

app.use("/category",CategoryRouter);

app.listen(3000,()=>{
    console.log("server started...");
});