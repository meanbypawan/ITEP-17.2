import { DataTypes } from "sequelize";
import sequelize from "./dbConfig.js";

const User = sequelize.define("users",{
   id:{
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
   },
   name: {
      type: DataTypes.STRING(50),
      allowNull: false
   },
   email:{
    type: DataTypes.STRING(100),
    allowNull: false,
    unique: true
   },
   password:{
    type:DataTypes.STRING,
    allowNull: false
   }
});

// Sequelize model turn into javascript class and it also
// provide interface to interact with database
// create(), findAll(), destroy(), update(), findByPk(), findOne()
export default User;