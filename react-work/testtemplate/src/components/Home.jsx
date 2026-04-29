import { Component } from "react";
import Header from "./Header";
import Banner from "./Banner";
import LatestProduct from "./LatestProduct";
import About from "./About";
import Footer from "./Footer";

class Home extends Component{
    render(){
        return <>
           <Header/>
           <Banner/>
           <LatestProduct/>
           <About/>
           <Footer/>
        </>
    }
}
export default Home;