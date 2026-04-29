import express from "express";
import { aboutPage, contactPage, indexPage } from "../controller/index.controller.js";
// router :- It is mini express application
 const router = express.Router();
 
 router.get("/",indexPage);
 
 router.get("/about",aboutPage);

 router.get("/contact",contactPage);
 
 export default router;