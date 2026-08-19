import { ToDo } from "../model/todo.model.js"

export const deleteById = async (request,response,next)=>{
    try{
       let todo = await ToDo.findById(request.params.id)
       if (todo){ // null undefined false "" 0 NaN []
           await todo.deleteOne()
           return response.status(200).json({"message":"ToDo Deleted","todo": todo})
       }
       return response.status(404).json({error: "Resouce not found"}) 
    }
    catch(err){
        console.log(err)
        return response.status(500).json({"error":"Internal Server Error"})
    }
    
}
export const fetchById = (request,response,next)=>{
  let id = request.params.id
  console.log(id)
  ToDo.findById(id).then(result=>{
    return response.status(200).json({"todo": result})
  }).catch(err=>{
    console.log(err)
    return response.status(500).json({"error": "Internal server error.."})
  })
}
export const fetchAll = (request,response,next)=>{
    ToDo.find()
    .then(results=>{
        return response.status(200).json({"nishi_ki_todos_list": results})
    }).catch(err=>{
        console.log(err)
        return response.status(500).json({"error":"Internal server error"})
    })
}
export const save = async (request,response,next)=>{
   try{
      let result = await ToDo.create(request.body)
      return response.status(201).json({"todoDetail": result})
   }
   catch(err){
    console.log(err)
    return response.status(500).json({"error":"Internal Server Error"})
   }
}