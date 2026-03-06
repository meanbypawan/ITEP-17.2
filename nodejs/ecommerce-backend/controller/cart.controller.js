import sequelize from "../dbconfig/dbConfig.js";
import CartItems from "../model/cart-item.model.js";
import Cart from "../model/cart.model.js";

export const addToCart = async (request, response, next)=>{
   let transaction = await sequelize.transaction(); 
   try{ 
    let {userId,productId} = request.body;

    let cart =  await Cart.findOne({where:{userId},raw: true}); 
    if(cart){
      let cartItems =   await CartItems.findOne({where:{cartId: cart.id, productId}}); 
      if(cartItems)
        return response.status(200).json({message:"Item already added in cart."});
      await CartItems.create({cartId: cart.id, productId},{transaction});
      transaction.commit();
      return response.status(201).json({message: "Item successfully added in cart"});
    }
    else{
       let cart = await Cart.create({userId},{transaction}).then(result=>{
        return result.dataValues;
       }); 
       await CartItems.create({cartId: cart.id, productId},{transaction});
       await transaction.commit();
       return response.status(201).json({message: "Item successfully added in cart"});
    }
   }
   catch(err){
     console.log(err);
     await transaction.rollback();
     return response.status(500).json({error: "Internal Server Error"});
   }
}