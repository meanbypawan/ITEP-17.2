import mysql from "mysql2";

const pool = mysql.createPool({
    host: "localhost",
    user: "pawan",
    password: "root",
    database: "ecomdb",
    connectionLimit: 100
}); // meta-object

export default pool;