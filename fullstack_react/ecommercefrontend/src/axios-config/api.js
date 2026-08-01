import axios from "axios";
import store from "../redux-config/store"
const axiosInstance = axios.create({
    baseURL: "http://localhost:8000"
})

axiosInstance.interceptors.request.use((config)=>{
    const token =  store.getState().user?.currentUser?.token
    if(token)
        config.headers.Authorization = "Bearer "+token
    return config
},(err)=>Promise.reject(err))

export default axiosInstance;