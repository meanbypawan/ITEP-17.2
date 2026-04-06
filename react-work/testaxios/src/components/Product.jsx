import { useEffect, useReducer } from "react";
import Header from "./Header";
import axios from "axios";

function Product(){
    const [state,dispatch] = useReducer((state,action)=>{
      if(action.type == "set-product"){
        state.productList = action.payload;
      }
      return {...state};
    },{productList:[]});
    useEffect(()=>{
        loadProduct();
    },[]);

    const loadProduct = async()=>{
      try{
        let response = await axios.get("https://dummyjson.com/products");
        dispatch({type:"set-product",payload: response.data.products});
      }
      catch(err){
        console.log(err);
      }
    }
    return <>
      <Header/>
      <div className="container mt-3">
        <h1>Product Page</h1>
        <div className="container">
            <div className="row">
                {state.productList.map((product,index)=>{return <div key={product.id} className="col-md-4 p-2">
                  <div className="d-flex flex-column" style={{minHeight:"350px", boxShadow:"10px 10px 10px grey"}}>
                       <img src={product.thumbnail} width="100%" height="250px"/>
                       <p className="text-center">{product.title}</p>
                       <h3 className="text-center text-success">{product.price} Rs.</h3>
                  </div>
                </div>})}
            </div>
        </div>
      </div>
    </>
}
export default Product;