import { createSlice } from "@reduxjs/toolkit";

const slice = createSlice({
    name: "UserSlice",
    initialState:{
        currentUser: null,
        isLoggedIn: false
    },
    reducers:{
        setUser: (state,action)=>{
           state.currentUser = action.payload
           state.isLoggedIn = true
           console.log(state)
        }
    }

})
export const {setUser} = slice.actions

export default slice.reducer