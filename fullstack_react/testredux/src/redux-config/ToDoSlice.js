import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import axios from "axios";

export const fetchToDos = createAsyncThunk("ToDoSlice/fetchToDos",async ()=>{
   const response = await axios.get("https://dummyjson.com/todos")
   return response.data.todos
});

const slice = createSlice({
    name:"ToDoSlice",
    initialState:{
        todos: [],
        error: false,
        isLoading: false
    },
    extraReducers:(builder)=>{
        builder.addCase(fetchToDos.fulfilled,(state,action)=>{
            console.log("Promise is fullfilled.....")
            console.log(action)
            state.todos = action.payload
            state.isLoading = false
        })
        .addCase(fetchToDos.rejected,(state,action)=>{
           state.error = true
           state.isLoading = false
        })
        .addCase(fetchToDos.pending,(state,action)=>{
            state.isLoading = true
        })
    }
})

export default slice.reducer