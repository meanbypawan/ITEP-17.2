import axios from "axios"
import { useRef } from "react"
import { Link, useNavigate } from "react-router-dom"
import { toast } from "react-toastify"
import { useDispatch } from "react-redux"
import { setUser } from "../../redux-config/UserSlice"
import axiosInstance from "../../axios-config/api"

function Signin(){
    const emailInput = useRef("")
    const passwordInput = useRef("")
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const handleSubmit = async (event)=>{
      try{
        event.preventDefault()
        const userEmail = emailInput.current.value
        const userPassword = passwordInput.current.value
        const response = await axiosInstance.post("/user/signin",{email: userEmail,password: userPassword})
        dispatch(setUser(response.data))
        toast.success("Sign in success....")
        navigate("/")
      }
      catch(err){
        toast.error(`${err}`)
      }
    }
    return <>
     <div className="container-fluid d-flex justify-content-center align-items-center" style={{height:"600px"}}>
        <div className="border" style={{width:"40%", minHeight:"300px"}}>
            <form onSubmit={handleSubmit} className="p-3">
                <div className="form-group">
                    <label>Enter email id</label>
                    <input ref={emailInput} className="form-control" type="email"/>
                </div>
                <div className="form-group">
                    <label>Enter password</label>
                    <input ref={passwordInput} className="form-control" type="password"/>
                </div>
                <div className="form-group">
                    <button className="btn btn-warning mr-2">Sign in</button>
                    <Link  to="/signup">Create new account</Link>
                </div>
            </form>
        </div>
      </div>
    </>
}

export default Signin