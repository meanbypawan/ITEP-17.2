import { createSlice } from "@reduxjs/toolkit";

const slice = createSlice({
    name: "Message-Slice",
    initialState:{
        m1: "GM...",
        m2: "GN..."
    }
});

export default slice.reducer;