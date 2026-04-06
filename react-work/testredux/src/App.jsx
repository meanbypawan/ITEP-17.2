import { useSelector } from "react-redux";
import First from "./components/First";
import Second from "./components/Second";

function App(){
  let {m1,m2} = useSelector((store)=>store.messages);
  let {counter,evenCounter,oddCounter} = useSelector((store)=>store.counters)
  return <>
    <h1>App component...{m1} : {m2}</h1>
    <h1>{counter} : {evenCounter} : {oddCounter}</h1>
    <hr/>
    <First/>
    <hr/>
    <Second/>
  </>
}
export default App;