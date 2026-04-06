import { useDispatch, useSelector } from "react-redux";
import { decrementCounter, incrementAll, incrementCounter, incrementEvenCounter } from "../redux-config/CounterSlice";
import { useRef } from "react";

function Second(){
    let {counter,evenCounter,oddCounter} = useSelector((store)=>store.counters);
    const dispatch = useDispatch();
    const inputRef = useRef();
    const handleAll = ()=>{
        let value = inputRef.current.value;
        if(value)
         dispatch(incrementAll({val: value}));
    }
    return <>
      <h2>Second component...</h2>
      {counter} : {evenCounter} : {oddCounter}
      <br/><br/>
      <button onClick={()=>dispatch(incrementCounter())}>Increment-Counter</button>
      <button onClick={()=>dispatch(decrementCounter())}>Decrement-counter</button>
      <br></br>
      <button onClick={()=>{dispatch(incrementEvenCounter())}}>Increment Even Counter</button>
      <br/><br/><br/>
      <input ref={inputRef} type="text" placeholder="Enter value"/>
      <button onClick={handleAll}>Increment-all</button>
    </>
}

export default Second;