import jwt from "jsonwebtoken";
import dotenv from "dotenv";
dotenv.config();
export const auth = async (request,response,next)=>{
  try{
    if(request.headers.authorization){
       let token = request.headers.authorization.split(" ")[1]; 
       console.log(token);
       await jwt.verify(token,process.env.SECRET_KEY);
       console.log("Token Successfully Verified.....");
       //console.log(jwt.decode(token));
       next(); 
    }
    else 
      throw new Error();
  }
  catch(err){
    console.log(err);
    return response.status(401).json({error: "Unauthorized Access"});
  }
}