import express from "express";
import { save, fetchAll, fetchById, update, deleteCategory } from "../controller/category.controller.js";

const router = express.Router();

// POST:-http://localhost:3000/category
router.post("/",save);
router.get("/",fetchAll);
// GET:-http://localhost:3000/category/200
router.get("/:id",fetchById);
router.put("/:id",update);
router.delete("/:id",deleteCategory);
export default router;