import Category from "../model/category.model.js";
import Product from "../model/product.model.js";
export const save = async (request,response,next)=>{
   try{ 
    let {title,brand,price,categoryId} = request.body;
    let dbCategory = await Category.findByPk(categoryId);
    if(!dbCategory)
        return response.status(404).json({error:"Category not found"});
    let result = await Product.create({title,brand,price,categoryId});
    return response.status(201).json({message:"product saved..",product: result.dataValues});
   }
   catch(err){
    return response.status(500).json({error: "Internal Server Error"});
   }
}
export const fetchAll = async(request,response,next)=>{
   try{
      let productList = await Product.findAll({raw: true});
      return response.status(200).json({products: productList});
   }
   catch(err){
    console.log(err);
    return response.status(500).json({error: "Internal Server Error"});
   }
}