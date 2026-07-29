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
        },
        signOut:(state,action)=>{
            state.currentUser = null
            state.isLoggedIn = false
        }
    }

})
export const {setUser,signOut} = slice.actions

export default slice.reducer