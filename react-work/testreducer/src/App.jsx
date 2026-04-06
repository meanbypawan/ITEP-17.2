import { useReducer, useRef } from "react";

function App(){
  const inputRef = useRef();
  const [state,dispatch] = useReducer((state,action)=>{
    console.log(action);
    if(action.type == "increment"){
      state.counter = state.counter + 1
    }
    else if(action.type=="decrement"){
      state.counter = state.counter - 1
    }
    else if(action.type=="increment-by-value"){
      state.counter = state.counter + action.payload*1;
    }
    return {...state}
  },{counter: 100});
  return <>
     <h1>App component...{state.counter}</h1>
     <button onClick={()=>{dispatch({type:"increment"})}}>Increment</button>
     <button onClick={()=>{dispatch({type:"decrement"})}}>Decrement</button>
     <br/><br/>
     <input ref={inputRef} type="text" placeholder="Enter value"/>
     <button onClick={()=>{dispatch({type:"increment-by-value",payload: inputRef.current.value})}}>Increment by value</button>
  </>
}

export default App;