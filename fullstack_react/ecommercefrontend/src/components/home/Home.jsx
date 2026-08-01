import { useEffect, useReducer } from "react";
import Nav from "../nav/Nav";
import axios from "axios";
import  BASE_URL  from "../../Api";
import { useNavigate } from "react-router-dom";
import axiosInstance from "../../axios-config/api";

function Home(){
    const [state,dispatch] = useReducer((state,action)=>{
        if(action.type == "set-categories")
            state.categories = action.payload
        else if(action.type == "set-products")
            state.products = action.payload
        return {...state}
    },{
        categories: [],
        products: []
    });
    useEffect(()=>{
        loadCategories()
        loadProducts()
    },[])
    const loadCategories = async ()=>{
        const response = await axiosInstance.get("/category/")
        dispatch({type:"set-categories",payload: response.data})
    }
    const loadProducts = async()=>{
        const response = await axiosInstance.get("/product/")
        dispatch({type:"set-products",payload: response.data})
    }
    const navigate = useNavigate()
    return <>
      <Nav/>
      <div className="container mt-3">
        <div className="row">
            {state?.categories.map((category,index)=>{return <div key={category.id} className="col-md-2">
                <div className="category-container border d-flex justify-content-around align-items-center" style={{height:"60px"}}>
                    <img src={BASE_URL+category.category_image} width="50px" height="50px"/>
                    <label style={{fontSize:"12px"}}>{category.category_name}</label>
                </div>
            </div>})}
        </div>
        <hr/>
        <div className="row">
            {state?.products.map((product,index)=>{return <div className="col-md-3" key={product.id}>
                <div className="product-card border d-flex flex-column align-items-center justify-content-between" style={{minHeight:"300px"}}>
                    <img src={BASE_URL+product.product_image} style={{height:"200px",width:"100%"}}/>
                    <h5>{product.title}</h5>
                    <h3 className="text-success">{product.price} Rs.</h3>
                    <button onClick={()=>{navigate(`/view-description/${product.id}`)}} className="btn btn-warning text-white" style={{width:"100%"}}>View description</button>
                </div>
            </div>})}
        </div>
      </div>
    </>
}

export default Home