import { Route, Routes } from "react-router-dom";
import Home from "./components/Home";
import Contact from "./components/Contact";
import About from "./components/About";
import Product from "./components/Product";
import DiscountedProduct from "./components/DiscountedProduct";
import FeatureProduct from "./components/FeatureProduct";

function RouteConfig(){
    return <>
       <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="contact" element={<Contact/>}/>
        <Route path="about" element={<About/>}/>
        <Route path="product" element={<Product/>}>
          <Route path="discounted-product" element={<DiscountedProduct/>}/>
          <Route index  element={<FeatureProduct/>}/>
          <Route path="feature-product" element={<FeatureProduct/>}/>
        </Route>
       </Routes>
    </>
}

export default RouteConfig;