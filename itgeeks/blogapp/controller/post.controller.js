import { Post } from "../model/post.model.js"

export const fetchPost = async(request,response,next)=>{
    console.log("Handler process : "+process.pid)
    try{
       let posts = await Post.find().populate("user")
       return response.status(200).json({"posts": posts})
    }
    catch(err){
        console.log(err)
        return response.status(500).json({"error":"Internal Server Error"})
    }
}
export const createPost = async (request,response,next)=>{
  try{
    let filepath = ""
    if(request.file)
     filepath = request.file.filename
    request.body.image = "images/"+filepath
    let post = await Post.create(request.body)
    return response.status(201).json({"message":"post created",post}) 
  }
  catch(err){
    return response.status(500).json({"error": "Internal server error"})
  }
}