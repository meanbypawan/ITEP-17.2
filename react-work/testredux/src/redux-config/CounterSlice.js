import { createSlice } from "@reduxjs/toolkit";

const slice = createSlice({
    name: "Counter-Slice",
    initialState:{
        counter: 100,
        evenCounter: 0,
        oddCounter: 1
    },
    reducers:{
        incrementCounter: (state,action)=>{
            state.counter = state.counter + 1
        },
        decrementCounter: (state,action)=>{
            state.counter = state.counter - 1
        },
        incrementEvenCounter:  (state,action)=>{
            state.evenCounter = state.evenCounter + 2
        },
        incrementAll: (state,action)=>{
            let val = action.payload.val*1
            state.counter = state.counter + val
            state.evenCounter = state.evenCounter + val
            state.oddCounter = state.oddCounter + val
        }
    }
});
export const {incrementAll,incrementCounter, decrementCounter, incrementEvenCounter} = slice.actions;
export default slice.reducer;