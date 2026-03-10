import { Sequelize } from "sequelize";

const sequelize = new Sequelize("socialapp","pawan","root",{
    host: "localhost",
    dialect: "mysql"
});


sequelize.sync()
.then(result=>{
    console.log("Database connected...");
}).catch(err=>{
    console.log(err);
})
export default sequelize;