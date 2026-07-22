import { Route, Routes } from "react-router-dom"
import About from "./About"
import Contact from "./Contact"
import Home from "./Home"
import TestEffect from "./TestEffect"
import Quotes from "./Quotes"

function RouteConfig(){
    return <>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/contact" element={<Contact/>}/>
        <Route path="/about" element={<About/>}/>
        <Route path="/use-effect" element={<TestEffect/>}/>
        <Route path="/quotes" element={<Quotes/>}/>
     </Routes>
    </>
}

export default RouteConfig