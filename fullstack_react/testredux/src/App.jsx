import { useDispatch, useSelector } from "react-redux"
import { incrementCounter, incrementEvenCounter, incrementOddCounter } from "./redux-config/CounterSlice"
import ToDo from "./ToDo"
import { useEffect } from "react"
import { fetchToDos } from "./redux-config/ToDoSlice"

function App(){
  let {counter,evenCounter,oddCounter}= useSelector((store)=>store.CounterData)
  const dispatch = useDispatch()

  useEffect(()=>{
    dispatch(fetchToDos())
  },[])

return <>
     <h1>App Component.....</h1>
     {counter} : {evenCounter} : {oddCounter}
     <button onClick={()=>dispatch(incrementCounter())}>Counter</button>
     <button onClick={()=>dispatch(incrementEvenCounter())}>Even-counter</button>
     <button onClick={()=>dispatch(incrementOddCounter())}>Odd-counter</button>
     <hr/>
     <ToDo/>
  </>
}

export default App