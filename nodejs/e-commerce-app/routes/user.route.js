import express from "express";
import { signInPage, signUpPage, signUpAction } from "../controller/user.controller.js";
const router = express.Router();

router.get("/sign-in",signInPage);
router.get("/sign-up",signUpPage);

router.post("/sign-up",signUpAction);
export default router;