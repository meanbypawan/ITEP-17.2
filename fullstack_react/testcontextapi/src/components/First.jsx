import { useContext } from "react"
import Second from "./Second"
import { CounterContext } from "../App"

function First(){
    
    let {counter,setCounter} = useContext(CounterContext)
    return <>
       <h2>First Component...</h2>
       <button onClick={()=>setCounter(counter-1)}>Decrement counter</button>
       <Second/>
    </>
}

export default First