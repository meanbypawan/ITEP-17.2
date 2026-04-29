import CartItems from "./cart-item.model.js";
import Cart from "./cart.model.js";
import Category from "./category.model.js";
import Product from "./product.model.js";
import User from "./user.model.js";

Category.hasMany(Product);
Product.belongsTo(Category);

User.hasOne(Cart);
Cart.belongsTo(User);

Cart.belongsToMany(Product,{through: CartItems});
Product.belongsToMany(Cart,{through:CartItems});