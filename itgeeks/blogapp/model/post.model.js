import mongoose from "mongoose"
const postSchema = new mongoose.Schema({
    title: String,
    image: String,
    content:String,
    user:{
      type: mongoose.Schema.Types.ObjectId,
      ref: "users"
    },
    createdAt:{
        type:Date,
        default: Date.now
    }
})

export const Post = mongoose.model("posts",postSchema)