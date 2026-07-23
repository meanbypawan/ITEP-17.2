import { configureStore } from "@reduxjs/toolkit";
import CounterSlice from "./CounterSlice"
import ToDoSlice from "./ToDoSlice"
const store = configureStore({
    reducer:{
        CounterData: CounterSlice,
        ToDos: ToDoSlice 
    }
})
// CounterData : {counter:100,evenCounter:0,oddCounter:1}
// ToDos: {todos: []}
export default store