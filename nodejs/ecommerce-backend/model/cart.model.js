import { DataTypes } from "sequelize";
import sequelize from "../dbconfig/dbConfig.js";

const Cart = sequelize.define("carts",{
    id:{
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
    }
});

export default Cart;