import mongoose from "mongoose"
import express from "express"
import UserRouter from "./router/user.router.js"
import PostRouter from "./router/post.router.js"
import CommentRouter from "./router/comment.router.js"
import dotenv from "dotenv"
import cluster from "cluster"
import os from "os"
if (cluster.isPrimary) {
    console.log("Main process : "+process.pid)
    console.log("Memory usage : "+process.memoryUsage())
    for (let i = 0; i < os.cpus().length; i++)
        cluster.fork()
    cluster.on("exit", (worker) => {
        cluster.fork()
    })
}
else {
    console.log("Worker Thread : "+process.pid)
    dotenv.config()
    const app = express()

    app.use(express.json())
    app.use(express.urlencoded({ extended: true }))
    app.use(express.static("public"))
    app.use("/user", UserRouter)
    app.use("/post", PostRouter)
    app.use("/comment", CommentRouter)

    mongoose.connect("mongodb://localhost:27017/blogapp")
        .then(con => {
            console.log("Database connected....")
            const PORT = process.env.PORT || 3001
            app.listen(PORT, () => {
                console.log(`Server started at ${PORT}`)
            });
        }).catch(err => {
            console.log(err)
            console.log("Something wrong...")
        });
}