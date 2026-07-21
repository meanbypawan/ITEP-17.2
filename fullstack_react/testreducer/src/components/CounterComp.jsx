import { useReducer } from "react"

function CounterComp(){
    const [state,dispatch] = useReducer((state,action)=>{
        // State Logic
        if(action.type == "increment-even"){
             state.evenCounter = state.evenCounter + 2
        }
        else if(action.type == "decrement-even"){
           state.evenCounter = state.evenCounter - 2
        }
        else if(action.type == "increment-odd")
            state.oddCounter += 2
        else if(action.type == "decrement-odd")
            state.oddCounter -= 2
        
        return {...state}
    },{evenCounter:0, oddCounter:1})
    return <>
      <h1>Counter Component....</h1>
      <center>
         <h1>Even Counter : {state.evenCounter}</h1>
         <button onClick={()=>{dispatch({"type":"increment-even"})}}>Increment</button>
         <button onClick={()=>dispatch({"type":"decrement-even"})}>Decrement</button>
      </center> 
      <hr/>
      <hr/>
      <center>
         <h1>Odd Counter : {state.oddCounter}</h1>
         <button onClick={()=>dispatch({type:"increment-odd"})}>Increment</button>
         <button onClick={()=>dispatch({type:"decrement-odd"})}>Decrement</button>
      </center> 
    </>
}
export default CounterComp;