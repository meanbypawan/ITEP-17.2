import express from "express"
import { save, fetchAll, fetchById, deleteById } from "../controller/todo.controller.js"

const router = express.Router()

router.post("/",save)
router.get("/",fetchAll)
router.get("/:id",fetchById)
router.delete("/:id",deleteById)
export default router