import { useState } from "react"

function Add(){
    const [result,setResult] = useState(0)
    const add = ()=>{
        let firstValue = document.getElementById("first").value
        let secondValue = document.getElementById("second").value

        firstValue = firstValue*1
        secondValue = secondValue*1

        setResult(firstValue + secondValue)
    }
    return <>
      <hr/>
        <h1>Add Component...Using ID</h1>
        <input id="first" placeholder="Enter first number.."/>
        <input id="second" placeholder="Enter second number..."/>
        <button onClick={add}>ADD</button>
        <h1 id='result'>Result : {result}</h1>
      <hr/>
    </>
}

export default Add