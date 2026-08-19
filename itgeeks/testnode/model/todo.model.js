import mongoose, { Types } from "mongoose"

const todoSchema = new mongoose.Schema({
    title: String,
    priority: String,
    description: String,
    status:{
        type: String,
        default: "Pending"
    }
})

export const ToDo = mongoose.model("todos",todoSchema)
/*
  mongoose.mode() create model class and it also
  provide interface to interact with database
  ToDo.create()
  ToDo.find()
  ToDo.findOne()
  ToDo.updateOne()
  ToDo.deleteOne()
*/