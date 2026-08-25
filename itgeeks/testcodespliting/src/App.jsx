import { Link, Route, Routes } from "react-router-dom"
import First from "./First"
import React from "react"
import HelloWithLogger from "./Third"
const Second = React.lazy(()=>import("./Second"))
function App(){
  return <>
    <h1>App component...</h1>
    <HelloWithLogger/>
    <Link to="/first">First Component..</Link>
    <Link to="/second">Second Component....</Link>
    <React.Suspense fallback={<h1>Loading.....</h1>}>
      <Routes>
        <Route path="/first" element={<First/>}/>
        <Route path="/second" element={<Second/>}/>
      </Routes>
    </React.Suspense>
  </>
}

export default App