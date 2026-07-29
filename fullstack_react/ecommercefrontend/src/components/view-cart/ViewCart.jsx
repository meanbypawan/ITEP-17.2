import { useEffect, useReducer } from "react";
import Nav from "../nav/Nav";
import { toast } from "react-toastify";
import axios from "axios";
import { BASE_URL } from "../../Api";
import { useSelector } from "react-redux";

function ViewCart(){
    const {currentUser} = useSelector((store)=>store.user)
    let [state,dispatch] = useReducer((state,action)=>{
        if(action.type == "set-cart-items"){
            let itemList = []
            for(let item of action.payload){
                item.product.qty = 1
                item.product.totalPrice = item.product.price
                itemList.push(item.product)
                state.totalBillAmount = state.totalBillAmount + item.product.qty * item.product.price
            }
            state.cartItems = itemList
            console.log(state.cartItems)
        }    
        else if(action.type == "update-qty"){
           console.log("update-qty called...") 
           let productId = action.payload.id
           let qty = action.payload.qty
           let index = state.cartItems.findIndex((item)=>{return item.id == productId})
           let product = state.cartItems[index]
           state.cartItems.splice(index,1)
           product.qty = qty
           product.totalPrice = product.price * qty
           state.cartItems.splice(index,0,product)

           state.totalBillAmount = 0
           for(let item of state.cartItems){
             state.totalBillAmount = state.totalBillAmount + item.totalPrice
           }
        }
        return {...state}
    },{
        cartItems: [],totalBillAmount: 0
    })
    useEffect(()=>{
        loadCartItems()
    },[])

    const loadCartItems = async()=>{
        try{
           const response = await axios.get(BASE_URL+`/cart/${currentUser.id}`)
           dispatch({type:"set-cart-items",payload: response.data.cart_items})
        }
        catch(err){
            console.log(err)
            toast.error("Something wrong...")
        }
    }
    
    return <>
      <Nav/>
      <div className="container mt-3">
         <div className="row">
            <div className="col-md-8 border">
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th>S.no</th>
                            <th>Title</th>
                            <th>Image</th>
                            <th>Price</th>
                            <th>Total price</th>
                            <th>Qty</th>
                            <th>Remove</th>
                        </tr>
                    </thead>
                    <tbody>
                       {state.cartItems?.map((cartItem,index)=>{return <tr key={cartItem?.id}>
                         <td>{index+1}</td>
                         <td>{cartItem?.title}</td>
                         <td>
                            <img src={BASE_URL+`${cartItem?.product_image}`} width="50px" height="50px"/>
                         </td>
                         <td>{cartItem?.price}</td>
                         <td id={`total-price`+cartItem.id}>{cartItem?.totalPrice}</td>
                         <td>
                            <input onChange={(event)=>dispatch({type:"update-qty",payload:{id: cartItem.id, qty: event.target.value}})} type="number" defaultValue="1" min="1" style={{width:"50px"}}/>
                         </td>
                         <td>
                            <button className="btn btn-outline-danger">Remove</button>
                         </td>
                       </tr>})}           
                    </tbody>
                </table>
            </div>
            <div className="col-md-4 border">
                <h4 className="bg-warning text-white p-2">Bill Summery</h4>
                <p><b>Total Item : </b>{state.cartItems.length}</p>
                <p><b>Bill Amount :</b> <span className="text-success" style={{fontSize:"18px", fontWeight:"bolder"}}>{state.totalBillAmount} Rs.</span></p>
                <button className="btn btn-warning">Checkout</button> 
            </div>
         </div>
      </div>
    </>
}

export default ViewCart;