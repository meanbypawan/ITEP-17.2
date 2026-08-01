import { useCallback, useMemo, useState } from "react"
import First from "./First"
import Second from "./Second"
import Third from "./Third"
import Fourth from "./Fourth"

function App(){
  const [counter,setCounter] = useState(100)
  console.log("App Rerender....")
  const [evenCounter,setEvenCounter] = useState(0)
  let wishingMessage = {m1:"GM",m2:"GN",evenCounter: evenCounter}
  wishingMessage = useMemo(()=>wishingMessage,[evenCounter])
  
  let sayHello = ()=>{
    window.alert("Hello Friends.....")
  }
  
  sayHello = useCallback(()=>sayHello,[])
  
  return <>
    <h1>App component...</h1>
    <button onClick={()=>setCounter(counter+1)}>Counter : {counter}</button>
    <button onClick={()=>setEvenCounter(evenCounter+2)}>Even Counter : {evenCounter}</button>
    <First/>
    <Second message="Hello...."/>
    <Third wishingMessage={wishingMessage}/>
    <Fourth sayHello={sayHello}/>
  </>
}

export default App