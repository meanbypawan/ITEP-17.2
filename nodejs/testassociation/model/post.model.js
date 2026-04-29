import { DataTypes } from "sequelize";
import sequelize from "./dbConfig.js";

const Post = sequelize.define("posts",{
    id:{
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
    },
    postText:{
        type: DataTypes.STRING,
        allowNull: false
    }
});

export default Post;