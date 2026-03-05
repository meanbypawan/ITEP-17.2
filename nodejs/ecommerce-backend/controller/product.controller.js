import Product from "../model/product.model.js";
export const save = (request,response,next)=>{
    console.log(request.body);
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