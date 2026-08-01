import axios from "axios";
import { useRef } from "react";
import { useLocation } from "react-router-dom";
import BASE_URL  from "../../Api";
import { toast } from "react-toastify";
import axiosInstance from "../../axios-config/api";

function PlaceOrder(){
    const location = useLocation()
    
    let {cartItems,totalBillAmount,currentUser} = location.state.params
    let nameRef = useRef("")
    let emailRef = useRef("")
    let contactRef = useRef("")
    let deliveryAddressRef = useRef("")

    console.log(cartItems)
    console.log(totalBillAmount)
    console.log(currentUser)
    const handleSubmit = async (event)=>{
      try{
        event.preventDefault()
        let name = nameRef.current.value
        let email = emailRef.current.value
        let contact = contactRef.current.value
        let address = deliveryAddressRef.current.value
        
        let orderDetails = {
            "user_id":currentUser.id,
            "totalBillAmount": totalBillAmount,
            "name": name,
            "email":email,
            "contact" : contact,
            "address": address,
            "order_items":cartItems
        }
        // Call place order api
        let response = await axiosInstance.post("/orders/",orderDetails)
        toast.success("Order placed successfully.....")
      }
      catch(err){
        toast.error("Oops! something went wrong...")
        console.log(err)
      } 
    }
    return <>
       <h1>Enter order details</h1>
       <div className="container">
        <form onSubmit={handleSubmit}>
            <div className="form-group">
                <label>Enter name</label>
                <input ref={nameRef} value={currentUser.name} type="text" className="text-capitalize form-control"/>
            </div>
            <div className="form-group">
                <label>Enter email id</label>
                <input ref={emailRef} value={currentUser.email} type="text" className="form-control"/>
            </div>
            <div className="form-group">
                <label>Enter contact number</label>
                <input ref={contactRef} value={currentUser.contact} type="text" className="form-control"/>
            </div>
            <div>
                <label>Enter delivery address</label>
                <textarea ref={deliveryAddressRef} className="form-control"></textarea>
            </div>
            <div className="form-group mt-2">
                <button className="btn btn-secondary">Place order</button>
            </div>
        </form>
       </div>
    </>
}

export default PlaceOrder;