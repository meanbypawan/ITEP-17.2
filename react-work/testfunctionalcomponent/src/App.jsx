import { useState } from "react";
import Home from "./components/Home";

function App(){
   const [counter,setCounter] =  useState(100);
   const [evenCounter,setEvenCounter] = useState(0);
   const [oddCounter,setOddCounter] = useState(1);
   const incrementCounter = ()=>{
      setCounter(counter+1);
   }
   return <>
     <h1>App Component...{counter} : {evenCounter} : {oddCounter}</h1>
     <button onClick={incrementCounter}>Increment Counter</button>
     <button onClick={()=>{setEvenCounter(evenCounter+2)}}>Increment Even Counter</button>
     <button onClick={()=>{setOddCounter(oddCounter+2)}}>Increment Odd Counter</button> 
     <Home/>
   </>
}

export default App;