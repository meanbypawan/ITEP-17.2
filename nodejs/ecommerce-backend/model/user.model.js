import { DataTypes } from "sequelize";
import sequelize from "../dbconfig/dbConfig.js";

const User = sequelize.define("users",{
    id:{
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
    },
    email:{
        type: DataTypes.STRING,
        allowNull: false,
        unique: true
    },
    password:{
        type: DataTypes.STRING,
        allowNull: false
    },
    contact:{
        type: DataTypes.STRING
    }
});
sequelize.sync()
.then(()=>{
    console.log("User table created...");
}).catch(err=>{
    console.log(err);
})
export default User;