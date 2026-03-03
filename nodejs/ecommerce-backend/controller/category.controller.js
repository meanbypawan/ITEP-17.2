import Category from "../model/category.model.js";

export const fetchAll = (request,response,next)=>{
    Category.findAll({raw: true})
    .then(result=>{
      return response.status(200).json(result);
    }).catch(err=>{
        return response.status(500).json({error: "Internal Server Error"});
    });
}
export const save = (request,response,next)=>{
    let {categoryName} = request.body;
    Category.create({categoryName})
    .then(result=>{
       return response.status(201).json({message: "category saved",category: result.dataValues});
    }).catch(err=>{
        return response.status(500).json({error: "Internal Server Error"});
    });
}