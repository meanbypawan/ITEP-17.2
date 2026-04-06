import { configureStore } from "@reduxjs/toolkit";
import CounterSlice from "./CounterSlice";
import MessageSlice from "./MessageSlice"
const store  = configureStore({
    reducer:{
        counters: CounterSlice,
        messages: MessageSlice
    }
});
/*
  initialState: {counter: 100, evenCounter:0 , oddCounter: 1}

  counters: {counter: 100, evenCounter:0 , oddCounter: 1}
  messages: {m1: "GM", m2: "GN"}
  */
export default store;