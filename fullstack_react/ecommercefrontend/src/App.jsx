import { Route, Routes } from "react-router-dom";
import Home from "./components/home/Home";
import ViewDescription from "./components/view-description/ViewDescription";
import Signup from "./components/user/Signup";
import { ToastContainer } from "react-toastify";
import Signin from "./components/user/Signin";

function App(){
  return <>
     <ToastContainer/>
     <Routes>
       <Route path="/" element={<Home/>}/>
       <Route path="/view-description/:id" element={<ViewDescription/>}/>
       <Route path="/signup" element={<Signup/>}/>
       <Route path="/signin" element={<Signin/>}/>
     </Routes>
  </>
}

export default App;