import express from "express"
import multer from "multer"
import { createPost, fetchPost } from "../controller/post.controller.js"
const upload = multer({"dest": "public/images"})
const router = express.Router()

router.post("/",upload.single("image"),createPost)
router.get("/",fetchPost)
export default router