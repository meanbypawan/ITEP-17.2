import { useSelector } from "react-redux";

function First(){
    let {counter,evenCounter,oddCounter} = useSelector((store)=>store.counters);
    return <>
      <h2>First Component...</h2>
      {counter} : {evenCounter} : {oddCounter}
    </>
}

export default First;