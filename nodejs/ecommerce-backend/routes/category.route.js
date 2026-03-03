import express from "express";
import { save, fetchAll } from "../controller/category.controller.js";

const router = express.Router();

// POST:-http://localhost:3000/category
router.post("/",save);
router.get("/",fetchAll);
export default router;