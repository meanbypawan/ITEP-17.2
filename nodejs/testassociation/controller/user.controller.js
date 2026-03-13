import User from "../model/user.model.js"

export const fetchUser = async(request,response,next)=>{
    try{
       let {id} = request.params; 
       let user = await User.findByPk(id);
       return response.status(200).json({user});
    }
    catch(err){
        return response.status(500).json({error: "Internal Server Error"});
    }
}
export const signUp = async (request,response,next)=>{
   try{ 
    let {name,email,password} = request.body;
    let result = await User.create({name,email,password});
    return response.status(201).json({message:"User registered successfully", user: result});
   }
   catch(err){
    console.log(err);
    return response.status(500).json({error: "Internal Server Error"});
   }
}