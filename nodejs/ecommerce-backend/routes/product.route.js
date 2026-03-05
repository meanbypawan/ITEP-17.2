import express from "express";
import { fetchAll, save } from "../controller/product.controller.js";

const router = express.Router();

router.get("/",fetchAll); // Fetch All Product
router.post("/",save);
// router.get("/:id"); // Fetch product by id
// router.put("/:id"); // Update product
// router.delete("/:id"); // Delete product
export default router;