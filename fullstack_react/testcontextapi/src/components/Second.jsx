import { useContext } from "react"
import { CounterContext, MessageContext } from "../App"

function Second(){
    let {m1,m2} = useContext(MessageContext)
    let {counter,setCounter} = useContext(CounterContext)
    return <>
      <h2>Second Component...{m1} : {m2}</h2>
      <button onClick={()=>setCounter(counter+1)}>Increment Counter</button>
    </>
}

export default Second