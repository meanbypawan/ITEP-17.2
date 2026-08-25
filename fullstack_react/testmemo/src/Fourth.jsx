import React from "react";
function Fourth({sayHello}){
    console.log("Fourth Rerender....")
    return <>
       <h1>Fourth Component...</h1>
       <button onClick={()=>sayHello()}>Say Hello</button>
    </>
}

export default React.memo(Fourth);