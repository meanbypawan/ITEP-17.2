import { Comment } from "../model/comment.model.js"
import { Post } from "../model/post.model.js"
import { User } from "../model/user.model.js"

export const createComment = async(request,response,next)=>{
    try{
      console.log(request.body)
      let user = await User.findById(request.body.user)
      if (!user)
        return response.status(404).json({"error":"User not found"})
      let post = await Post.findById(request.body.post)
      
      if (!post)
       return response.status(404).json({"error":"Post not found"})
      
      let comment = await Comment.create(request.body)
      return response.status(201).json({"message":"Comment created", comment})
    }
    catch(err){
        return response.status(500).json({"error":"Internal server error"})
    }
}