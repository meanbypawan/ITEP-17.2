import { DataTypes } from "sequelize";
import sequelize from "../dbconfig/dbConfig.js";

const Category = sequelize.define("categories",{
    id:{
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
    },
    categoryName:{
        type: DataTypes.STRING,
        allowNull: false
    }
});
sequelize.sync()
.then(()=>{
    console.log("categories table created...");
}).catch(err=>{
    console.log(err);
})
export default Category;