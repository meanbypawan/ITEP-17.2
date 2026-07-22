import { useEffect, useState } from "react";
import Nav from "./Nav";

function TestEffect(){
    const [counter,setCounter] = useState(100)
    useEffect(()=>{
        console.log("1st flevour.....")
    })
    
    useEffect(()=>{
        console.log("2nd flevour | [] dependency array | ComponentDidMount")
    },[])
    
    useEffect(()=>{
        console.log("3rd flevour | [counter] dependency | ComponentDidUpdate")
    },[counter])

    useEffect(()=>{
        return ()=>{
            console.log("4th flevour | ComponentWillUnMount")
        }
    },[])
    return <>
      <Nav/>
      <div className="container mt-3">
        <h1>TestEffect Component...</h1>
        <button onClick={()=>setCounter(counter+1)}>{counter}</button>
      </div>
    </>
}

export default TestEffect