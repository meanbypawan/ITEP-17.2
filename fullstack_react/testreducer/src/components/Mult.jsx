import { useState } from "react"

function Mult(){
    const [result,setResult] = useState(0)
    const [firstValue,setFirstValue] = useState(0)
    const [secondValue,setSecondValue] = useState(0)
    const mult = ()=>{
        setResult(firstValue * secondValue)
    }
    return <>
      <hr/>
        <h1>Mult. Component...Using State</h1>
        <input onChange={(event)=>{setFirstValue(event.target.value*1)}} placeholder="Enter first number.."/>
        <input onChange={(event)=>{setSecondValue(event.target.value*1)}} placeholder="Enter second number..."/>
        <button onClick={mult}>Mult.</button>
        <h1 id='result'>Result : {result}</h1>
      <hr/>
    </>
}
export default Mult