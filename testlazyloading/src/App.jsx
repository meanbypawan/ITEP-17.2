import { Link, Route, Routes } from "react-router-dom";
import First from "./First";
import React from "react";
const Second = React.lazy(()=>import("./Second"))
function App(){
  return <>
    <Link to="/first">First</Link>
    <Link to="/second">Second</Link>
    <h1>App Component...</h1>
    <React.Suspense fallback={<h2>Second is loading...</h2>}>
      <Routes>
        <Route path="/first" element={<First/>}/>
        <Route path="/second" element={<Second/>}/>
      </Routes>
    </React.Suspense>
  </>
}

export default App;