import mongoose from "mongoose"
const commentSchema = new mongoose.Schema({
    text:String,
    post:{
        type: mongoose.Schema.Types.ObjectId,
        ref: "posts"
    },
    user:{
        type: mongoose.Schema.Types.ObjectId,
        ref: "users"
    },
    createAt:{
        type: Date,
        default: Date.now
    }
});

export const Comment = mongoose.model("comments",commentSchema)