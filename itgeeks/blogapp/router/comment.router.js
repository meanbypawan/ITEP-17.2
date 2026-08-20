import express from "express"
import { createComment } from "../controller/comment.controller.js";

const router = express.Router()

router.post("/",createComment);
export default router