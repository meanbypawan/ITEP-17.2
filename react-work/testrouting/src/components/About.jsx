import { useEffect, useState } from "react";

function About(){
    const [counter,setCounter] = useState(100);
    useEffect(()=>{
        console.log("1st felvour.....");
    });
    useEffect(()=>{
        console.log("2nd flevour | componentDidMount()");
    },[]);
    useEffect(()=>{
        console.log("3rd flevour | componentDidUpdate()");
    },[counter]);
    useEffect(()=>{
        console.log("4th flevour..");
        const interval = setInterval(()=>{
            console.log("Interval Executing......");
        },1000);
        return ()=>{
            console.log("4th flevour -> componentWillUnMount()");
            clearInterval(interval);
        }
    },[]);
    console.log("component  render...");
    return <>
      <div className="container mt-2">
        <h1>About Component...</h1>
        <button onClick={()=>{setCounter(counter+1)}}>Counter : {counter}</button>
      </div>
    </>
}
export default About;