import express from "express"
import { save, signIn } from "../controller/user.controller.js";
import {body} from "express-validator"
const router = express.Router()

// http://localhost:3000/user
router.post("/", body("name", "name is requred").notEmpty(),
    body("email", "email is required").notEmpty(),
    body("email", "invalid email id").isEmail(),
    body("password", "password is required..").notEmpty(), save);

router.post("/signin",signIn)    
export default router