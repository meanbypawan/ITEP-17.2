import { DataTypes } from "sequelize";
import sequelize from "./dbConfig.js";

const Profile = sequelize.define("profiles",{
    id:{
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
    },
    bio:{
        type: DataTypes.STRING,
        allowNull: false
    }
});
export default Profile;