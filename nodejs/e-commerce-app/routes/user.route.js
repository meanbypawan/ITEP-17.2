import express from "express";
import { signInPage, signUpPage, signUpAction, signInAction } from "../controller/user.controller.js";
const router = express.Router();

router.get("/sign-in",signInPage);
router.get("/sign-up",signUpPage);

router.post("/sign-up",signUpAction);
router.post("/sign-in",signInAction);
export default router;