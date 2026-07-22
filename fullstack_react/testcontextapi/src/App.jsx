import { createContext, useState } from "react"
import First from "./components/First"

export const MessageContext =  createContext()
export const CounterContext = createContext()
function App(){
  const [counter,setCounter] = useState(100)
  return <>
    <h1>App Component...{counter}</h1>
    <MessageContext.Provider value={{m1:"GM",m2:"GN"}}>
      <CounterContext.Provider value={{counter:counter,setCounter:setCounter}}>
       <First/>
      </CounterContext.Provider> 
    </MessageContext.Provider>
    
  </>
}

export default App



