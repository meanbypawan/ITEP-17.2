import { useCallback, useState } from "react";
import First from "./First";

function App(){
  const [counter,setCounter] = useState(100)
  console.log("App Render...")
  const sayHello = useCallback(()=>{
    window.alert("Hello Friends...")
  },[])
  return <>
    <h1>App Component...</h1>
    <button onClick={()=>setCounter(counter+1)}>Counter : {counter}</button>
    <First sayHello = {sayHello}/>
  </>
}

export default App;