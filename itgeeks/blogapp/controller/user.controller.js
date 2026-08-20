import { validationResult } from "express-validator"
import { User } from "../model/user.model.js"
import bcrypt from "bcryptjs"

export const signIn = async(request,response,next)=>{
    try{
      let {email,password} = request.body
      let user = await User.findOne({email})
      if(!user)
        return response.status(404).json({"error": "User not found"})
      
      let status = await bcrypt.compare(password,user.password) 
      
      return status ? response.status(200).json({"message":"Sign in success",user:{...user.toObject(),password: undefined}}): response.status(400).json({"error":"Bad request | Invalid"})
    }
    catch(err){
        return response.status(500).json({"message": "Internal Server Error"})
    }
}
export const save = async (request, response, next) => {
    try {
        const errors = validationResult(request)
        if (!errors.isEmpty())
            return response.status(400).json({ "error": errors.errors })

        let {password}  = request.body
        let saltKey = await bcrypt.genSalt(10)
        password = await bcrypt.hash(password,saltKey)
        request.body.password = password
        
        const user = await User.create(request.body)
        return response.status(201).json({"message":"user created",user})
    } catch (err) {
        console.log(err)
        return response.status(500).json({ "error": "Internal server error" })
    }

}