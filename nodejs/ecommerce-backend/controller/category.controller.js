import Category from "../model/category.model.js";
export const deleteCategory = async (request,response,next)=>{
   try{
    let category = await Category.findOne({where:{id: request.params.id},raw: true});

    if(!category)
        return response.status(404).json({error: "Resource not found"});
    
    await Category.destroy({where:{id: request.params.id}});
    return response.status(200).json({message:"category deleted..."});
   }
   catch(err){
    console.log(err);
    return response.status(500).json({error: "Internal Server Error"});
   } 
}
export const update = async (request,response,next)=>{
   try{ 
    let {id} = request.params;
    let dbCategory = await Category.findOne({where:{id},raw: true});
    if(!dbCategory)
        return response.status(404).json({error: "Requested resource not available | id not found"});
  
    await Category.update({categoryName: request.body.categoryName},{where:{id}});

    return response.status(200).json({message: "Category updated"});
   }
   catch(err){
    console.log(err);
    return response.status(500).json({error: "Internal Server Error"});
   } 
}
export const fetchById = (request,response,next)=>{
    let {id} = request.params;
    Category.findByPk(id,{raw: true})
    .then(result=>{
        return response.status(200).json(result);
    }).catch(err=>{
        console.log(err);
        return response.status(500).json({error: "Internal Server Error"});
    });
}
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