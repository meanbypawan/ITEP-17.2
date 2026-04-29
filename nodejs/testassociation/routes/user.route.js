import express from "express";
import { signUp, fetchUser } from "../controller/user.controller.js";

const router = express.Router();
router.post("/",signUp);
router.get("/:id",fetchUser);
export default router;