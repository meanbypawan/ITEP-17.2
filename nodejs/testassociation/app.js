import express from "express";
import bodyParser from "body-parser";
import UserRouter from "./routes/user.route.js";
import ProfileRouter from "./routes/profile.route.js";
const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

app.use("/user",UserRouter);
app.use("/profile",ProfileRouter);


app.listen(3000,()=>{
    console.log("Server Started...");
});

