import axios from "axios";
import { useRef } from "react";
import Api from "../../Api";
import { toast } from "react-toastify";
import { Link } from "react-router-dom";

function Signup(){
    const nameInput = useRef("")
    const emailInput = useRef("")
    const passwordInput = useRef("")
    const contactInput = useRef("")
    const handleSubmit = async (event)=>{
      try{  
        event.preventDefault()
        const name = nameInput.current.value
        const email = emailInput.current.value
        const password = passwordInput.current.value
        const contact = contactInput.current.value
        let response = await axios.post(Api.CREATE_USER,{name,email,password,contact})
        
      }
      catch(err){
        toast.error("Oops ! something went wrong..")
      }  
    }
    return <>
      <div className="container-fluid d-flex justify-content-center align-items-center" style={{height:"600px"}}>
        <div className="border" style={{width:"40%", minHeight:"300px"}}>
            <form onSubmit={handleSubmit} className="p-3">
                <div className="form-group">
                    <label>Enter name</label>
                    <input ref={nameInput} className="form-control" type="text"/>
                </div>
                <div className="form-group">
                    <label>Enter email id</label>
                    <input ref={emailInput} className="form-control" type="email"/>
                </div>
                <div className="form-group">
                    <label>Enter password</label>
                    <input ref={passwordInput} className="form-control" type="password"/>
                </div>
                <div className="form-group">
                    <label>Enter contact number</label>
                    <input ref={contactInput} className="form-control" type="text"/>
                </div>
                <div className="form-group">
                    <button className="btn btn-warning">Sign up</button>
                    <Link to="/signin">Already have account ?</Link>
                </div>
            </form>
        </div>
      </div>
    </>
}
export default Signup;