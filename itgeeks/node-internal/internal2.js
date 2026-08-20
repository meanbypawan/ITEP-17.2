import crypto from "crypto"
import cluster from "cluster"
import os from "os"

if(cluster.isPrimary){
    console.log("Main/Primary Process : "+process.pid)
    for (let i=0; i<os.cpus().length; i++)
        cluster.fork()
}
else{
    console.log("Worker Thread/ Child Process : "+process.pid)
}

crypto.pbkdf2("Helloo..","fdffdfkjshfksdhfk",1000000,50,"sha256",(err,key)=>{
    console.log("crypto-1")
})

crypto.pbkdf2("Helloo..","fdffdfkjshfksdhfk",1000000,50,"sha256",(err,key)=>{
    console.log("crypto-2")
})

crypto.pbkdf2("Helloo..","fdffdfkjshfksdhfk",1000000,50,"sha256",(err,key)=>{
    console.log("crypto-3")
})

crypto.pbkdf2("Helloo..","fdffdfkjshfksdhfk",1000000,50,"sha256",(err,key)=>{
    console.log("crypto-4")
})
crypto.pbkdf2("Helloo..","fdffdfkjshfksdhfk",1000000,50,"sha256",(err,key)=>{
    console.log("crypto-5")
})
crypto.pbkdf2("Helloo..","fdffdfkjshfksdhfk",1000000,50,"sha256",(err,key)=>{
    console.log("crypto-6")
})