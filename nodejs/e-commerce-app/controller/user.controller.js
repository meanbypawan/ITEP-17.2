import pool from "../dbconfig/dbConfig.js";
export const signInPage = (request,response,next)=>{
    return response.render("sign-in.ejs");
}

export const signUpPage = (request,response,next)=>{
    return response.render("sign-up.ejs");
}
export const signUpAction = (request,response,next)=>{
  const {username,email,password,contact} = request.body;   
  pool.getConnection((err,con)=>{
     if(!err){
        let sql = "insert into users(username,email,password,contact) values(?,?,?,?)";
        con.query(sql,[username,email,password,contact],(err,result)=>{
          con.release();  
          return err ? response.render("error.ejs") : response.redirect("/user/sign-in");
        });
     }
     else
        console.log(err);
  });
}

export const signInAction = (request,response,next)=>{
    let {email,password} = request.body;
    console.log(email+"  "+password);
    pool.getConnection((err,con)=>{
        if(!err){
          let sql = "select * from users where email = ? and password = ?";
          con.query(sql,[email,password],(err,result)=>{
            if(!err){
                if(result.length)
                    return response.end("Sign in success..");
                return response.end("Sign in failed...");
            }
            else
                return response.render("error.ejs");
          });
        }
        else{
            console.log(err);
            return response.render("error.ejs");
        }   
    });
}