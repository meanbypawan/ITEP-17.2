import { useEffect, useReducer } from "react";
import Nav from "./Nav";
import axios from "axios";

function Quotes(){
    const [state,dispatch] = useReducer((state,action)=>{
        if(action.type == "set-quotes"){
           state.quotes = action.payload
        }
        return {...state}
    },{quotes:[]})
    useEffect(()=>{
        loadQuotes()
    },[])
    const loadQuotes = ()=>{
       axios.get("https://dummyjson.com/quotes")
       .then((response)=>{
          dispatch({type:"set-quotes",payload: response.data.quotes})
          console.log(state.quotes)
       }).catch((err)=>{
         console.log(err)
       });
    }
    return <>
      <Nav/>
      <div className="container mt-3">
        <div className="row">
           {state.quotes?.map((quote,index)=>{return <div key={quote.id} className="col-md-3 p-2">
                <div className="card border" style={{"height":"300px"}}>
                    <h4 className="text-center bg-dark text-white p-2">{quote.author}</h4>
                    <p className="text-justify p-2">{quote.quote}</p>
                </div>
            </div>})} 
        </div>
      </div>
    </>
}

export default Quotes