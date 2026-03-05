import express from "express";
import CategoryRouter from "./routes/category.route.js";
import bodyParser from "body-parser";
import ProductRouter from "./routes/product.route.js";
import UserRouter from "./routes/user.route.js";
import "./model/association.js";
const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

app.use("/category",CategoryRouter);
app.use("/product",ProductRouter);
app.use("/user",UserRouter);
app.listen(3000,()=>{
    console.log("server started...");
});