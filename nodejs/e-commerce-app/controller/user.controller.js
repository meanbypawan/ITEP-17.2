export const signInPage = (request,response,next)=>{
    return response.render("sign-in.ejs");
}

export const signUpPage = (request,response,next)=>{
    return response.render("sign-up.ejs");
}
export const signUpAction = (request,response,next)=>{
    //console.log(request.body);
    // save data in datbase
}