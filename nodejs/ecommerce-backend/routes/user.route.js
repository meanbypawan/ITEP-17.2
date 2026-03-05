import express from "express";
import { signUp, signIn } from "../controller/user.controller.js";

const router = express.Router();

// http://localhost:3000/user
router.post("/",signUp);
router.post("/signin",signIn);
export default router;