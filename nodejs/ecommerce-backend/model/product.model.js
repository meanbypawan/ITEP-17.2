import { DataTypes } from "sequelize";
import sequelize from "../dbconfig/dbConfig.js";

const Product = sequelize.define("products",{
    id:{
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
    },
    title:{
        type: DataTypes.STRING,
        allowNull: false
    },
    price:{
        type: DataTypes.FLOAT,
        allowNull: false
    },
    brand:DataTypes.STRING
});
sequelize.sync()
.then(result=>{
    console.log("Database synced....");
}).catch(err=>{
    console.log(err);
})
export default Product;