import { Route, Routes } from "react-router-dom";
import Home from "./components/Home";
import Product from "./components/Product";

function App(){
  return <>
    <Routes>
      <Route path="/" element={<Home/>}/>
      <Route path="product" element={<Product/>}/>
    </Routes>
  </>
}
export default App;