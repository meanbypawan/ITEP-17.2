export  const indexPage = (request,response,next)=>{
    return response.render("index.ejs");
}
export const aboutPage = (request,response,next)=>{
    return response.render("about.ejs");
 }

 export const contactPage = (request,response,next)=>{
    return response.render("contact.ejs");
 }