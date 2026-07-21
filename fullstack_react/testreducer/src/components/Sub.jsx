import { useRef, useState } from "react"

function Sub(){
    let firstInput = useRef(0)
    let secondInput = useRef(0)
    const [result,setResult] = useState(0)
    const sub = ()=>{
        let firstValue = firstInput.current.value*1
        let secondValue = secondInput.current.value*1
        setResult(firstValue - secondValue)
    }
    return <>
      <hr/>
        <h1>Sub Component...Using Ref:</h1>
        <input ref={firstInput} id="first" placeholder="Enter first number.."/>
        <input ref={secondInput} id="second" placeholder="Enter second number..."/>
        <button onClick={sub}>Sub</button>
        <h1>Result : {result}</h1>
      <hr/>
    </>
}

export default Sub