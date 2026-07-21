import { useReducer } from "react";
import CounterComp from "./components/CounterComp";
import Add from "./components/Add";
import Mult from "./components/Mult";
import Sub from "./components/Sub";

function App(){
  
  return <>
     {/* <CounterComp/> */}
     <Add/>
     <Mult/>
     <Sub/>
  </>
}

export default App;