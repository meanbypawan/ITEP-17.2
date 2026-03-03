import { Sequelize } from "sequelize";

const sequelize = new Sequelize("backendapis","pawan","root",{
    host: "localhost",
    dialect: "mysql"
});

sequelize.sync()
.then(()=>{
    console.log("Database connected....");
}).catch(err=>{
    console.log(err+"connection failed...");
});
export default sequelize;