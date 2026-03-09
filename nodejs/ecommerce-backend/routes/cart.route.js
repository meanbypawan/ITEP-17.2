import express from "express";
import { addToCart, fetchCartItems } from "../controller/cart.controller.js";
import { auth } from "../middleware/auth.js";
const router = express.Router();

router.post("/",auth, addToCart);
router.get("/:userId",auth,fetchCartItems);
export default router;