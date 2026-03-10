import sequelize from "./dbConfig.js";
import Post from "./post.model.js";
import Profile from "./profile.model.js";
import User from "./user.model.js";

User.hasOne(Profile,{
    onDelete: "cascade"
});

Profile.belongsTo(User);

User.hasMany(Post);
Post.belongsTo(User);