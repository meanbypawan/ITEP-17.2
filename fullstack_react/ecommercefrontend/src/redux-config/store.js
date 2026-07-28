import { configureStore } from "@reduxjs/toolkit";
import UserSlice from "./UserSlice"
const store = configureStore({
    reducer:{
        user: UserSlice
    }
})
// user: {currentUser: {},isLoggedIn}
export default store