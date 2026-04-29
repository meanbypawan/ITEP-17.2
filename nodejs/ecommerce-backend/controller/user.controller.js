import bcrypt from "bcryptjs";
import User from "../model/user.model.js";
import jwt from "jsonwebtoken";
import dotenv from "dotenv";
dotenv.config();
export const signIn = async(request,response,next)=>{
    try{
      let {email,password} = request.body;
      let dbUser = await User.findOne({where:{email},raw: true});
      if(!dbUser)
        return response.status(404).json({error:"Resource not found"});
      let hashPassword = dbUser.password;
      let status = await bcrypt.compare(password,hashPassword);    
      return status ? response.status(200).json({message:"Sign in success", token: generateToken(dbUser)}) : response.status(401).json({error:"Unauthorised user"});
    }
    catch(err){
        return response.status(500).json({error: "Internal Server Error"});
    }
}
const generateToken = (dbUser)=>{
  let payload = {userId: dbUser.id, email: dbUser.email};
  return jwt.sign(payload,process.env.SECRET_KEY,{expiresIn: "30m"});
}
export const signUp = async (request,response,next)=>{
   try{ 
    let {email,password,contact} = request.body;
    let saltKey = await bcrypt.genSalt(10);
    password = await bcrypt.hash(password,saltKey);
    let user = await User.create({email,password,contact});
    return response.status(201).json({message: "User created..",user});
   }
   catch(err){
     return response.status(500).json({error: "Internal Server Error"});
   }
}