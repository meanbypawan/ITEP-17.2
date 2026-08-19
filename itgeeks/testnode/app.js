import express from "express"
import mongoose from "mongoose"
import { ToDo } from "./model/todo.model.js"
import ToDoRouter from "./router/todo.router.js"
const app = express()


mongoose.connect("mongodb://localhost:27017/todoapp")
.then(()=>{
    app.use(express.json())
    app.use(express.urlencoded({extended: true}))

    app.use("/todo",ToDoRouter)
    
    app.listen(3000,()=>{
        console.log("Server Started...")
    })
    console.log("Database connected....")

}).catch(err=>{
    console.log(err)
})
