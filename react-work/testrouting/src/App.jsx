import { Link, Route, Routes } from "react-router-dom";
import RouteConfig from "./RouteConfig";
import { useState } from "react";

function App(){
  const [counter,setCounter] = useState(100);
  return <>
    <div className="d-flex p-2 justify-content-around bg-danger text-white">
      <Link to="/"><span>Home</span></Link>
      <Link to="/about"><span>About</span></Link>
      <Link to="/contact"><span>Contact us</span></Link>
      <Link to="/product"><span>Product</span></Link>
    </div> 
    <button onClick={()=>{setCounter(counter+1)}}>Increment :{counter}</button>
    <RouteConfig/>
  </>
}

export default App;